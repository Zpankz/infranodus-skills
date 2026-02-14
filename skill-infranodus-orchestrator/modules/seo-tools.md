# SEO & Search Analytics Tools

> **Layer**: 2 | **Dependencies**: `core/types.md`, `core/api-reference.md`
> **Dependents**: `modules/seo-analysis`, `bridges/skill-tool-map`
> **Tags**: `#tools` `#seo` `#google` `#search` `#symbolic`

## Tools in this Module

### 1. analyze_google_search_results
**Purpose**: Build knowledge graph from keywords found in Google search results (informational supply).
**Endpoint**: `/import/googleSearchResultsGraph`
**When to use**: When mapping what content currently ranks for a topic — understanding the existing information landscape.

**Parameters**:
| Param | Required | Default | Description |
|-------|----------|---------|-------------|
| `searchQuery` | yes | — | Keywords to search |
| `importLanguage` | no | "EN" | Language code |
| `importCountry` | no | "US" | Country code for localization |

**Returns**: `KnowledgeGraphOutput` of keywords/concepts found in top search results

**Insight**: This maps the SUPPLY side — what information exists about a topic.

### 2. analyze_related_search_queries
**Purpose**: Build graph of related search queries and suggestions (search demand).
**Endpoint**: `/import/googleSearchQueriesGraph`
**When to use**: When understanding what people actually search for — the demand side of information.

**Parameters**: Same as above

**Returns**: `KnowledgeGraphOutput` of related queries, autocomplete suggestions, AdWords data

**Insight**: This maps the DEMAND side — what people want to know.

### 3. search_queries_vs_search_results
**Purpose**: Find supply-demand gaps — keywords people search for but don't find in results.
**Endpoint**: `/import/googleSearchVsIntentGraph`
**When to use**: After running both supply and demand analysis. This reveals the highest-value content opportunities.

**Parameters**: Same as above

**Returns**: Gap analysis between search demand and informational supply

**Insight**: These gaps represent unmet search intent — content that would serve real user needs.

### 4. generate_seo_report
**Purpose**: Comprehensive SEO audit comparing content against the search landscape.
**Endpoint**: Multiple endpoints (6-step pipeline with progress reporting)
**When to use**: For full content SEO optimization. Most comprehensive SEO tool — combines supply, demand, and gap analysis with the user's actual content.

**6-Step Pipeline**:
```
Step 1 (5%):  Extract content from URL/text
Step 2 (15%): Generate knowledge graph of content
Step 3 (30%): Analyze Google search results (supply)
Step 4 (50%): Analyze related search queries (demand)
Step 5 (70%): Compare content vs search results
Step 6 (90%): Compare queries vs results (gaps)
Final (100%): Synthesize comprehensive report
```

**Parameters**:
| Param | Required | Description |
|-------|----------|-------------|
| `text` / `url` | yes | Content to audit |
| `contentToExtract` | no | "all", "headerTags", "linkTags" |
| `importLanguage` | no | Language for search |
| `importCountry` | no | Country for search |
| `useProxy` | no | Proxy for URL extraction |

**Returns**: Combined analysis with:
- Content topical structure
- Search result landscape
- Search demand patterns
- Content vs results gaps
- Query vs results gaps

## Supply-Demand-Gap Framework
```
SUPPLY (what exists)          → analyze_google_search_results
DEMAND (what people want)     → analyze_related_search_queries
GAP   (unmet need)            → search_queries_vs_search_results
AUDIT (content vs landscape)  → generate_seo_report
```

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md`
- **Consumed by**: `→ modules/seo-analysis.md`
- **Bridged via**: `→ bridges/skill-tool-map.md`
