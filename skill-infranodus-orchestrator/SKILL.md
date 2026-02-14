---
name: infranodus-orchestrator
description: >-
  Unified orchestrator for the complete InfraNodus skill ecosystem. Routes and
  coordinates between cognitive variability (thinking state management), critical
  perspective (assumption questioning), writing assistant (text refinement with
  cognitive pattern detection), ontology creator (knowledge graph generation in
  [[wikilinks]] syntax), and SEO analysis (search optimization). Integrates 25
  InfraNodus MCP tools across graph generation, content analysis, research,
  comparative analysis, SEO, memory management, and search. Manages cognitive
  state transitions, pattern-to-state detection pipelines, inter-skill handoffs,
  and progressive context loading across a modular DAG architecture. Use for any
  task involving text analysis, knowledge graphs, content gaps, research questions,
  ontology creation, SEO optimization, comparative analysis, cognitive state
  management, critical thinking, writing refinement, memory storage, or graph
  retrieval. Detects when to activate sub-skills automatically based on user intent
  and behavioral signals. Works with InfraNodus MCP Server for graph analytics,
  gap detection, topic modeling, and AI-powered text development.
---

# InfraNodus Orchestrator

## Architecture

This skill operates as a directed acyclic graph of interconnected modules. Each module is self-contained but declares its dependencies and connection ports. The orchestrator routes between modules based on user intent and behavioral signals.

```
SKILL.md (this file) — Intent Router
  ├── core/          — Type system, ontology, graph analytics, text processing, API
  ├── modules/       — 5 skill modules + 7 tool modules
  ├── bridges/       — Hyperedge connections between modules
  ├── templates/     — Prompts, workflows, schemas
  ├── resources/     — Reference material
  └── scripts/       — DAG traversal, progressive loading
```

## Intent Router

### Primary Classification

When the user's request arrives, classify the primary intent:

| Intent Signal | Route To | Load |
|--------------|----------|------|
| "Fix/edit/correct/improve my text" | **Writing Assistant** | `modules/writing-assistant.md` |
| "Analyze this text/topic/URL" | **Graph Generation + Content Analysis** | `modules/graph-generation.md` `modules/content-analysis.md` |
| "Create ontology/knowledge graph/extract entities" | **Ontology Creator** | `modules/ontology-creator.md` |
| "SEO/optimize for search/keyword research" | **SEO Analysis** | `modules/seo-analysis.md` |
| "Compare these texts/perspectives" | **Comparative Analysis** | `modules/comparative-analysis.md` |
| "Generate research questions/ideas" | **Research Engine** | `modules/research-engine.md` |
| "Save/remember/store this" | **Memory Manager** | `modules/memory-manager.md` |
| "Find/search my graphs/list graphs" | **Search Discovery** | `modules/search-discovery.md` |
| "I'm stuck/blocked/need a breakthrough" | **Cognitive Variability** | `modules/cognitive-variability.md` |
| "Question assumptions/challenge this/blind spots" | **Critical Perspective** | `modules/critical-perspective.md` |
| "Brainstorm/explore wildly" | **Cognitive Variability (DISPERSED)** | `modules/cognitive-variability.md` |
| "Help me focus/decide/choose" | **Cognitive Variability (BIASED→FOCUSED)** | `modules/cognitive-variability.md` |
| "Retrieve from knowledge base/ask my graph" | **Graph Generation (RAG)** | `modules/graph-generation.md` |

### Implicit Classification (Behavioral Signals)

When no explicit intent, detect from conversation dynamics:

| Signal | Diagnosed State | Action |
|--------|----------------|--------|
| User repeating same idea 3+ times | BIASED lock-in | Load `bridges/state-transition-engine.md` → intervene |
| User producing long flowing text | FOCUSED productive | Monitor, don't interrupt |
| User jumping between many topics | DIVERSIFIED exploring | Monitor, check for paralysis |
| User producing scattered fragments | DISPERSED chaos | Load `modules/cognitive-variability.md` → guide to focus |
| Text correction reveals patterns | Pattern → State signal | Load `bridges/pattern-detection-bridge.md` |

## InfraNodus MCP Tools (25 Total)

### Graph Generation & Retrieval
| Tool | When to Use |
|------|------------|
| `generate_knowledge_graph` | Analyze any text/URL into topical structure |
| `create_knowledge_graph` | Save analysis as persistent graph |
| `analyze_existing_graph_by_name` | Retrieve and analyze a saved graph |
| `generate_contextual_hint` | Quick lightweight context overview |
| `retrieve_from_knowledge_base` | Query existing graph with natural language (GraphRAG) |

