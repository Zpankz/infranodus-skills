# Workflow Pipelines
Deps: core/api-reference.md, core/types.md
Used-by: SKILL.md, bridges/workflow-orchestrator.md

---

## Knowledge Graph Pipeline

### Ontology Creation

**Stage 1: Generate Ontology**
```
Input: topic or text
Process:
  1. Extract entities and concepts
  2. Infer relationships between entities
  3. Classify each relation with [relationCode]
  4. Validate network topology (not tree)
Output: Wikilink-formatted ontology statements
```

**Stage 2: Quality Validation**
```
Tool: generate_knowledge_graph
Input: { text: ontology_output }
Check:
  - Modularity 0.3-0.6 (not too uniform, not too fragmented)
  - No single entity in >25% of statements (hub avoidance)
  - Cross-cluster edges present (conceptual gateways)
  - All 10 relation codes represented
  - Diversity statistics healthy
```

**Stage 3: Iterative Refinement**
```
If quality check fails:
  1. Identify over-represented entities -> redistribute
  2. Identify missing relation types -> add
  3. Identify disconnected clusters -> add bridges
  4. Regenerate and re-check
Repeat until topology is healthy (typically 1-2 iterations)
```

**Stage 4: Persistence**
```
Option A: Save as graph
  Tool: create_knowledge_graph
  Input: { name: "ontology-name", text: ontology_output }

Option B: Save as memory
  Tool: memory_add_relations
  Input: { graphName: "ontology-name", text: ontology_output }

Option C: Output for external use
  Format: code block for direct paste into InfraNodus.com
```

### GraphRAG Chatbot

**Stage 1: Knowledge Base Setup**
```
1. Create persistent graph from source material
   Tool: create_knowledge_graph
   Input: { name: "knowledge-base", text/url: source_material }

2. Optionally add multiple sources to same graph
   Tool: memory_add_relations (repeated)
```

**Stage 2: Query Processing**
```
1. User asks a question
2. Retrieve relevant context
   Tool: retrieve_from_knowledge_base
   Input: { name: "knowledge-base", prompt: user_question }
3. Get: retrieved statements with similarity scores
```

**Stage 3: Response Generation**
```
1. Construct response using retrieved statements as context
2. Cite specific statements where relevant
3. Identify gaps in knowledge base for the query
```

### Multi-Source Knowledge Integration

```
Google Drive / Document uploads:
  -> Extract text content
  -> Generate knowledge graph per document
  -> Merge into unified knowledge base
  -> Enable cross-document retrieval

Email / message threads:
  -> Extract content
  -> Generate knowledge graph of threads
  -> Label/categorize based on topical clusters
  -> Enable knowledge retrieval
```

---

## Text Analysis Pipeline

End-to-end text analysis from raw input to actionable insights.

**Stage 1: Input Resolution**
```
Input: text | url | file
  +-- If URL -> extract via /convert/url -> validate text quality
  +-- If file -> read content -> clean markdown/code
  +-- If text -> use directly
Output: clean text string
```

**Stage 2: Knowledge Graph Generation**
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

**Stage 3: Gap Analysis**
```
Tool: generate_content_gaps
Input: same text
Output: contentGaps[]
  - Each gap = space between clusters
  - Ranked by significance (weight)
```

**Stage 4: Research Questions**
```
Tool: generate_research_questions
Input: same text
Output: questions[]
  - Each question bridges a specific gap
  - Actionable direction for development
```

**Stage 5: Latent Topic Discovery**
```
Tool: develop_latent_topics
Input: same text
Output: { ideas, mainTopics, latentTopicsToDevelop }
  - Underdeveloped themes with expansion potential
```

**Stage 6: Conceptual Bridging**
```
Tool: develop_conceptual_bridges
Input: same text
Output: { ideas, latentConceptsToDevelop, latentConceptsRelations }
  - Cross-domain connections
  - Hidden patterns linking to broader discourse
```

**Stage 7: Synthesis**
```
Combine all outputs:
1. Overview (from graphSummary)
2. Topical structure (from clusters)
3. Gaps and opportunities (from gaps)
4. Development directions (from questions + latent topics)
5. Cross-domain connections (from conceptual bridges)
6. Recommendations (synthesized from all)
```

### Shortcut: develop_text_tool

For the comprehensive pipeline in a single tool call:
```
Tool: develop_text_tool
Input: { text }
Output: Combined gaps + latent topics + conceptual bridges (3 sequential API calls)
```
Use when you need all stages but want efficiency over granular control.

---

## Content Comparison Pipeline

### Two-Text Comparison

**Stage 1: Find Overlap**
```
Tool: overlap_between_texts
Input: { texts: [{ text/url: text1 }, { text/url: text2 }] }
Output: Shared topical structure -- concepts and relations present in both
Insight: Common ground, agreement, shared foundations
```

