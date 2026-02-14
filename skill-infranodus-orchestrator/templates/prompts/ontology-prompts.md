# Ontology Generation Prompt Templates

> **Layer**: 5 | **Dependencies**: `core/ontology.md`, `modules/ontology-creator`
> **Tags**: `#template` `#prompts` `#ontology` `#knowledge-graph`

## Topic-Based Ontology Prompt
```
Generate a comprehensive ontological knowledge graph for the domain: {topic}

Requirements:
- Use [[wikilinks]] syntax: [[Entity1]] relation [[Entity2]] [relationCode]
- Cover ALL relation types: [isA] [partOf] [hasAttribute] [relatedTo] [dependentOn]
  [causes] [locatedIn] [occursAt] [derivedFrom] [opposes]
- Minimum 8 statements per relation type
- Generate a NETWORK, not a tree — avoid hub-and-spoke patterns
- Distribute entities across multiple relationships
- Include cross-domain connections
- Output ONLY the ontology in a code block — no explanations
```

## Text-Based Extraction Prompt
```
Extract the ontological structure from the following text.

For each entity pair identified:
1. Mark entities with [[wikilinks]]
2. Describe the relationship in natural language
3. Classify with the appropriate [relationCode]

Focus on:
- Named entities (people, organizations, concepts, technologies)
- Implicit relationships (causation, dependency, opposition)
- Cross-domain connections (how concepts from different areas relate)
- Temporal and spatial relationships

Output ONLY the ontology in a code block.
```

## Ontology Quality Check Prompt
```
Analyze this ontology for structural quality:

1. Hub detection: Does any entity appear in >25% of statements?
2. Cluster balance: Are there multiple distinct topic clusters?
3. Cross-cluster edges: Do clusters connect to each other?
4. Relation diversity: Are all 10 relation codes represented?
5. Modularity: Is the network neither too uniform nor too fragmented?

Suggest specific improvements if issues are found.
```

## Ontology Expansion Prompt
```
Given the existing ontology below, expand it by:
1. Identifying underrepresented relation types
2. Finding entities that lack sufficient connections
3. Adding cross-domain bridges between isolated clusters
4. Introducing opposing concepts ([opposes]) where only agreement exists
5. Adding temporal ([occursAt]) and spatial ([locatedIn]) grounding

Maintain the same [[wikilinks]] + [relationCode] format.
```

## Ontology-to-Memory Save Prompt
```
Save this ontology to InfraNodus memory:
- Graph name: {sanitized_topic_name} (max 28 chars, lowercase, dashes)
- Use memory_add_relations with the full ontology text
- Verify save by retrieving with memory_get_relations
```
