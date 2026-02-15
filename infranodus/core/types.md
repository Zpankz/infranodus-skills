# Core Type System

> **Layer**: 0 (Root) | **Dependencies**: None | **Dependents**: All modules
> **Tags**: `#foundation` `#types` `#schema` `#symbolic`

## Graph Primitives

### GraphNode
```
id: string            # Unique node identifier
label: string         # Display name
degree: number        # Connection count
bc: number            # Betweenness centrality (0..1)
community: number     # Cluster membership ID
weighedDegree: number # Weighted connection sum
x, y: number          # Layout coordinates
```

### GraphEdge
```
source: string    # Source node ID
target: string    # Target node ID
id: string        # Edge identifier
weight: number    # Connection strength
```

### TopCluster
```
community: string                              # Cluster ID
nodes: Array<{ nodeName, degree, bc }>         # Member nodes ranked by centrality
statementIds: number[]                         # Associated statement indices
topStatementId: number                         # Most representative statement
aiName: string                                 # AI-generated cluster label
```

### GraphGap
```
source: string       # Source cluster/concept
target: string       # Target cluster/concept
weight: number       # Gap significance (higher = more potential)
concepts: string[]   # Concepts that could bridge this gap
```

### Statement
```
id: number
content: string
contextId: number
categories: string[]
createdAt: string
statementHashtags: string[]
statementCommunities: string[]
topStatementCommunity: string
similarityScore: number        # When used in RAG retrieval
```

## Composite Types

### KnowledgeGraphOutput
```
statistics:
  modularity: number             # Graph modularity (0=uniform, 1=highly clustered)
  clusterCount: number           # Number of topical clusters
  nodeCount: number              # Total concept nodes
  edgeCount: number              # Total relation edges
  diversityStats:
    diversity_score: string
    too_focused_on_top_nodes: boolean
    too_focused_on_top_clusters: boolean
    top_nodes_entropy: number
    ratio_of_top_nodes_influence_by_betweenness: number
    ratio_of_top_cluster_influence_by_betweenness: number
    total_clusters: number
    fair_influence_by_cluster: number
graphSummary: string             # AI-generated overview
contentGaps: string[]            # Structural gaps between clusters
mainTopicalClusters: string[]    # Named topic groups
mainConcepts: string[]           # Key concepts
topInfluentialNodes: Array<{ node, degree, bc }>
conceptualGateways: string[]     # Bridge concepts between clusters
topRelations: string[]           # Strongest concept pairs
topBigrams: string[]             # Key two-word combinations
statements: Statement[]          # Extracted statements
```

### GraphRagOutput
```
retrievedStatements: Array<{
  content: string
  categories: string[]
  topStatementCommunity: string
  similarityScore: number
}>
graphSummary: string
contentGaps: string[]
mainTopicalClusters: string[]
topInfluentialNodes: Array<{ node, degree, bc }>
```

## Cognitive Types

### CognitiveState
```
mode: "biased" | "focused" | "diversified" | "dispersed"
scale: "zoomed_in" | "zoomed_out"
intent: "connecting" | "exploring"
dwellingTime: number             # Exchanges in current state
energyLevel: "high" | "medium" | "low"
emotionalSignal: EmotionalSignal
```

### EmotionalSignal
```
type: "continue" | "transition"
emotion: "inspiration" | "excitement" | "flow" | "satisfaction"
       | "exhaustion" | "frustration" | "despair" | "boredom" | "anxiety"
intensity: number                # 0..1
```

### PatternSignal
```
source: "grammar" | "punctuation" | "structure" | "semantic"
pattern: string                  # Description of detected pattern
cognitiveImplication: string     # What this suggests about cognitive state
suggestedAction: string          # Recommended intervention
priority: "highest" | "high" | "moderate" | "low"
```

## Ontology Types

### OntologyRelation
```
entity1: string        # Source entity in [[wikilinks]]
relation: string       # Natural language relation description
entity2: string        # Target entity in [[wikilinks]]
code: RelationCode     # Formal relation type
```

### RelationCode
```
"isA" | "partOf" | "hasAttribute" | "relatedTo" | "dependentOn"
| "causes" | "locatedIn" | "occursAt" | "derivedFrom" | "opposes"
```

## Platform Types

### ToolInvocation
```
toolName: string
parameters: Record<string, any>
progressCallback: (percent: number, message: string) => void
```

### SkillHandoff
```
sourceSkill: string
targetSkill: string
trigger: string
context: Record<string, any>
priority: "highest" | "high" | "moderate" | "low"
```

## Port Connections
- **Consumed by**: `→ core/graph-analytics.md` `→ core/api-reference.md` `→ modules/*` `→ bridges/*`
