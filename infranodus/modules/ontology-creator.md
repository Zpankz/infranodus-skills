# Ontology Creator Module

> **Layer**: 3 | **Dependencies**: `core/types.md`, `core/ontology.md`, `core/api-reference.md`
> **Dependents**: `bridges/skill-tool-map`, `bridges/workflow-orchestrator`
> **Tags**: `#skill` `#ontology` `#knowledge-graph` `#wikilinks` `#symbolic`

## Activation Trigger
Generate comprehensive ontological knowledge graphs in [[wikilinks]] syntax for InfraNodus visualization. Use when the user requests to create an ontology, extract entities and relationships from text, or generate knowledge graph structures. Handles both topic-based ontology generation and entity extraction from existing text. Output formatted for direct paste into InfraNodus.com.

## Input Types

### 1. Topic-Based Generation
Given a topic/domain, generate a comprehensive ontology covering:
- Core entities and their relationships
- Classes, subclasses, and membership
- Properties, attributes, and characteristics
- Causal chains and dependencies
- Spatial and temporal relations
- Opposing forces and tensions

### 2. Text-Based Extraction
Given existing text, extract ontological structure:
- Named entities and concepts
- Implicit relationships between entities
- Classification into relation types
- Network topology from textual co-occurrence

## Output Format
```
[[entity1]] natural language relation [[entity2]] [relationCode]
```

### Relation Codes (see `core/ontology.md` for full taxonomy)
`[isA]` `[partOf]` `[hasAttribute]` `[relatedTo]` `[dependentOn]` `[causes]` `[locatedIn]` `[occursAt]` `[derivedFrom]` `[opposes]`

### Requirements
1. Each statement: minimum 2 entities in `[[wikilinks]]`
2. Each statement: exactly one `[relationCode]` at end
3. Minimum 8 statements per relation code type
4. Output in code block for easy copying
5. NO explanations, descriptions, or meta-commentary
6. Network topology — NOT tree/hierarchy
7. Distribute entities — avoid hub-and-spoke patterns

### Anti-Pattern Detection
```
BAD (hub-and-spoke):
  [[X]] relates to [[A]] [relatedTo]
  [[X]] relates to [[B]] [relatedTo]
  [[X]] relates to [[C]] [relatedTo]   ← X appears in EVERY statement

GOOD (network):
  [[A]] connects to [[B]] [relatedTo]
  [[B]] is part of [[C]] [partOf]
  [[C]] opposes [[D]] [opposes]
  [[D]] derives from [[A]] [derivedFrom]  ← distributed entity usage
```

## InfraNodus Tool Integration

### After Generation
| Tool | Action | Purpose |
|------|--------|---------|
| `create_knowledge_graph` | Save ontology as persistent graph | Preserve for ongoing use |
| `generate_knowledge_graph` | Analyze ontology quality | Check topology, find gaps |
| `memory_add_relations` | Save as memory graph | Long-term retrieval |
| `memory_get_relations` | Retrieve existing ontology | Build on previous work |
| `search` | Find related graphs in account | Connect to existing knowledge |

### Quality Feedback Loop
```
1. Generate ontology
2. Analyze via generate_knowledge_graph
3. Check: modularity 0.3–0.6? Hub avoidance? Cross-cluster links?
4. If not → adjust entity distribution and regenerate
5. Save via create_knowledge_graph or memory_add_relations
```

## Cognitive Variability Integration
Use the cognitive variability framework to improve ontology balance:
- **BIASED ontology**: Too centered on one entity → diversify
- **FOCUSED ontology**: Good connections but narrow scope → explore new domains
- **DIVERSIFIED ontology**: Multiple clusters with gaps → bridge the gaps
- **DISPERSED ontology**: Fragmented, no coherence → focus on core relations

## Port Connections
- **Depends on**: `← core/types.md` `← core/ontology.md` `← core/api-reference.md`
- **Receives from**: `← modules/writing-assistant.md` (entity marking suggestions)
- **Orchestrated by**: `← bridges/workflow-orchestrator.md`
