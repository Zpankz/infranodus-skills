# Graph Generation Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`, `core/graph-analytics.md`
> **Dependents**: `modules/cognitive-variability`, `modules/ontology-creator`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#graph` `#generation` `#symbolic`

## Tools in this Module

### 1. generate_knowledge_graph
**Purpose**: Analyze text or URL into a knowledge graph without saving.
**Endpoint**: `/graphAndStatements` (read-only, idempotent)
**When to use**: Whenever you need to understand the topical structure of any content — text, URL, conversation transcript, document. This is the primary analysis entry point.

**Parameters**:
| Param | Required | Default | Description |
|-------|----------|---------|-------------|
| `text` | one of text/url | — | Text content (supports [[wikilinks]] for entity marking) |
| `url` | one of text/url | — | URL to analyze |
| `includeStatements` | no | false | Return individual statements |
| `includeGraph` | no | false | Return raw graph structure |
| `addNodesAndEdges` | no | false | Return node/edge arrays |
| `modifyAnalyzedText` | no | "none" | Entity detection mode |
| `includeGraphSummary` | no | true | Include AI-generated summary |

**Returns**: `KnowledgeGraphOutput` — statistics, graphSummary, contentGaps, mainTopicalClusters, mainConcepts, topInfluentialNodes, conceptualGateways, topRelations, topBigrams

**Cognitive bridge**: The output's modularity and gap structure directly map to cognitive states (see `bridges/state-transition-engine.md`).

### 2. create_knowledge_graph
**Purpose**: Create and SAVE a persistent graph in user's InfraNodus account.
**Endpoint**: `/graphAndStatements` (NOT read-only, NOT idempotent)
**When to use**: When the user explicitly wants to save a graph for later retrieval, memory, or ongoing analysis. Not for one-off analysis.

**Additional params**:
| Param | Required | Description |
|-------|----------|-------------|
| `name` | yes | Graph name (max 28 chars, lowercase, dashes) |

**Returns**: Same as generate_knowledge_graph, plus `graphUrl` and `graphName`

### 3. analyze_existing_graph_by_name
**Purpose**: Retrieve and analyze an already-saved graph.
**Endpoint**: `/graphAndStatements` (read-only, idempotent)
**When to use**: When the user references a previously created graph by name, or when checking current state of an evolving graph.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `name` | yes | Name of existing graph |

**Returns**: Full `KnowledgeGraphOutput` for the named graph

### 4. generate_contextual_hint
**Purpose**: Generate a concise topical overview for augmenting LLM responses (lightweight GraphRAG).
**Endpoint**: `/graphAndStatements` (read-only, idempotent)
**When to use**: Quick context augmentation — when you need a brief overview rather than full analysis.

**Returns**: `{ textOverview: string }` — a compact topical summary

### 5. retrieve_from_knowledge_base
**Purpose**: GraphRAG retrieval — query an existing graph with natural language.
**Endpoint**: `/graphAndAdvice` (read-only, idempotent)
**When to use**: When the user asks a question that should be answered using data from an existing graph. This is the primary RAG mechanism.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `name` | yes | Graph name to query |
| `prompt` | yes | Natural language question |

**Returns**: `GraphRagOutput` — retrievedStatements (with similarity scores), graphSummary, contentGaps, mainTopicalClusters

## Decision Tree
```
Need to analyze content?
├── One-off analysis → generate_knowledge_graph
├── Save for later → create_knowledge_graph
├── Check existing → analyze_existing_graph_by_name
├── Quick overview → generate_contextual_hint
└── Query existing → retrieve_from_knowledge_base
```

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md` `← core/graph-analytics.md`
- **Consumed by**: `→ modules/cognitive-variability.md` `→ modules/ontology-creator.md` `→ modules/writing-assistant.md` `→ modules/seo-analysis.md`
- **Bridged via**: `→ bridges/skill-tool-map.md`
