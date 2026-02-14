# Content Analysis Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`, `core/graph-analytics.md`, `core/text-processing.md`
> **Dependents**: `modules/writing-assistant`, `modules/critical-perspective`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#analysis` `#gaps` `#clusters` `#neural`

## Tools in this Module

### 1. generate_content_gaps
**Purpose**: Detect missing connections and underexplored topics between discourse clusters.
**Endpoint**: `/graphAndStatements` (read-only, idempotent)
**When to use**: When you detect structural gaps in text, when the user's thinking seems incomplete, or when the Critical Perspective skill identifies blind spots.

**Parameters**: Same as generate_knowledge_graph (text or url)

**Returns**: `{ contentGaps: string[] }` — list of identified gaps between topic clusters

**Cognitive bridge**: Each gap represents creative potential. Gaps between strong clusters = innovation space. Use to identify where the user should explore next.

### 2. generate_topical_clusters
**Purpose**: Extract topic groupings and keyword clusters from text.
**Endpoint**: `/graphAndStatements` (read-only, idempotent)
**When to use**: When you need to understand the thematic structure of content — what topics are covered and how they're grouped.

**Returns**: `{ topicalClusters: string[] }` — named topic groups with constituent concepts

### 3. develop_text_tool
**Purpose**: Comprehensive text development — combines gap analysis + latent topic discovery + conceptual bridging in one operation.
**Endpoint**: `/graphAndAdvice` (3 sequential calls with progress)
**When to use**: This is the "deep analysis" tool. Use when the writing-assistant detects patterns requiring investigation, when content needs strategic development, or for comprehensive text review.

**Process** (3-phase):
```
Phase 1 (0-33%): Content gap analysis → identify structural holes
Phase 2 (33-66%): Latent topic discovery → find underdeveloped themes
Phase 3 (66-100%): Conceptual bridging → connect to broader discourse
```

**Returns**: Combined output with:
- Content gaps with bridging suggestions
- Latent topics with development ideas
- Conceptual bridges to broader contexts

**Priority**: This is the most comprehensive analysis tool. Use when other tools provide insufficient depth.

## Decision Tree
```
Need content analysis?
├── Just gaps → generate_content_gaps
├── Just topics → generate_topical_clusters
└── Deep analysis (gaps + latent + bridges) → develop_text_tool
```

## Skill Integration Points
- **Writing Assistant** → uses gap analysis when detecting missing transitions
- **Critical Perspective** → uses gap analysis when surfacing blind spots
- **Cognitive Variability** → uses topical clusters to map cognitive state
- **SEO Analysis** → uses develop_text_tool for content optimization recommendations

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md` `← core/graph-analytics.md` `← core/text-processing.md`
- **Consumed by**: `→ modules/writing-assistant.md` `→ modules/critical-perspective.md` `→ modules/seo-analysis.md`
- **Bridged via**: `→ bridges/skill-tool-map.md` `→ bridges/pattern-detection-bridge.md`
