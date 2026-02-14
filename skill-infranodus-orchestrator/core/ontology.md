# Ontology Schema & Relation System

> **Layer**: 0 (Root) | **Dependencies**: None | **Dependents**: `modules/ontology-creator`, `bridges/skill-tool-map`
> **Tags**: `#foundation` `#ontology` `#relations` `#symbolic`

## Relation Code Taxonomy

Ten formal relation types for knowledge graph construction. Each defines a semantic edge type in the graph.

### Structural Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[isA]` | Class membership / taxonomy | memberOf | `[[neural network]] is a type of [[machine learning]] [isA]` |
| `[partOf]` | Compositional containment | hasPart | `[[attention head]] is a component of [[transformer]] [partOf]` |
| `[derivedFrom]` | Origin / lineage / adaptation | givesRiseTo | `[[BERT]] was adapted from [[transformer architecture]] [derivedFrom]` |

### Attributive Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[hasAttribute]` | Property / characteristic | attributeOf | `[[graph neural network]] exhibits [[permutation invariance]] [hasAttribute]` |
| `[relatedTo]` | General association / correlation | relatedTo (symmetric) | `[[betweenness centrality]] correlates with [[information flow]] [relatedTo]` |

### Causal Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[causes]` | Causal / produces / enables | causedBy | `[[cognitive bias]] leads to [[tunnel vision]] [causes]` |
| `[dependentOn]` | Requires / prerequisite | enabledBy | `[[gap analysis]] requires [[knowledge graph]] [dependentOn]` |
| `[opposes]` | Contradiction / tension / contrast | opposedBy | `[[exploration]] contrasts with [[exploitation]] [opposes]` |

### Spatiotemporal Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[locatedIn]` | Spatial containment / domain | contains | `[[semantic analysis]] operates in [[NLP domain]] [locatedIn]` |
| `[occursAt]` | Temporal / phase / stage | stageOf | `[[gap detection]] happens during [[diversified state]] [occursAt]` |

## Wikilink Syntax

```
[[Entity1]] natural language relation description [[Entity2]] [relationCode]
```

### Rules
1. Each entity enclosed in `[[double brackets]]`
2. Each statement has exactly one `[relationCode]` at end
3. Minimum 2 entities per statement
4. Relation description is natural language between entities
5. No hierarchical hub-and-spoke patterns — distribute entities across a network topology

### Anti-patterns
- **Hub-and-spoke**: One entity appearing in every statement (tree structure)
- **Disconnected components**: Entities with no cross-cluster connections
- **Missing relation codes**: Statements without formal type annotation

### Network Topology Requirements
- Entity frequency should follow a power-law distribution (few high-degree, many low-degree)
- Cross-cluster edges are essential (conceptual gateways)
- Target modularity: 0.3–0.6 (neither too uniform nor too fragmented)
- Minimum 8 statements per relation code type

## Ontology Generation Process

```
Input (topic or text)
  → Entity extraction (detect named concepts)
  → Relation inference (determine semantic connections)
  → Code assignment (classify each relation)
  → Topology validation (check for hub avoidance, cross-links)
  → Output as wikilink statements
```

## Port Connections
- **Consumed by**: `→ modules/ontology-creator.md` `→ modules/memory-manager.md`
- **Referenced by**: `→ resources/relation-codes-reference.md` `→ bridges/skill-tool-map.md`
