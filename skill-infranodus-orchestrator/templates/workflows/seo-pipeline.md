# SEO Analysis Pipeline — Workflow Template

> **Layer**: 5 | **Dependencies**: `modules/seo-tools`, `modules/seo-analysis`, `modules/content-analysis`, `modules/comparative-analysis`
> **Tags**: `#template` `#workflow` `#pipeline` `#seo`

## Topic-Based SEO Pipeline

### Stage 1: Map Informational Supply
```
Tool: analyze_google_search_results
Input: { searchQuery: "keyword1 keyword2", importLanguage: "EN", importCountry: "US" }
Repeat: 3-5 keyword combinations for comprehensive coverage
Output: Topical clusters in existing search results
Insight: What content already exists (supply)
```

### Stage 2: Map Search Demand
```
Tool: analyze_related_search_queries
Input: { searchQuery: same keywords }
Output: Related search queries, autocomplete suggestions
Insight: What people actually search for (demand)
```

### Stage 3: Find Supply-Demand Gaps
```
Tool: search_queries_vs_search_results
Input: { searchQuery: same keywords }
Output: Keywords with high search volume but low result quality
Insight: Unmet search intent = highest-value content opportunities
```

### Stage 4: Synthesize Recommendations
```
From the three analyses above, derive:
1. Priority keywords: high demand + low supply
2. Content topics: fill identified gaps
3. Semantic relations: build topical authority
4. Quick wins: low competition, immediate opportunity
5. Long-term plays: high competition, high reward
```

## Content-Based SEO Pipeline

### Stage 1: Full SEO Report
```
Tool: generate_seo_report
Input: { url: "https://...", importLanguage: "EN", importCountry: "US" }
Progress: 6 checkpoints (5% → 15% → 30% → 50% → 70% → 100%)
Output: Combined analysis of content vs search landscape
```

### Stage 2: Competitor Analysis (Optional)
```
Tool: overlap_between_texts
Input: { texts: [{ url: "your-content" }, { url: "competitor-1" }, { url: "competitor-2" }] }
Output: What you and competitors share

Tool: difference_between_texts
Input: { texts: [{ url: "your-content" }, { url: "competitor-1" }, { url: "competitor-2" }] }
Output: What competitors cover that you don't
```

### Stage 3: Structural Recommendations
```
From analysis, recommend:
1. HTML structure alignment (headers mapping to topic clusters)
2. Missing keywords to integrate
3. Content sections to add (from gaps)
4. Internal linking opportunities (from conceptual gateways)
5. Schema.org markup opportunities
```

## n8n Equivalent
```
Trigger → InfraNodus (google search results graph)
       → InfraNodus (google search queries graph)
       → InfraNodus (search vs intent graph)
       → AI Synthesizer → Report Output
```

## Report Template
```markdown
## Executive Summary
[1-2 sentences on overall content SEO health]

## Informational Supply
[What currently ranks — key clusters and authority sources]

## Search Demand
[What people search for — high-volume terms and patterns]

## Supply-Demand Gaps
[Unmet intent — keywords with demand but weak supply]

## Recommendations
### Quick Wins (Low effort, immediate impact)
- [Specific keyword/topic actions]

### Strategic Plays (Higher effort, sustained impact)
- [Content development recommendations]

## Next Steps
[Actionable implementation guidance]
```