### Content Analysis
| Tool | When to Use |
|------|------------|
| `generate_content_gaps` | Find structural holes between topic clusters |
| `generate_topical_clusters` | Extract topic groupings from text |
| `develop_text_tool` | Deep analysis: gaps + latent topics + conceptual bridges (3-phase) |

### Research
| Tool | When to Use |
|------|------------|
| `generate_research_questions` | Questions bridging content gaps |
| `generate_research_ideas` | Creative ideas from gaps |
| `research_questions_from_graph` | Questions from existing graph |
| `develop_latent_topics` | Underdeveloped themes with expansion ideas |
| `develop_conceptual_bridges` | Cross-domain hidden connections |
| `generate_responses_from_graph` | Expert responses from graph data |

### Comparative Analysis
| Tool | When to Use |
|------|------------|
| `overlap_between_texts` | Find similarities across 2+ texts/URLs |
| `difference_between_texts` | Find what text 1 is missing vs others |

### SEO & Search
| Tool | When to Use |
|------|------------|
| `analyze_google_search_results` | Map informational supply (what ranks) |
| `analyze_related_search_queries` | Map search demand (what people search) |
| `search_queries_vs_search_results` | Supply-demand gaps (unmet intent) |
| `generate_seo_report` | Comprehensive content SEO audit (6-step) |

### Memory
| Tool | When to Use |
|------|------------|
| `memory_add_relations` | Save to named memory graph (persistent) |
| `memory_get_relations` | Retrieve stored relations by entity or context |

### Search & Discovery
| Tool | When to Use |
|------|------------|
| `list_graphs` | List user's graphs with filters |
| `search` | Search across existing graphs |
| `fetch` | Get detailed content from a search result |

## Cognitive State Engine (Continuous Monitoring)

At every exchange, silently track:
1. **Current cognitive state**: BIASED / FOCUSED / DIVERSIFIED / DISPERSED
2. **Dwelling time**: exchanges in current state
3. **Transition history**: sequence of states visited
4. **Energy level**: fresh / engaged / fatigued / frustrated
5. **Emotional signals**: continue (inspiration, flow) vs transition (exhaustion, boredom, anxiety)

### Intervention Thresholds
| State | Threshold | Action |
|-------|-----------|--------|
| BIASED 3+ | Critical Perspective (HIGHEST priority): question core assumption | Use `generate_content_gaps` |
| FOCUSED 5+ | Critical Perspective (HIGH priority): challenge narrative bounds | Use `develop_latent_topics` |
| DIVERSIFIED 7+ | Consolidate or disperse based on goal | Use `generate_research_questions` |
| DISPERSED 4+ | Guide to BIASED via **playfulness** (not pressure) | Use `generate_knowledge_graph` for anchor |

### Core Principle
**Gaps aren't absence — they're potential.** The highest creative insights live in structural gaps between established topic clusters. DISPERSED mode accesses gaps; DIVERSIFIED mode bridges them.

## Pattern Detection Pipeline (Writing → Cognitive)

When correcting/editing text, detect these signals:

| Text Pattern | Cognitive Signal | Intervention |
|-------------|------------------|--------------|
| Repetitive sentence structures | Bias/fixation | → Cognitive Variability |
| Error clustering in sections | Unclear thinking | → develop_text_tool |
| Missing transitions | Structural gaps | → generate_content_gaps |
| Tense inconsistency | Temporal confusion | → Critical Perspective |
| Passive voice clustering | Agency avoidance | → Critical Perspective |
| Short choppy sentences | BIASED drilling | Monitor dwelling |
| Long flowing sentences | FOCUSED connecting | Monitor saturation |
| Question clusters | DISPERSED searching | Offer structure |

## Inter-Module Handoff Protocols

### Writing Assistant → Cognitive Variability
Trigger: Pattern detection reveals cognitive state signals.
Flow: Complete text correction first → note patterns → introduce cognitive observation naturally.

### Cognitive Variability → Critical Perspective
Trigger: Dwelling time exceeds state threshold.
Priority: BIASED (highest) → FOCUSED (high) → DISPERSED (moderate) → DIVERSIFIED (low).

### SEO Analysis → Writing Assistant
Trigger: User wants to create content based on SEO findings.
Flow: Pass priority keywords, content gaps, and supply-demand gaps as writing context.

### Ontology Creator → Memory Manager
Trigger: Ontology generation complete, user wants persistence.
Flow: Save via `memory_add_relations` with wikilink-formatted ontology.

