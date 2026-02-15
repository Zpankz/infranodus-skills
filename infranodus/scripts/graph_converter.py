#!/usr/bin/env python3
"""
InfraNodus Graph Converter
Transforms InfraNodus graph output to multiple target formats.
Supports: Mermaid, Graphology JSON, DOT, Obsidian MD, Wikilinks Ontology
"""

import json
import sys
from datetime import datetime


def parse_infranodus_output(data: dict) -> dict:
    """Parse raw InfraNodus tool output into normalized structure."""
    result = {
        "nodes": [], "edges": [], "clusters": [],
        "gaps": [], "statements": [], "statistics": {}
    }
    
    if "graph" in data and "graphologyGraph" in data["graph"]:
        g = data["graph"]["graphologyGraph"]
        attrs = g.get("attributes", {})
        
        result["nodes"] = g.get("nodes", [])
        result["edges"] = g.get("edges", [])
        result["clusters"] = attrs.get("top_clusters", [])
        result["gaps"] = attrs.get("gaps", [])
        result["statistics"] = {
            "modularity": attrs.get("modularity", 0),
            "node_count": len(result["nodes"]),
            "edge_count": len(result["edges"]),
            "cluster_count": len(result["clusters"]),
            "gap_count": len(result["gaps"]),
            "top_nodes": attrs.get("top_nodes", [])
        }
    
    result["statements"] = data.get("statements", [])
    return result


def to_mermaid(graph: dict, diagram_type: str = "graph TD") -> str:
    """Convert to Mermaid diagram format."""
    lines = [diagram_type]
    
    # Add cluster subgraphs
    for cluster in graph["clusters"]:
        name = cluster.get("aiName", f"Cluster {cluster['community']}")
        lines.append(f'    subgraph {name.replace(" ", "_")}')
        for node in cluster.get("nodes", []):
            node_id = node["nodeName"].replace(" ", "_")
            lines.append(f'        {node_id}["{node["nodeName"]}"]')
        lines.append("    end")
    
    # Add edges (top 30 by weight)
    edges = sorted(graph["edges"], key=lambda e: e.get("weight", 0), reverse=True)[:30]
    for edge in edges:
        src = edge["source"].replace(" ", "_")
        tgt = edge["target"].replace(" ", "_")
        lines.append(f'    {src} --> {tgt}')
    
    # Add gap annotations
    for gap in graph["gaps"][:5]:
        src = gap["source"].replace(" ", "_")
        tgt = gap["target"].replace(" ", "_")
        lines.append(f'    {src} -.->|gap| {tgt}')
    
    return "\n".join(lines)


def to_graphology_json(graph: dict) -> str:
    """Convert to Graphology-compatible JSON."""
    output = {
        "attributes": graph["statistics"],
        "nodes": [
            {"key": n.get("id", n.get("label", "")), "attributes": n}
            for n in graph["nodes"]
        ],
        "edges": [
            {"source": e["source"], "target": e["target"], 
             "attributes": {"weight": e.get("weight", 1)}}
            for e in graph["edges"]
        ]
    }
    return json.dumps(output, indent=2)


def to_dot(graph: dict) -> str:
    """Convert to DOT/GraphViz format."""
    lines = ["digraph InfraNodus {", '    rankdir=LR;', '    node [shape=ellipse];']
    
    # Cluster subgraphs
    for i, cluster in enumerate(graph["clusters"]):
        name = cluster.get("aiName", f"Cluster {cluster['community']}")
        lines.append(f'    subgraph cluster_{i} {{')
        lines.append(f'        label="{name}";')
        for node in cluster.get("nodes", []):
            node_id = node["nodeName"].replace(" ", "_").replace('"', '\\"')
            lines.append(f'        "{node_id}";')
        lines.append("    }")
    
    # Edges
    for edge in graph["edges"]:
        src = edge["source"].replace('"', '\\"')
        tgt = edge["target"].replace('"', '\\"')
        w = edge.get("weight", 1)
        lines.append(f'    "{src}" -> "{tgt}" [weight={w}];')
    
    lines.append("}")
    return "\n".join(lines)


