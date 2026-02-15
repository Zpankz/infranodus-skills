# Memory Management Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`, `core/ontology.md`
> **Dependents**: `modules/ontology-creator`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#memory` `#persistence` `#storage` `#symbolic`

## Tools in this Module

### 1. memory_add_relations
**Purpose**: Save text, entities, and relations to a named memory graph (persistent, writable).
**Endpoint**: `/graphAndStatements` with `contextType: "memory"`, `doNotSave: false`
**When to use**: When the user wants to remember something, when building an ongoing knowledge base, when saving ontology relations for later retrieval.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `graphName` | yes | Memory graph name (max 28 chars, lowercase, dashes for spaces) |
| `text` | yes | Content to save (use [[wikilinks]] for entities, newlines between statements) |
| `includeStatements` | no | Return saved statements |
| `includeGraph` | no | Return graph structure |
| `modifyAnalyzedText` | no | Entity detection mode |

**Best practices**:
- Use [[wikilinks]] to explicitly mark entities
- Separate distinct facts with newlines
- Use consistent graph names for related memories
- Use relation codes when saving ontology: `[[A]] relates to [[B]] [relatedTo]`

### 2. memory_get_relations
**Purpose**: Retrieve stored relations by entity name or memory context.
**Endpoint**: `/graphAndStatements` (graph mode) or `/search` (search mode)
**When to use**: When recalling previously stored knowledge, when checking if information exists, when building context from memory.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `query` | yes | Entity name or search query |
| `graphName` | no | Specific memory graph to search |

**Returns**: `StatementsOutput` (graph mode) or `StatementsSearchOutput` (search mode)

**Modes**:
- **Graph mode**: Returns full graph of a named memory with all relations
- **Search mode**: Searches across all memories for matching content

## Memory Architecture
```
Memory Graph = Named, persistent knowledge store
  ├── Contains: statements with entity relations
  ├── Queryable: by entity name or free text
  ├── Cumulative: new additions merge into existing graph
  └── Analyzable: can run full graph analysis on memory graphs
```

## Integration with Ontology Creator
The Ontology Creator generates structured knowledge in wikilink format that feeds directly into memory_add_relations:
```
Ontology Creator generates:
  [[Entity1]] relation [[Entity2]] [relationCode]

Memory Manager saves:
  memory_add_relations({ graphName: "project-ontology", text: output })

Later retrieval:
  memory_get_relations({ query: "Entity1", graphName: "project-ontology" })
```

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md` `← core/ontology.md`
- **Consumed by**: `→ modules/ontology-creator.md`
- **Bridged via**: `→ bridges/skill-tool-map.md`
