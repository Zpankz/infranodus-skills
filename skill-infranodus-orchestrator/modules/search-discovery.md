# Search & Discovery Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`
> **Dependents**: `modules/ontology-creator`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#search` `#discovery` `#retrieval` `#symbolic`

## Tools in this Module

### 1. list_graphs
**Purpose**: List all user's graphs with optional filters.
**Endpoint**: `/listGraphs`
**When to use**: When the user wants to see what graphs they have, when searching for a graph by name, or when checking available data.

**Parameters**:
| Param | Required | Default | Description |
|-------|----------|---------|-------------|
| `query` | no | — | Filter by name substring |
| `type` | no | — | Filter by type |
| `language` | no | — | Filter by language |
| `favorite` | no | — | Filter favorites only |

**Returns**: Array of graph metadata (name, url, type, date, language)

### 2. search
**Purpose**: Search across existing graphs by content query.
**Endpoint**: `/search`
**When to use**: When looking for specific content across all graphs, when trying to find related work, or when building context from existing knowledge.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `query` | yes | Search query |
| `contextNames[]` | no | Limit to specific graphs |
| `contextTypes[]` | no | Limit to graph types |

**Returns**: `SearchOutput` — results with compound IDs (`user:graph:query`), titles, URLs

### 3. fetch
**Purpose**: Fetch a specific search result by compound ID for detailed content.
**Endpoint**: `/search`
**When to use**: After running `search` to get result IDs, fetch specific results for full content.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `id` | yes | Compound ID from search results (`user:graph:query`) |

**Returns**: `FetchOutput` — id, title, full text, URL

## Search Workflow
```
1. list_graphs → Browse available graphs
2. search → Find relevant content across graphs
3. fetch → Get detailed content from specific results
```

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md`
- **Consumed by**: `→ modules/ontology-creator.md`
- **Bridged via**: `→ bridges/skill-tool-map.md`