def to_obsidian_md(graph: dict, title: str = "Graph Analysis") -> str:
    """Convert to Obsidian-compatible markdown with frontmatter."""
    stats = graph["statistics"]
    now = datetime.now().isoformat()
    
    lines = [
        "---",
        "type: infranodus-analysis",
        f"created: {now}",
        f"modularity: {stats.get('modularity', 0):.3f}",
        f"clusters: {stats.get('cluster_count', 0)}",
        f"gaps: {stats.get('gap_count', 0)}",
        "tags: [infranodus, knowledge-graph]",
        "---", "",
        f"# {title}", ""
    ]
    
    # Top nodes
    if stats.get("top_nodes"):
        lines.append("## Key Concepts")
        for node in stats["top_nodes"][:10]:
            lines.append(f"- [[{node}]]")
        lines.append("")
    
    # Clusters
    if graph["clusters"]:
        lines.append("## Topical Clusters")
        for cluster in graph["clusters"]:
            name = cluster.get("aiName", f"Cluster {cluster['community']}")
            lines.append(f"\n### {name}")
            lines.append(f"> [!cluster] Nodes: {', '.join(n['nodeName'] for n in cluster.get('nodes', [])[:8])}")
        lines.append("")
    
    # Gaps
    if graph["gaps"]:
        lines.append("## Structural Gaps")
        for gap in graph["gaps"]:
            concepts = ", ".join(gap.get("concepts", []))
            lines.append(f"> [!gap] **{gap['source']}** ↔ **{gap['target']}**")
            lines.append(f"> Weight: {gap.get('weight', 0):.2f} | Bridging: {concepts}")
            lines.append("")
    
    return "\n".join(lines)


RELATION_TEMPLATES = {
    "isA": "{src} is a type of {tgt}",
    "partOf": "{src} belongs to {tgt}",
    "hasAttribute": "{src} has attribute {tgt}",
    "relatedTo": "{src} relates to {tgt}",
    "dependentOn": "{src} depends on {tgt}",
    "causes": "{src} causes {tgt}",
    "locatedIn": "{src} is located in {tgt}",
    "occursAt": "{src} occurs at {tgt}",
    "derivedFrom": "{src} is derived from {tgt}",
    "opposes": "{src} opposes {tgt}",
}


def to_wikilinks_ontology(graph: dict) -> str:
    """Convert graph to [[wikilinks]] ontology format."""
    lines = []
    for edge in graph["edges"]:
        src = edge["source"]
        tgt = edge["target"]
        relation = edge.get("relation", edge.get("label", "relatedTo"))
        if relation not in RELATION_TEMPLATES:
            relation = "relatedTo"
        template = RELATION_TEMPLATES[relation]
        lines.append(f"{template.format(src=f'[[{src}]]', tgt=f'[[{tgt}]]')} [{relation}]")

    # Add cluster membership
    for cluster in graph["clusters"]:
        name = cluster.get("aiName", f"cluster_{cluster['community']}")
        for node in cluster.get("nodes", []):
            lines.append(f"[[{node['nodeName']}]] belongs to [[{name}]] [partOf]")

    return "\n".join(lines)


CONVERTERS = {
    "mermaid": to_mermaid,
    "graphology": to_graphology_json,
    "dot": to_dot,
    "obsidian": to_obsidian_md,
    "wikilinks": to_wikilinks_ontology
}


def convert(data: dict, target_format: str, **kwargs) -> str:
    """Main conversion entry point."""
    graph = parse_infranodus_output(data)
    converter = CONVERTERS.get(target_format)
    if not converter:
        raise ValueError(f"Unknown format: {target_format}. Available: {list(CONVERTERS.keys())}")
    return converter(graph, **kwargs)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <format> [input.json]")
        print(f"Formats: {', '.join(CONVERTERS.keys())}")
        sys.exit(1)
    
    fmt = sys.argv[1]
    input_file = sys.argv[2] if len(sys.argv) > 2 else "-"
    
    if input_file == "-":
        data = json.load(sys.stdin)
    else:
        with open(input_file) as f:
            data = json.load(f)
    
    print(convert(data, fmt))
