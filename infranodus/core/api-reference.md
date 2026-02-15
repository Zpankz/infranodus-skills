# InfraNodus API Reference

> **Layer**: 1 | **Dependencies**: `core/types.md` | **Dependents**: All `modules/*` tool modules
> **Tags**: `#core` `#api` `#reference` `#symbolic`

## Connection

```
Base URL: https://infranodus.com/api/v1
Auth: Bearer {INFRANODUS_API_KEY}
Content-Type: application/json
All requests include: { modal: "mcp_server" }
Response wrapper: data.entriesAndGraphOfContext (unwrapped by client)
```

## Endpoints

### /graphAndStatements (POST)
**Primary endpoint** — generates knowledge graph from text or URL.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `text` | string | Input text (supports [[wikilinks]]) |
| `url` | string | URL to analyze (alternative to text) |
| `name` | string | Graph name (for saving) |
| `doNotSave` | boolean | If true, ephemeral analysis |
| `addStats` | boolean | Include graph statistics |
| `dotGraph` | boolean | Include DOT representation |
| `optimize` | string | Analysis mode: "develop", "gap" |
| `requestMode` | string | "question" for research questions |
| `aiTopics` | boolean | Generate AI topic names |
| `extendedGraphSummary` | boolean | Include full summary with gaps, topics, concepts |
| `contextType` | string | "memory" for memory storage |
| `partOfSpeechToProcess` | string | "HASHTAGS_AND_WORDS", "HASHTAGS_ONLY", "WORDS_IF_NO_HASHTAGS" |
| `doubleSquarebracketsProcessing` | string | "PROCESS_AS_HASHTAGS", "EXCLUDE" |
| `mentionsProcessing` | string | "CONNECT_TO_ALL_CONCEPTS" |
| `modifyAnalyzedText` | string | "none", "detectEntities", "extractEntitiesOnly" |
| `modelToUse` | string | AI model selection |
| `gapDepth` | number | Depth of gap analysis (0 = default) |
| `useSeveralGaps` | boolean | Extend to multiple gaps |

**Returns**: `GraphResponse` (graph + statements + summaries + gaps)

**Used by tools**: generate_knowledge_graph, create_knowledge_graph, analyze_existing_graph_by_name, generate_content_gaps, generate_topical_clusters, generate_contextual_hint, generate_research_questions, memory_add_relations, memory_get_relations

### /graphAndAdvice (POST)
**AI advice endpoint** — generates recommendations based on graph analysis.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `text` / `url` | string | Input content |
| `name` | string | Existing graph name |
| `prompt` | string | User query for retrieval |
| `optimize` | string | "gap", "latent", "imagine", "develop" |
| `requestMode` | string | "question", "search" |

**Returns**: `GraphResponse` with `aiAdvice[]` array

**Used by tools**: develop_text_tool (3 sequential calls), generate_research_ideas, research_questions_from_graph, develop_latent_topics, develop_conceptual_bridges, generate_responses_from_graph, retrieve_from_knowledge_base

### /graphsAndStatements (POST)
**Multi-text comparison endpoint** — analyzes overlap/difference between texts.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `texts[]` | array | Array of { text, url } objects |
| `comparisonType` | string | "overlap" or "difference" |

**Returns**: `GraphResponse` with comparative analysis

**Used by tools**: overlap_between_texts, difference_between_texts

### /import/googleSearchResultsGraph (POST)
**SERP analysis** — knowledge graph from Google search results.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `searchQuery` | string | Search keywords |
| `importLanguage` | string | 2-letter language code |
| `importCountry` | string | 2-letter country code |

**Returns**: Graph of keywords found in search results (informational supply)

### /import/googleSearchQueriesGraph (POST)
**Search demand** — graph of related search queries/suggestions.

Same parameters as above.

**Returns**: Graph of related search queries (search demand)

### /import/googleSearchVsIntentGraph (POST)
**Supply-demand gap** — what people search vs what they find.

Same parameters as above.

**Returns**: Gap analysis between search queries and results

### /search (POST)
**Graph search** — search across existing graphs.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `query` | string | Search query |
| `contextNames[]` | array | Filter by graph names |
| `contextTypes[]` | array | Filter by graph types |

**Returns**: `SearchOutput` with results array

### /listGraphs (POST)
**Graph listing** — enumerate user's graphs.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `query` | string | Filter by name |
| `type` | string | Filter by type |
| `language` | string | Filter by language |
| `favorite` | boolean | Filter favorites |

**Returns**: Array of graph metadata

### /convert/url (POST)
**URL extraction** — converts URL to structured text.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `url` | string | Target URL |
| `useProxy` | boolean | Proxy for blocked sites |

**Returns**: `{ title, headerTags[], linkTags[], text }`

### /aiAdvice (POST) [Obsidian Plugin specific]
**AI advice** — generates AI advice from graph context.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `type` | string | "question", "develop", "summary", "response", "topics" |
| `prompt` | string | Constructed prompt with context |
| `promptContext` | string | Supporting context statements |
| `promptGraph` | string | DOT graph structure |
| `modelToUse` | string | AI model selection |

### /aiSearch (POST) [Obsidian Plugin specific]
**Semantic search** — embedding-based similarity search for chat RAG.

| Parameter | Type | Purpose |
|-----------|------|---------|
| `query` | string | Natural language query |
| `contextStatements` | array | Statements to search within |

**Returns**: Ranked statements by similarity

### /userId (POST)
**Authentication** — validates API key and returns user ID.

**Returns**: `{ userId: string }`

## Model Options
```
claude-opus-4.1, claude-opus-4.5, claude-sonnet-4, claude-sonnet-4.5,
gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite,
grok-4.1-fast-non-reasoning, grok-4.1-fast-reasoning,
gpt-4o, gpt-4o-mini, gpt-5, gpt-5-mini
```

## Language Codes
```
EN, DE, FR, ES, IT, PT, RU, CN, JP, NL, TW, KO, AR, HE
```

## Country Codes (30+)
```
US, GB, CA, AU, DE, FR, ES, IT, NL, BE, AT, CH, SE, NO, DK, FI,
PT, BR, MX, AR, CL, CO, JP, CN, TW, KR, IN, RU, IL, AE, SA, ZA, NG, KE, EG
```

## Port Connections
- **Depends on**: `← core/types.md`
- **Consumed by**: `→ modules/ontology-creator.md` `→ modules/critical-perspective.md` `→ modules/seo-analysis.md` `→ modules/writing-assistant.md` `→ modules/cognitive-variability.md`
