# Comparative Analysis Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`
> **Dependents**: `modules/critical-perspective`, `modules/seo-analysis`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#comparison` `#overlap` `#difference` `#symbolic`

## Tools in this Module

### 1. overlap_between_texts
**Purpose**: Find similarities and shared concepts across 2+ texts or URLs.
**Endpoint**: `/graphsAndStatements` (read-only, idempotent)
**When to use**: When comparing perspectives on the same topic, finding common ground between sources, or checking content alignment across documents.

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `texts[]` | yes | Array of { text?, url? } objects (minimum 2) |
| `includeStatements` | no | Return individual statements |
| `includeGraph` | no | Return raw graph structure |

**Returns**: `KnowledgeGraphOutput` showing shared topical structure across all texts

**Use cases**:
- Compare two articles to find consensus
- Merge team members' notes to find alignment
- Validate coverage consistency across documents
- SEO: Compare content with competitor content

### 2. difference_between_texts
**Purpose**: Find what exists in texts 2..N but is MISSING from text 1.
**Endpoint**: `/graphsAndStatements` (read-only, idempotent)
**When to use**: When identifying blind spots, finding what competitors cover that you don't, or discovering gaps between perspectives.

**Parameters**: Same as overlap_between_texts

**Returns**: `KnowledgeGraphOutput` showing topics/concepts present in comparison texts but absent from the primary text

**Directionality**: Text 1 is the reference — results show what text 1 is MISSING relative to other texts.

**Use cases**:
- Find content gaps vs competitors
- Identify blind spots in your analysis
- Compare draft vs reference material
- Discover what alternative perspectives bring

## Combined Workflow
The most powerful comparative analysis combines both tools:
```
Step 1: overlap_between_texts → What do they share? (common ground)
Step 2: difference_between_texts → What's missing? (blind spots)
Step 3: Synthesize → Map gaps in shared context (innovation space)
```

## Skill Integration
- **Critical Perspective**: Uses difference to identify unexamined perspectives
- **SEO Analysis**: Uses overlap/difference for competitor analysis
- **Cognitive Variability**: Compare BIASED (narrow) text against DIVERSIFIED (broad) text to identify narrowing patterns

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md`
- **Consumed by**: `→ modules/critical-perspective.md` `→ modules/seo-analysis.md`
- **Bridged via**: `→ bridges/skill-tool-map.md`
