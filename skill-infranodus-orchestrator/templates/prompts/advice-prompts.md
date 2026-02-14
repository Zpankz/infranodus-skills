# AI Advice Prompt Templates

> **Layer**: 5 | **Dependencies**: `core/api-reference.md`, `modules/research-engine`
> **Tags**: `#template` `#prompts` `#advice` `#ai`

## Question Generation Prompt (from Obsidian)
```
Generate a question that uses the current context and the graph structure below:
{dotGraph}

Context statements:
{statements}
```

## Idea Development Prompt (from Obsidian)
```
Generate an idea that uses the current context and the graph structure below:
{dotGraph}

Context statements:
{statements}
```

## Summary Prompt (from Obsidian)
```
Summarize the content using the current context and the graph structure below:
{dotGraph}

Context statements:
{statements}
```

## Context Retrieval Prompt (from Obsidian)
```
Retrieve the most relevant content from the current context that relates
to the graph structure below:
{dotGraph}
```

## Gap Bridging Prompt (from Obsidian)
```
Find the gap in the current context that would bridge the graph structure below:
{dotGraph}
```

## Graph-Augmented Response Prompt (from VSCode)
```
Use the following knowledge graph data to make your response more precise:
{dotGraphByCluster}
```

## GraphRAG Retrieval Prompt
```
Using the knowledge stored in graph "{graphName}", answer the following question:
{userQuery}

Ground your response in the retrieved statements. Cite specific statements
where relevant. If the graph doesn't contain sufficient information, say so.
```

## Expert Response Prompt
```
Based on the knowledge graph "{graphName}", generate an expert response to:
{userQuery}

Draw on the graph's topical clusters, key relationships, and conceptual
gateways to provide a comprehensive, well-structured answer.
```

## Prompt Construction Guidelines (from Obsidian Plugin)
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
