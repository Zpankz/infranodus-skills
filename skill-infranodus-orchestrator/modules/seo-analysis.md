# SEO Analysis Module

> **Layer**: 3 | **Dependencies**: `core/types.md`, `modules/seo-tools`, `modules/content-analysis`, `modules/comparative-analysis`, `modules/graph-generation`
> **Dependents**: `bridges/skill-tool-map`, `bridges/workflow-orchestrator`
> **Tags**: `#skill` `#seo` `#content-optimization` `#search` `#neural`

## Activation Trigger
Comprehensive SEO analysis for content optimization. Use when the user asks to perform SEO analysis, keyword research, content gap analysis, search intent analysis, or wants to optimize content for search engines. Covers topic-based keyword research (informational supply and search demand), website/document analysis, and actionable SEO recommendations.

## Decision Tree
```
User request →
  ├── No input specified → Ask for topic, document, or URL
  ├── Topic provided → Topic Analysis Workflow
  └── Document/URL provided → Content Analysis Workflow
```

## Topic Analysis Workflow

### Step 1: Analyze Informational Supply
**Tool**: `analyze_google_search_results` (3–5 keyword combinations)
**Present**: Topical clusters (authority pillars), key relations (semantic relevance), content gaps (opportunity spaces)

### Step 2: Analyze Search Demand
**Tool**: `analyze_related_search_queries`
**Present**: High-volume keywords, low-competition opportunities, search intent patterns, topical clusters in search behavior

### Step 3: Identify Supply-Demand Gaps
**Tool**: `search_queries_vs_search_results`
**Present**: Keywords people search for but don't find in results, high-volume/weak-supply queries, emerging topics with growing demand

### Step 4: Deliver Recommendations
- Priority keywords (high volume + low competition)
- Content topics that fill identified gaps
- Semantic relations to build authority
- Quick wins vs long-term strategy

### Step 5: Ask for Content Example
- Prompt user for URL or content to optimize
- Offer writing-assistant integration for content creation
- **Handoff**: → `modules/writing-assistant.md` for SEO-aware content refinement

### Step 6: Structural Semantic Optimization
- HTML structure alignment with topical clusters
- Meta-data recommendations (title, description, OG tags)
- Header hierarchy mapping (H1–H6 aligned with topic importance)
- Structured markup (Schema.org, JSON-LD) recommendations

## Content Analysis Workflow

### Step 1: Extract Content
- URL: Crawl via API with optional `contentToExtract` modes
- File: Direct text extraction

### Step 2: Run SEO Report
**Tool**: `generate_seo_report` (comprehensive 6-step pipeline)
**Fallback**: If report unavailable, run Topic Analysis Workflow manually with content as anchor

### Step 3: Structural Semantic Optimization
Same as Topic Analysis Step 6

### Step 4: Deliver Report
```
## Executive Summary
[1-2 paragraph overview of content SEO health]

## Current State
[Content coverage strengths, existing topical authority]

## Opportunities
[Missing keywords, content gaps, unmet search intent]

## Recommendations
[Prioritized action items ranked by impact/effort]

## Next Steps
[Specific implementation guidance]
```

## Competitor Analysis Extension
Using comparative analysis tools:
```
1. overlap_between_texts → What does competitor cover that you also cover? (shared ground)
2. difference_between_texts → What does competitor cover that you DON'T? (your gaps)
3. Synthesize → Priority gaps to fill for competitive advantage
```

## InfraNodus Tool Summary
| Tool | Phase | Maps To |
|------|-------|---------|
| `analyze_google_search_results` | Supply analysis | What exists |
| `analyze_related_search_queries` | Demand analysis | What people want |
| `search_queries_vs_search_results` | Gap analysis | Unmet need |
| `generate_seo_report` | Full audit | Complete picture |
| `overlap_between_texts` | Competitor overlap | Shared ground |
| `difference_between_texts` | Competitor gaps | Your blind spots |

## Port Connections
- **Depends on**: `← core/types.md` `← modules/seo-tools` `← modules/content-analysis` `← modules/comparative-analysis` `← modules/graph-generation`
- **Hands off to**: `→ modules/writing-assistant.md` (for content creation/refinement)
- **Orchestrated by**: `← bridges/workflow-orchestrator.md`
