# Content Comparison Pipeline — Workflow Template

> **Layer**: 5 | **Dependencies**: `modules/comparative-analysis`, `modules/content-analysis`
> **Tags**: `#template` `#workflow` `#pipeline` `#comparison`

## Two-Text Comparison Pipeline

### Stage 1: Find Overlap
```
Tool: overlap_between_texts
Input: { texts: [{ text/url: text1 }, { text/url: text2 }] }
Output: Shared topical structure — concepts and relations present in both
Insight: Common ground, agreement, shared foundations
```

### Stage 2: Find Differences
```
Tool: difference_between_texts
Input: { texts: [{ text/url: text1 }, { text/url: text2 }] }
Output: What text2 has that text1 is missing
Insight: Blind spots in text1, unique contributions of text2
```

### Stage 3: Reverse Difference
```
Tool: difference_between_texts
Input: { texts: [{ text/url: text2 }, { text/url: text1 }] }
Output: What text1 has that text2 is missing
Insight: Unique contributions of text1, blind spots in text2
```

### Stage 4: Synthesize
```
1. Shared foundation: What both agree on
2. Text 1 unique: What only text 1 contributes
3. Text 2 unique: What only text 2 contributes
4. Gap in overlap: Topics related to shared ground but not covered by either
5. Innovation space: Where combining unique contributions could create new insight
```

## Multi-Text Comparison Pipeline

### For N texts:
```
1. overlap_between_texts(all N texts) → Universal common ground
2. For each text i:
   difference_between_texts([text_i, text_1, ..., text_N]) → What text_i is missing
3. Synthesize:
   - Consensus (all agree)
   - Diversity (unique per source)
   - Gaps (no source covers)
```

## Competitor Content Analysis Pipeline

### Stage 1: Map Your Content
```
Tool: generate_knowledge_graph
Input: your content URL
Output: Your topical structure
```

### Stage 2: Compare with Competitors
```
Tool: overlap_between_texts
Input: [your_url, competitor1_url, competitor2_url]
Output: What you share (competitive table stakes)

Tool: difference_between_texts
Input: [your_url, competitor1_url, competitor2_url]
Output: What competitors cover that you don't (your gaps)
```

### Stage 3: Prioritize Gaps
```
From difference output:
1. Filter gaps by relevance to your audience
2. Cross-reference with search demand (analyze_related_search_queries)
3. Rank by: relevance × search volume × difficulty
4. Generate content development plan
```

## Use Cases by Scenario

| Scenario | Pipeline | Key Output |
|----------|----------|------------|
| Comparing research papers | Two-text | Shared findings + unique contributions |
| Competitive analysis | Multi-text | Your gaps vs competitors |
| Draft vs reference | Two-text | What your draft is missing |
| Team alignment | Multi-text | Consensus + divergent views |
| Literature review | Multi-text | Coverage map + research gaps |
| Perspective integration | Two-text | How to synthesize viewpoints |

## n8n Equivalent
```
Input URLs (batch)
  → InfraNodus (overlap)
  → InfraNodus (difference)
  → AI Synthesizer
  → Report Output
```