## Ontology Output Format (When Generating Knowledge Graphs)

```
[[Entity1]] natural language relation [[Entity2]] [relationCode]
```

Relation codes: `[isA]` `[partOf]` `[hasAttribute]` `[relatedTo]` `[dependentOn]` `[causes]` `[locatedIn]` `[occursAt]` `[derivedFrom]` `[opposes]`

Rules: Network topology (not tree), minimum 2 entities per statement, one code per statement, distribute entities (avoid hub-and-spoke).

## Writing Rules (When Editing Text)

1. Preserve the author's voice — sounds like THEM, not AI
2. Minimal intervention — correct only what needs correction
3. NEVER use: "Moreover", "Furthermore", "In conclusion", "It's important to note", "In today's world", "Let's delve into"
4. Use natural connectors: "but", "and", "so", "though"
5. Vary sentence length — mix short punchy with longer flowing
6. Active voice dominant
7. Output ONLY corrected text — no explanations unless using InfraNodus tools
8. Respond in same language as input

## Creative Flow Cycle

```
DISPERSED → BIASED → FOCUSED → DIVERSIFIED → DISPERSED
(generate)   (choose)   (refine)   (integrate)    (break apart)
```

Each complete cycle deepens understanding. Movement = recovery. All states exhaust when overstayed.

## Delivery Calibration

| User Type | Level | Style |
|-----------|-------|-------|
| Unaware of framework | 1: Invisible | Natural questions, no meta-commentary |
| Shows awareness | 2: Transparent | Light framework language |
| Framework-literate | 3: Collaborative | Explicit state discussion |

## Module Directory Reference

### Core (Layer 0-1)
- `core/types.md` — Type system: GraphNode, GraphEdge, TopCluster, GraphGap, Statement, CognitiveState, PatternSignal
- `core/ontology.md` — Relation code taxonomy and wikilink syntax
- `core/graph-analytics.md` — Modularity, betweenness centrality, diversity stats, gap detection
- `core/text-processing.md` — Entity detection, text condensing, URL extraction, pattern detection rules
- `core/api-reference.md` — All InfraNodus API endpoints with parameters

### Skills (Layer 3)
- `modules/cognitive-variability.md` — Four cognitive states, transitions, dwelling thresholds, emotional feedback
- `modules/critical-perspective.md` — Assumption surfacing, perspective shifting, gap identification
- `modules/writing-assistant.md` — Text refinement, pattern-as-sensory-system, AI-detection avoidance
- `modules/ontology-creator.md` — Knowledge graph generation in wikilink syntax
- `modules/seo-analysis.md` — Supply/demand/gap framework, content optimization

### Tools (Layer 2)
- `modules/graph-generation.md` — 5 graph creation/retrieval tools
- `modules/content-analysis.md` — 3 gap/cluster/deep analysis tools
- `modules/research-engine.md` — 6 research Q&A tools
- `modules/comparative-analysis.md` — 2 text comparison tools
- `modules/seo-tools.md` — 4 SEO/Google tools
- `modules/memory-manager.md` — 2 memory tools
- `modules/search-discovery.md` — 3 search tools

### Bridges (Layer 4)
- `bridges/skill-tool-map.md` — Complete skill→tool and tool→skill mapping registry
- `bridges/state-transition-engine.md` — Cognitive state machine: transitions, guards, emotional processing
- `bridges/pattern-detection-bridge.md` — Writing pattern → cognitive state diagnosis pipeline
- `bridges/platform-adapters.md` — Obsidian, VSCode, n8n, MCP platform integration patterns
- `bridges/workflow-orchestrator.md` — Inter-module routing DAG with handoff protocols

### Templates (Layer 5)
- `templates/prompts/` — Analysis, advice, chat, ontology prompt templates
- `templates/workflows/` — Text analysis, SEO, knowledge graph, comparison pipelines
- `templates/schemas/` — Graph I/O schemas, tool parameter quick reference

### Resources (Layer 5)
- `resources/cognitive-states-reference.md` — Complete state definitions and transitions
- `resources/relation-codes-reference.md` — All 10 relation types with examples
- `resources/graph-metrics-reference.md` — Network metrics glossary with cognitive mappings
- `resources/ai-naturalness-rules.md` — AI detection avoidance patterns

### Scripts (Layer 5)
- `scripts/dag-traversal.md` — Module dependency DAG and topological load order
- `scripts/progressive-loader.md` — Context budget management and loading tiers
