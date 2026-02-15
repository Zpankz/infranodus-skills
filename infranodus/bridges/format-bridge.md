# Bridge: Format Conversion

> Unifies graph output conversion across platforms and output types.
> Connects: core/types.md
> Deps: [core/types.md]

## Output Format Matrix

| Source | Target | Converter | Use When |
|---|---|---|---|
| GraphResponse | KnowledgeGraphOutput | transformToStructuredOutput | Standard analysis display |
| GraphResponse | [[wikilinks]] ontology | ontology formatter | Ontology generation |
| GraphResponse | Obsidian markdown | obsidian formatter | Vault integration |
| GraphResponse | Mermaid diagram | mermaid formatter | Visual documentation |
| GraphResponse | DOT/GraphViz | dot formatter | External visualization |
| GraphResponse | Graphology JSON | json formatter | Programmatic access |
| GraphResponse | VSCode Log | log formatter | Extension sidebar |

## Transform: GraphResponse → Structured Output

```python
# Core transform (mirrors transformers.ts logic)
def transform_to_structured(response):
    graph = response.graph.graphologyGraph
    return {
        "statistics": {
            "nodes": len(graph.nodes),
            "edges": len(graph.edges),
            "modularity": graph.attributes.modularity,
            "density": len(graph.edges) / max(len(graph.nodes)**2, 1)
        },
        "graphSummary": graph.attributes.get("graphSummary", ""),
        "topInfluentialNodes": sorted(graph.nodes, key=lambda n: n.bc, reverse=True)[:10],
        "knowledgeGraphByCluster": group_statements_by_cluster(response.statements, graph.attributes.top_clusters),
        "topClusters": graph.attributes.top_clusters,
        "gaps": graph.attributes.gaps
    }
```

## Transform: GraphResponse → Obsidian Markdown

```markdown
---
type: infranodus-analysis
created: {timestamp}
modularity: {modularity}
clusters: {cluster_count}
gaps: {gap_count}
tags: [infranodus, knowledge-graph, {topic_tags}]
---

# {graph_name} Analysis

## Key Clusters
{for cluster in top_clusters}
### {cluster.aiName}
> [!cluster] Nodes: {cluster.nodes[].nodeName}
{cluster statements}
{end}

## Structural Gaps
{for gap in gaps}
> [!gap] {gap.source} ↔ {gap.target}
> Weight: {gap.weight} | Bridging concepts: {gap.concepts}
{end}

## Research Questions
{for question in research_questions}
> [!question] {question}
{end}
```

## Transform: GraphResponse → Mermaid

```
graph TD
{for edge in top_edges}
    {edge.source}["{source_label}"] --> {edge.target}["{target_label}"]
{end}

{for cluster in clusters}
    subgraph {cluster.aiName}
    {cluster.nodes[].nodeName}
    end
{end}
```

## Platform-Specific Formatting

### For Obsidian Plugin Context
- Preserve [[wikilinks]] matching vault note names
- Include backlink analysis context
- Use callout types: `[!insight]`, `[!gap]`, `[!question]`, `[!cluster]`

### For VSCode Extension Context
- Compress to JSON log format
- Include file/folder path references
- Generate AI copilot prompts from gaps

### For InfraNodus Direct
- Standard GraphResponse format
- Include graph URL link when saved
