# Graph Metrics — Complete Reference

> **Layer**: 5 (Resource) | **Tags**: `#resource` `#reference` `#metrics` `#graph-theory`

## Network Metrics

### Modularity
```
Definition: Measure of graph decomposition into distinct communities
Range: 0 (uniform) to 1 (perfectly clustered)
Optimal: 0.3-0.6 for creative/analytical text
Low (<0.2): Undifferentiated — single dominant theme
High (>0.7): Siloed — disconnected topic islands
Cognitive mapping:
  < 0.2  → BIASED (single dominant idea)
  0.2-0.4 → FOCUSED (coherent narrative)
  0.4-0.7 → DIVERSIFIED (multiple perspectives)
  > 0.7 or fragmented → DISPERSED (scattered)
```

### Betweenness Centrality (BC)
```
Definition: How much a node bridges different parts of the network
Range: 0 (peripheral) to 1 (central bridge)
High BC: Conceptual gateways — key bridge concepts
Significance: Nodes with high BC control information flow between clusters
Application: Identifying leverage points for state transitions
```

### Degree
```
Definition: Number of edges connected to a node
Weighted: Sum of edge weights for a node
Distribution: Healthy graphs follow power-law (few hubs, many leaves)
Hub detection: Nodes with both high degree AND high BC dominate discourse
```

### Top Nodes Entropy
```
Definition: Information distribution uniformity among top nodes
Low entropy: Influence concentrated in few nodes (over-focused)
High entropy: Influence distributed across many nodes (balanced)
Application: Detecting unhealthy hub dominance
```

## Diversity Statistics

### diversity_score
Overall balance metric combining multiple indicators.

### too_focused_on_top_nodes
Boolean flag indicating hub dominance — a few nodes carry disproportionate influence.

### too_focused_on_top_clusters
Boolean flag indicating cluster dominance — one cluster overshadows others.

### ratio_of_top_nodes_influence_by_betweenness
How much the top gateway nodes control information flow.

### ratio_of_top_cluster_influence_by_betweenness
How much the top cluster controls inter-cluster connections.

### total_clusters
Absolute count of detected communities.

### fair_influence_by_cluster
Expected per-cluster influence if influence were distributed equally.

## Structural Analysis

### Gaps
```
Definition: Missing connections between clusters that SHOULD exist
Components:
  source: originating cluster/concept
  target: destination cluster/concept
  weight: gap significance (higher = more potential)
  concepts: potential bridging concepts
Significance: Gaps = creative potential = innovation space
```

### Clusters
```
Definition: Communities of densely connected nodes
Components:
  community: cluster ID
  nodes: member nodes with degree and BC
  topStatementId: most representative statement
  aiName: AI-generated descriptive name
Assessment:
  Intra-cluster density: internal cohesion
  Inter-cluster edges: cross-topic connections
  Balance ratio: largest/smallest cluster (target <3:1)
```

### DOT Graph Representation
```
Format: Graphviz DOT language
Structure: Subgraphs per cluster + inter-cluster edges
Used for: Visualization, AI context, structural analysis
Partitioned: dotGraphByCluster separates by community
```

## Cognitive State Mapping Summary

| Metric | BIASED | FOCUSED | DIVERSIFIED | DISPERSED |
|--------|--------|---------|-------------|-----------|
| Modularity | < 0.2 | 0.2-0.4 | 0.4-0.7 | > 0.7/fragmented |
| Top node dominance | Very high | Moderate | Low | Low/chaotic |
| Cluster count | 1-2 | 2-4 | 4-8 | Many small |
| Significant gaps | Few | Few | Many | Many trivial |
| Diversity score | Low | Moderate | High | Chaotic |
| Narrative coherence | Single thread | Clear arc | Multiple arcs | No arc |
| Creative potential | Implementation | Refinement | Cross-pollination | Maximum generation |
