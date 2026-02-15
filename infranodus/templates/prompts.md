# Prompt Templates
Deps: core/types.md, core/ontology.md
Used-by: SKILL.md

## Advice Prompts

### Question Generation Prompt (from Obsidian)
```
Generate a question that uses the current context and the graph structure below:
{dotGraph}

Context statements:
{statements}
```

### Idea Development Prompt (from Obsidian)
```
Generate an idea that uses the current context and the graph structure below:
{dotGraph}

Context statements:
{statements}
```

### Summary Prompt (from Obsidian)
```
Summarize the content using the current context and the graph structure below:
{dotGraph}

Context statements:
{statements}
```

### Context Retrieval Prompt (from Obsidian)
```
Retrieve the most relevant content from the current context that relates
to the graph structure below:
{dotGraph}
```

### Gap Bridging Prompt (from Obsidian)
```
Find the gap in the current context that would bridge the graph structure below:
{dotGraph}
```

### Graph-Augmented Response Prompt (from VSCode)
```
Use the following knowledge graph data to make your response more precise:
{dotGraphByCluster}
```

### GraphRAG Retrieval Prompt
```
Using the knowledge stored in graph "{graphName}", answer the following question:
{userQuery}

Ground your response in the retrieved statements. Cite specific statements
where relevant. If the graph doesn't contain sufficient information, say so.
```

### Expert Response Prompt
```
Based on the knowledge graph "{graphName}", generate an expert response to:
{userQuery}

Draw on the graph's topical clusters, key relationships, and conceptual
gateways to provide a comprehensive, well-structured answer.
```

### Prompt Construction Guidelines (from Obsidian Plugin)
When building context prompts, follow this budget allocation:
```
maxPromptSize = MAX_CONTEXT_SIZE (54000 chars)
perTopicBudget = min(
  (maxPromptSize - currentSize) / totalTopics,
  summaryMode ? 5000 : 1500
)
```

Structure:
1. **prompt**: User question + keywords/bigrams or dotGraph per cluster
2. **promptGraph**: DOT graph filtered by selected topics + inter-cluster edges
3. **promptContext**: Per-cluster statement blocks within budget

## Analysis Prompts

### Text Analysis Prompt
```
Analyze the following text using generate_knowledge_graph to identify its main topics,
conceptual clusters, content gaps, and key relationships. Present:
1. Main topical clusters and their key concepts
2. Content gaps between clusters (opportunities for development)
3. Most influential nodes (gateway concepts)
4. Diversity statistics (is the text balanced or dominated by one topic?)
```

### Gap Analysis Prompt
```
Use generate_content_gaps to find structural holes in the following text.
For each gap identified:
- Which two clusters does it connect?
- What concepts could bridge it?
- What's the creative potential of bridging this gap?
```

### Topic Analysis Prompt
```
Use generate_topical_clusters to extract the thematic structure.
Present clusters ranked by:
1. Size (number of concepts)
2. Influence (betweenness centrality of top nodes)
3. Interconnectedness (cross-cluster edges)
```

### Comparative Analysis Prompt
```
Compare these texts using both overlap_between_texts and difference_between_texts:
1. First, find what they share (common ground)
2. Then, find what text 1 is missing relative to the others
3. Synthesize: map the gaps in shared context as innovation space
```

### Research Questions Prompt
```
Use generate_research_questions on the following text/topic.
Present questions organized by:
- Which gap they bridge
- Potential impact if answered
- Feasibility of investigation
```

### Develop Text Prompt
```
Use develop_text_tool for comprehensive analysis of the following text:
Phase 1: Content gaps — what's structurally missing?
Phase 2: Latent topics — what's underdeveloped but present?
Phase 3: Conceptual bridges — how does this connect to broader discourse?
Synthesize all three phases into actionable development recommendations.
```

### Memory Save Prompt
```
Save the following content to memory using memory_add_relations.
Graph name: {name} (max 28 chars, lowercase, dashes for spaces)
Format entities as [[wikilinks]] and separate statements with newlines.
```

## Chat Prompts

### RAG Chat Prompt (from Obsidian Plugin)

#### User Message Construction
```
{userQuestion}
{optional subPromptPrefix}
<--- answer the question above considering the context & previous conversation we had below --->
{JSON.stringify(statementsWithIds)}
{JSON.stringify(chatHistory)}
each response you provide should be followed with the separator |||| and the ids of the
context statements above where you got the information from in square brackets
```