**Stage 2: Find Differences (A vs B)**
```
Tool: difference_between_texts
Input: { texts: [{ text/url: text1 }, { text/url: text2 }] }
Output: What text2 has that text1 is missing
Insight: Blind spots in text1, unique contributions of text2
```

**Stage 3: Find Differences (B vs A)**
```
Tool: difference_between_texts
Input: { texts: [{ text/url: text2 }, { text/url: text1 }] }
Output: What text1 has that text2 is missing
Insight: Unique contributions of text1, blind spots in text2
```

**Stage 4: Synthesize**
```
1. Shared foundation: What both agree on
2. Text 1 unique: What only text 1 contributes
3. Text 2 unique: What only text 2 contributes
4. Gap in overlap: Topics related to shared ground but not covered by either
5. Innovation space: Where combining unique contributions could create new insight
```

### Multi-Text Comparison

```
For N texts:
1. overlap_between_texts(all N texts) -> Universal common ground
2. For each text i:
   difference_between_texts([text_i, text_1, ..., text_N]) -> What text_i is missing
3. Synthesize:
   - Consensus (all agree)
   - Diversity (unique per source)
   - Gaps (no source covers)
```

### Competitor Content Analysis

**Stage 1: Map Your Content**
```
Tool: generate_knowledge_graph
Input: your content URL
Output: Your topical structure
```

**Stage 2: Compare with Competitors**
```
Tool: overlap_between_texts
Input: [your_url, competitor1_url, competitor2_url]
Output: What you share (competitive table stakes)

Tool: difference_between_texts
Input: [your_url, competitor1_url, competitor2_url]
Output: What competitors cover that you don't (your gaps)
```

**Stage 3: Prioritize Gaps**
```
From difference output:
1. Filter gaps by relevance to your audience
2. Cross-reference with search demand (analyze_related_search_queries)
3. Rank by: relevance x search volume x difficulty
4. Generate content development plan
```

### Use Cases

| Scenario | Pipeline | Key Output |
|----------|----------|------------|
| Comparing research papers | Two-text | Shared findings + unique contributions |
| Competitive analysis | Multi-text | Your gaps vs competitors |
| Draft vs reference | Two-text | What your draft is missing |
| Team alignment | Multi-text | Consensus + divergent views |
| Literature review | Multi-text | Coverage map + research gaps |
| Perspective integration | Two-text | How to synthesize viewpoints |

---

## SEO Pipeline

### Topic-Based SEO

**Stage 1: Map Informational Supply**
```
Tool: analyze_google_search_results
Input: { searchQuery: "keyword1 keyword2", importLanguage: "EN", importCountry: "US" }
Repeat: 3-5 keyword combinations for comprehensive coverage
Output: Topical clusters in existing search results
Insight: What content already exists (supply)
```

**Stage 2: Map Search Demand**
```
Tool: analyze_related_search_queries
Input: { searchQuery: same keywords }
Output: Related search queries, autocomplete suggestions
Insight: What people actually search for (demand)
```

**Stage 3: Find Supply-Demand Gaps**
```
Tool: search_queries_vs_search_results
Input: { searchQuery: same keywords }
Output: Keywords with high search volume but low result quality
Insight: Unmet search intent = highest-value content opportunities
```

**Stage 4: Synthesize Recommendations**
```
From the three analyses above, derive:
1. Priority keywords: high demand + low supply
2. Content topics: fill identified gaps
3. Semantic relations: build topical authority
4. Quick wins: low competition, immediate opportunity
5. Long-term plays: high competition, high reward
```

### Content-Based SEO

**Stage 1: Full SEO Report**
```
Tool: generate_seo_report
Input: { url: "https://...", importLanguage: "EN", importCountry: "US" }
Progress: 6 checkpoints (5% -> 15% -> 30% -> 50% -> 70% -> 100%)
Output: Combined analysis of content vs search landscape
```

**Stage 2: Competitor Analysis (Optional)**

Use the Competitor Content Analysis from the Content Comparison Pipeline above
with `overlap_between_texts` and `difference_between_texts` on your URL vs competitor URLs.

**Stage 3: Structural Recommendations**
```
From analysis, recommend:
1. HTML structure alignment (headers mapping to topic clusters)
2. Missing keywords to integrate
3. Content sections to add (from gaps)
4. Internal linking opportunities (from conceptual gateways)
5. Schema.org markup opportunities
```

### SEO Report Template
```
## Executive Summary
[1-2 sentences on overall content SEO health]

## Informational Supply
[What currently ranks -- key clusters and authority sources]

## Search Demand
[What people search for -- high-volume terms and patterns]

## Supply-Demand Gaps
[Unmet intent -- keywords with demand but weak supply]

## Recommendations
### Quick Wins (Low effort, immediate impact)
- [Specific keyword/topic actions]

### Strategic Plays (Higher effort, sustained impact)
- [Content development recommendations]

## Next Steps
[Actionable implementation guidance]
```
