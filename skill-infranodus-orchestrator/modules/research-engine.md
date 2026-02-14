# Research Engine Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`
> **Dependents**: `modules/critical-perspective`, `modules/cognitive-variability`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#research` `#questions` `#ideas` `#neural`

## Tools in this Module

### 1. generate_research_questions
**Purpose**: Generate research questions that bridge content gaps.
**Endpoint**: `/graphAndStatements` with `optimize: "gap"`, `requestMode: "question"`
**When to use**: When the user needs research direction, when Critical Perspective identifies unexplored areas, or when in DIVERSIFIED cognitive state needing focus.

**Parameters**: text or url input

**Returns**: `{ questions: string[] }` — research questions derived from structural gaps

**Cognitive bridge**: Questions help transition from DIVERSIFIED (too many threads) to FOCUSED (clear direction) by selecting one gap to bridge.

### 2. generate_research_ideas
**Purpose**: Generate innovative research ideas from content gaps.
**Endpoint**: `/graphAndAdvice` with `optimize: "gap"`
**When to use**: When brainstorming, when in DISPERSED state needing creative fodder, or when existing analysis reveals untapped potential.

**Returns**: `{ ideas: string[] }` — creative research ideas from gaps

### 3. research_questions_from_graph
**Purpose**: Generate research questions from an existing saved graph.
**Endpoint**: `/graphAndAdvice` with `optimize: "gap"`, `requestMode: "question"`
**When to use**: When working with a previously saved graph and need new questions from its current state.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `name` | yes | Existing graph name |

**Returns**: `{ questions: string[] }`

### 4. develop_latent_topics
**Purpose**: Extract underdeveloped topics with expansion suggestions.
**Endpoint**: `/graphAndAdvice` with `optimize: "latent"`
**When to use**: When content has promising but underdeveloped threads, when Critical Perspective suggests hidden themes need surfacing.

**Returns**: `{ ideas: string[], mainTopics: string[], latentTopicsToDevelop: string[] }`

### 5. develop_conceptual_bridges
**Purpose**: Discover hidden patterns linking content to broader discourse.
**Endpoint**: `/graphAndAdvice` with `optimize: "imagine"`
**When to use**: When seeking cross-domain connections, when in DIVERSIFIED state wanting cross-pollination, or when Ontology Creator needs to connect isolated domains.

**Returns**: `{ ideas: string[], latentConceptsToDevelop: string[], latentConceptsRelations: string[] }`

### 6. generate_responses_from_graph
**Purpose**: Generate expert responses using existing graph data.
**Endpoint**: `/graphAndAdvice`
**When to use**: When the user needs answers grounded in existing graph knowledge, with optional custom prompt.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `name` | yes | Graph name |
| `prompt` | no | Custom question for response generation |

**Returns**: `{ responses: string[] }`

## Decision Tree
```
Need research support?
├── Generate questions from text → generate_research_questions
├── Generate questions from graph → research_questions_from_graph
├── Brainstorm ideas → generate_research_ideas
├── Find underdeveloped themes → develop_latent_topics
├── Cross-domain connections → develop_conceptual_bridges
└── Expert answers from graph → generate_responses_from_graph
```

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md`
- **Consumed by**: `→ modules/critical-perspective.md` `→ modules/cognitive-variability.md`
- **Bridged via**: `→ bridges/skill-tool-map.md`
