# Text Analysis Pipeline — Workflow Template

> **Layer**: 5 | **Dependencies**: `modules/graph-generation`, `modules/content-analysis`, `modules/research-engine`
> **Tags**: `#template` `#workflow` `#pipeline` `#text-analysis`

## Overview
End-to-end text analysis pipeline from raw input to actionable insights. Derived from n8n workflow patterns and MCP tool chains.

## Pipeline Stages

### Stage 1: Input Resolution
```
Input: text | url | file
  ├── If URL → extract via /convert/url → validate text quality
  ├── If file → read content → clean markdown/code
  └── If text → use directly
Output: clean text string
```

### Stage 2: Knowledge Graph Generation
```
Tool: generate_knowledge_graph
Input: { text, includeStatements: true, modifyAnalyzedText: "detectEntities" }
Output: KnowledgeGraphOutput
  - statistics (modularity, clusters, nodes, edges)
  - graphSummary (AI overview)
  - contentGaps (structural holes)
  - mainTopicalClusters (topic groups)
  - topInfluentialNodes (gateway concepts)
```

### Stage 3: Gap Analysis
```
Tool: generate_content_gaps
Input: same text
Output: contentGaps[]
  - Each gap = space between clusters
  - Ranked by significance (weight)
```

### Stage 4: Research Questions
```
Tool: generate_research_questions
Input: same text
Output: questions[]
  - Each question bridges a specific gap
  - Actionable direction for development
```

### Stage 5: Latent Topic Discovery
```
Tool: develop_latent_topics
Input: same text
Output: { ideas, mainTopics, latentTopicsToDevelop }
  - Underdeveloped themes with expansion potential
```

### Stage 6: Conceptual Bridging
```
Tool: develop_conceptual_bridges
Input: same text
Output: { ideas, latentConceptsToDevelop, latentConceptsRelations }
  - Cross-domain connections
  - Hidden patterns linking to broader discourse
```

### Stage 7: Synthesis
```
Combine all outputs:
1. Overview (from graphSummary)
2. Topical structure (from clusters)
3. Gaps and opportunities (from gaps)
4. Development directions (from questions + latent topics)
5. Cross-domain connections (from conceptual bridges)
6. Recommendations (synthesized from all)
```

## n8n Equivalent
```
Webhook/Trigger → InfraNodus (graphAndStatements) → InfraNodus (gaps)
  → InfraNodus (questions) → InfraNodus (latent topics)
  → AI Summarizer → Output
```

## Shortcut: develop_text_tool
For the comprehensive pipeline in a single tool call:
```
Tool: develop_text_tool
Input: { text }
Output: Combined gaps + latent topics + conceptual bridges (3 sequential API calls)
```
Use this when you need all stages but want efficiency over granular control.