#### Sub-Prompt Prefixes
These can be prepended to the user's question for directive control:
```
"elaborate on this statement:"
"challenge this idea:"
"generate an interesting question:"
"summarize it:"
"check if it's true:"
```

#### Response Parsing
```
responseText.split("||||")
-> [0]: AI response text
-> [1]: Reference IDs like "[2][7][15]"

Reference format: [n] where n is the statement ID from the context array
Clicking [n] reveals the source statement for verification
```

### AI Topic Naming Prompt (from Obsidian Plugin)

#### Construction
```
promptContext:
  [cluster {community}]: {topStatementContent}
  [cluster {community2}]: {topStatementContent2}

prompt (per cluster):
  { text: "concept1, concept2, concept3", id: clusterId, community: communityId }
```

#### Purpose
Generate short, human-readable names for topical clusters identified by graph analysis.

### Cognitive Variability Chat Patterns

#### Invisible Transition Prompts
| Transition | Natural Prompt |
|-----------|---------------|
| BIASED -> FOCUSED | "How do you see these ideas connecting to the bigger picture?" |
| FOCUSED -> DIVERSIFIED | "What perspectives might we be missing here?" |
| DIVERSIFIED -> FOCUSED | "Which of these threads resonates most with your goal?" |
| DISPERSED -> BIASED | "What's the one idea here that feels most alive to you?" |

#### Playfulness Prompts (Dispersed -> Biased)
```
"If you had to bet everything on one of these scattered ideas, which would it be?"
"Which of these is the weirdest? Let's start there."
"Pick the one that makes you slightly uncomfortable -- that's usually the good one."
```

#### Critical Perspective Prompts
```
"What assumption is this whole line of thinking resting on?"
"If someone from a completely different field read this, what would surprise them?"
"What are we NOT talking about that might matter more?"
```

### Contextual DOT Graph for Chat

#### Per-Cluster Format
```dot
[cluster {id}: {aiName}]
concept1 -- concept2
concept2 -- concept3
concept3 -- concept4
inter-cluster: concept2 -- concept_from_other_cluster
```

#### Filtered by Selection
When user selects specific nodes/topics, filter DOT graph to show only:
1. Lines where ALL selected nodes appear
2. Lines where at least one connected node appears
3. Inter-cluster connector lines for selected clusters

## Ontology Prompts

### Topic-Based Ontology Prompt
```
Generate a comprehensive ontological knowledge graph for the domain: {topic}

Requirements:
- Use [[wikilinks]] syntax: [[Entity1]] relation [[Entity2]] [relationCode]
- Cover ALL relation types: [isA] [partOf] [hasAttribute] [relatedTo] [dependentOn]
  [causes] [locatedIn] [occursAt] [derivedFrom] [opposes]
- Minimum 8 statements per relation type
- Generate a NETWORK, not a tree -- avoid hub-and-spoke patterns
- Distribute entities across multiple relationships
- Include cross-domain connections
- Output ONLY the ontology in a code block -- no explanations
```

### Text-Based Extraction Prompt
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

### Ontology Quality Check Prompt
```
Analyze this ontology for structural quality:

1. Hub detection: Does any entity appear in >25% of statements?
2. Cluster balance: Are there multiple distinct topic clusters?
3. Cross-cluster edges: Do clusters connect to each other?
4. Relation diversity: Are all 10 relation codes represented?
5. Modularity: Is the network neither too uniform nor too fragmented?

Suggest specific improvements if issues are found.
```

### Ontology Expansion Prompt
```
Given the existing ontology below, expand it by:
1. Identifying underrepresented relation types
2. Finding entities that lack sufficient connections
3. Adding cross-domain bridges between isolated clusters
4. Introducing opposing concepts ([opposes]) where only agreement exists
5. Adding temporal ([occursAt]) and spatial ([locatedIn]) grounding

Maintain the same [[wikilinks]] + [relationCode] format.
```

### Ontology-to-Memory Save Prompt
```
Save this ontology to InfraNodus memory:
- Graph name: {sanitized_topic_name} (max 28 chars, lowercase, dashes)
- Use memory_add_relations with the full ontology text
- Verify save by retrieving with memory_get_relations
```
