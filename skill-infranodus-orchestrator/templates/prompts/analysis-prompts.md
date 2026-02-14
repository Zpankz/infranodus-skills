# Analysis Prompt Templates

> **Layer**: 5 | **Dependencies**: `core/api-reference.md`, `modules/graph-generation`, `modules/content-analysis`
> **Tags**: `#template` `#prompts` `#analysis`

## Text Analysis Prompt
```
Analyze the following text using generate_knowledge_graph to identify its main topics,
conceptual clusters, content gaps, and key relationships. Present:
1. Main topical clusters and their key concepts
2. Content gaps between clusters (opportunities for development)
3. Most influential nodes (gateway concepts)
4. Diversity statistics (is the text balanced or dominated by one topic?)
```

## Gap Analysis Prompt
```
Use generate_content_gaps to find structural holes in the following text.
For each gap identified:
- Which two clusters does it connect?
- What concepts could bridge it?
- What's the creative potential of bridging this gap?
```

## Topic Analysis Prompt
```
Use generate_topical_clusters to extract the thematic structure.
Present clusters ranked by:
1. Size (number of concepts)
2. Influence (betweenness centrality of top nodes)
3. Interconnectedness (cross-cluster edges)
```

## Comparative Analysis Prompt
```
Compare these texts using both overlap_between_texts and difference_between_texts:
1. First, find what they share (common ground)
2. Then, find what text 1 is missing relative to the others
3. Synthesize: map the gaps in shared context as innovation space
```

## Research Questions Prompt
```
Use generate_research_questions on the following text/topic.
Present questions organized by:
- Which gap they bridge
- Potential impact if answered
- Feasibility of investigation
```

## Develop Text Prompt
```
Use develop_text_tool for comprehensive analysis of the following text:
Phase 1: Content gaps — what's structurally missing?
Phase 2: Latent topics — what's underdeveloped but present?
Phase 3: Conceptual bridges — how does this connect to broader discourse?
Synthesize all three phases into actionable development recommendations.
```

## Memory Save Prompt
```
Save the following content to memory using memory_add_relations.
Graph name: {name} (max 28 chars, lowercase, dashes for spaces)
Format entities as [[wikilinks]] and separate statements with newlines.
```
