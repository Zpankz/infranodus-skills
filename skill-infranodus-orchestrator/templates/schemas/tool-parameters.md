# Tool Parameter Quick Reference

> **Layer**: 5 | **Dependencies**: `core/api-reference.md`, `modules/*`
> **Tags**: `#template` `#schema` `#reference` `#quick-ref`

## Tool Parameter Matrix

### Graph Generation Tools

| Tool | text | url | name | includeStatements | includeGraph | modifyAnalyzedText | modelToUse |
|------|------|-----|------|-------------------|-------------|-------------------|------------|
| generate_knowledge_graph | opt* | opt* | — | opt | opt | opt | opt |
| create_knowledge_graph | opt* | opt* | **req** | opt | opt | opt | opt |
| analyze_existing_graph_by_name | — | — | **req** | opt | opt | — | opt |
| generate_contextual_hint | opt* | opt* | — | — | — | — | — |
| retrieve_from_knowledge_base | — | — | **req** | — | — | — | opt |

*At least one of text/url required

### Content Analysis Tools

| Tool | text | url | gapDepth | useSeveralGaps | modelToUse |
|------|------|-----|----------|---------------|------------|
| generate_content_gaps | opt* | opt* | opt | opt | opt |
| generate_topical_clusters | opt* | opt* | — | — | opt |
| develop_text_tool | opt* | opt* | opt | opt | opt |

### Research Tools

| Tool | text | url | name | prompt | optimize | requestMode |
|------|------|-----|------|--------|----------|-------------|
| generate_research_questions | opt* | opt* | — | — | gap | question |
| generate_research_ideas | opt* | opt* | — | — | gap | — |
| research_questions_from_graph | — | — | **req** | — | gap | question |
| develop_latent_topics | opt* | opt* | — | — | latent | — |
| develop_conceptual_bridges | opt* | opt* | — | — | imagine | — |
| generate_responses_from_graph | — | — | **req** | opt | — | — |

### Comparative Tools

| Tool | texts[] | includeStatements | includeGraph |
|------|---------|-------------------|-------------|
| overlap_between_texts | **req** (min 2) | opt | opt |
| difference_between_texts | **req** (min 2) | opt | opt |

### SEO Tools

| Tool | text | url | searchQuery | importLanguage | importCountry | contentToExtract | useProxy |
|------|------|-----|-------------|---------------|--------------|-----------------|---------|
| analyze_google_search_results | — | — | **req** | opt | opt | — | — |
| analyze_related_search_queries | — | — | **req** | opt | opt | — | — |
| search_queries_vs_search_results | — | — | **req** | opt | opt | — | — |
| generate_seo_report | opt* | opt* | — | opt | opt | opt | opt |

### Memory Tools

| Tool | graphName | text | query | includeStatements | modifyAnalyzedText |
|------|-----------|------|-------|-------------------|-------------------|
| memory_add_relations | **req** | **req** | — | opt | opt |
| memory_get_relations | opt | — | **req** | opt | — |

### Search Tools

| Tool | query | id | contextNames | contextTypes | type | language | favorite |
|------|-------|----|-------------|-------------|------|----------|---------|
| list_graphs | opt | — | — | — | opt | opt | opt |
| search | **req** | — | opt | opt | — | — | — |
| fetch | — | **req** | — | — | — | — | — |

## Legend
- **req**: Required parameter
- **opt**: Optional parameter
- **opt***: Optional but at least one of the starred group is required
- **—**: Not applicable to this tool
