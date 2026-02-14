# Skill-Tool Mapping — Hyperedge Registry

> **Layer**: 4 (Bridge) | **Dependencies**: All `modules/*` | **Dependents**: `SKILL.md` (index)
> **Tags**: `#bridge` `#hyperedge` `#mapping` `#registry` `#symbolic`

## Purpose
This bridge file maps every skill module to the InfraNodus MCP tools it uses. It serves as the central registry for skill→tool dependencies, enabling the orchestrator to resolve tool access and prevent redundant invocations.

## Complete Skill → Tool Mapping

### Cognitive Variability
| Tool | Purpose in Skill | When Triggered |
|------|-----------------|----------------|
| `generate_knowledge_graph` | Map discourse structure to cognitive state | State diagnosis |
| `generate_content_gaps` | Show what BIASED thinking excludes | BIASED 3+ intervention |
| `develop_latent_topics` | Surface suppressed themes in FOCUSED | FOCUSED 5+ intervention |
| `generate_research_questions` | Provide direction in DIVERSIFIED | DIVERSIFIED 7+ intervention |

### Critical Perspective
| Tool | Purpose in Skill | When Triggered |
|------|-----------------|----------------|
| `generate_knowledge_graph` | Map topics and relations | Starting analysis |
| `generate_content_gaps` | Find structural blind spots | Assumption surfacing |
| `develop_text_tool` | Comprehensive gap + latent + bridge analysis | Deep review |
| `generate_research_questions` | Questions from gaps | Directing exploration |
| `develop_latent_topics` | Underdeveloped themes | Finding hidden potential |
| `develop_conceptual_bridges` | Connect to broader discourse | Expanding context |
| `overlap_between_texts` | Common ground between perspectives | Comparing viewpoints |
| `difference_between_texts` | Missing content vs other sources | Finding blind spots |

### Writing Assistant
| Tool | Purpose in Skill | When Triggered |
|------|-----------------|----------------|
| `generate_knowledge_graph` | Check topical balance (with includeGraphSummary) | Pattern detection → imbalance |
| `develop_text_tool` | Deep text development | Error clustering detected |
| `generate_seo_report` | External alignment check | Publication-ready content |

### Ontology Creator
| Tool | Purpose in Skill | When Triggered |
|------|-----------------|----------------|
| `create_knowledge_graph` | Save ontology as graph | User wants persistence |
| `generate_knowledge_graph` | Quality analysis of generated ontology | Feedback loop |
| `memory_add_relations` | Save to memory graph | Long-term storage |
| `memory_get_relations` | Retrieve existing ontology | Building on prior work |
| `search` | Connect to existing graphs | Context enrichment |

### SEO Analysis
| Tool | Purpose in Skill | When Triggered |
|------|-----------------|----------------|
| `analyze_google_search_results` | Map informational supply | Topic analysis step 1 |
| `analyze_related_search_queries` | Map search demand | Topic analysis step 2 |
| `search_queries_vs_search_results` | Supply-demand gaps | Topic analysis step 3 |
| `generate_seo_report` | Full content audit | Content analysis step 2 |
| `overlap_between_texts` | Competitor overlap | Competitor analysis |
| `difference_between_texts` | Competitor gaps | Competitor analysis |

## Tool → Skill Reverse Index

| Tool | Used By Skills |
|------|---------------|
| `generate_knowledge_graph` | Cognitive Variability, Critical Perspective, Ontology Creator, Writing Assistant |
| `create_knowledge_graph` | Ontology Creator |
| `analyze_existing_graph_by_name` | (Direct user request) |
| `generate_content_gaps` | Cognitive Variability, Critical Perspective |
| `generate_topical_clusters` | (Direct user request) |
| `generate_contextual_hint` | (Direct user request — lightweight RAG) |
| `generate_research_questions` | Cognitive Variability, Critical Perspective |
| `generate_research_ideas` | (Direct user request) |
| `research_questions_from_graph` | (Direct user request) |
| `develop_latent_topics` | Cognitive Variability, Critical Perspective |
| `develop_conceptual_bridges` | Critical Perspective |
| `develop_text_tool` | Critical Perspective, Writing Assistant |
| `generate_responses_from_graph` | (Direct user request) |
| `overlap_between_texts` | Critical Perspective, SEO Analysis |
| `difference_between_texts` | Critical Perspective, SEO Analysis |
| `analyze_google_search_results` | SEO Analysis |
| `analyze_related_search_queries` | SEO Analysis |
| `search_queries_vs_search_results` | SEO Analysis |
| `generate_seo_report` | Writing Assistant, SEO Analysis |
| `memory_add_relations` | Ontology Creator |
| `memory_get_relations` | Ontology Creator |
| `retrieve_from_knowledge_base` | (Direct user request — GraphRAG) |
| `list_graphs` | (Direct user request) |
| `search` | Ontology Creator |
| `fetch` | (Direct user request) |

## Tool Categories Quick Reference
| Category | Tools | Count |
|----------|-------|-------|
| Graph Generation | generate_knowledge_graph, create_knowledge_graph, analyze_existing_graph_by_name, generate_contextual_hint, retrieve_from_knowledge_base | 5 |
| Content Analysis | generate_content_gaps, generate_topical_clusters, develop_text_tool | 3 |
| Research | generate_research_questions, generate_research_ideas, research_questions_from_graph, develop_latent_topics, develop_conceptual_bridges, generate_responses_from_graph | 6 |
| Comparative | overlap_between_texts, difference_between_texts | 2 |
| SEO | analyze_google_search_results, analyze_related_search_queries, search_queries_vs_search_results, generate_seo_report | 4 |
| Memory | memory_add_relations, memory_get_relations | 2 |
| Search | list_graphs, search, fetch | 3 |
| **Total** | | **25** |
