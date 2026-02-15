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

## Intent Router

| Intent Signal | Route To | Load |
|--------------|----------|------|
| Fix/edit/correct/improve text | Writing Assistant | `modules/writing-assistant.md` |
| Analyze text/topic/URL | Graph + Content Analysis | `core/api-reference.md` |
| Create ontology/knowledge graph | Ontology Creator | `modules/ontology-creator.md` |
| SEO/optimize for search | SEO Analysis | `modules/seo-analysis.md` |
| Compare texts/perspectives | Comparative Analysis | `core/api-reference.md` |
| Research questions/ideas | Research Engine | `core/api-reference.md` |
| Save/remember/store | Memory Manager | `core/api-reference.md` |
| Find/search graphs | Search Discovery | `core/api-reference.md` |
| Stuck/blocked/breakthrough | Cognitive Variability | `modules/cognitive-variability.md` |
| Question assumptions/blind spots | Critical Perspective | `modules/critical-perspective.md` |
| Brainstorm/explore wildly | Cognitive Variability (DISPERSED) | `modules/cognitive-variability.md` |
| Focus/decide/choose | Cognitive Variability (BIASED->FOCUSED) | `modules/cognitive-variability.md` |
| Retrieve from knowledge base | GraphRAG | `core/api-reference.md` |

### Behavioral Signals (Implicit)

| Signal | State | Action |
|--------|-------|--------|
| Repeating same idea 3+ times | BIASED | `bridges/state-transition-engine.md` -> intervene |
| Long flowing text | FOCUSED | Monitor, don't interrupt |
| Jumping between topics | DIVERSIFIED | Monitor for paralysis |
| Scattered fragments | DISPERSED | `modules/cognitive-variability.md` -> guide |
| Text patterns detected | Pattern signal | `bridges/pattern-detection-bridge.md` |

## Loading Strategy

### Always Loaded
- `SKILL.md` (this file) -- intent routing (~2KB)
- `core/types.md` -- shared type system (~2KB)

### On Intent Classification
Load the primary skill module + its declared dependencies.

### On Trigger (Lazy)
- Pattern detected -> `bridges/pattern-detection-bridge.md`
- Dwelling threshold -> `bridges/state-transition-engine.md`
- Inter-module handoff -> `bridges/workflow-orchestrator.md`
- Tool resolution -> `bridges/skill-tool-map.md`
- Format conversion -> `bridges/format-bridge.md`
- Output generation -> `templates/prompts.md` or `templates/workflows.md`

### Budget: 8KB minimal | 15KB standard | 27KB pipeline | 60KB maximum

## Module Directory

### Core (Layer 0-1) -- Always available
- `core/types.md` -- GraphNode, GraphEdge, TopCluster, GraphGap, CognitiveState, PatternSignal
- `core/ontology.md` -- 10 relation codes, wikilink syntax, entity processing pipeline
- `core/graph-analytics.md` -- Modularity, centrality, diversity stats, cognitive state mapping
- `core/text-processing.md` -- Entity detection, pattern detection, AI naturalness rules
- `core/api-reference.md` -- All 25 InfraNodus MCP tool endpoints (single source of truth)

### Skills (Layer 2) -- Load on classification
- `modules/cognitive-variability.md` -- Four states, transitions, dwelling thresholds, emotional feedback
- `modules/critical-perspective.md` -- Assumption surfacing, perspective shifting, gap identification
- `modules/writing-assistant.md` -- Text refinement, pattern-as-sensory-system, AI avoidance
- `modules/ontology-creator.md` -- Knowledge graph generation in wikilink syntax
- `modules/seo-analysis.md` -- Supply/demand/gap framework, 4 SEO tools, content optimization

### Bridges (Layer 3) -- Load on trigger
- `bridges/skill-tool-map.md` -- Bidirectional skill<->tool mapping registry
- `bridges/state-transition-engine.md` -- Cognitive state machine, guards, tool pipelines
- `bridges/pattern-detection-bridge.md` -- Writing pattern -> cognitive state diagnosis
- `bridges/workflow-orchestrator.md` -- Inter-module routing DAG with handoff protocols
- `bridges/format-bridge.md` -- 7-format conversion spec (links to graph_converter.py)

### Templates (Layer 4) -- Load on output
- `templates/prompts.md` -- Analysis, advice, chat, ontology prompt templates
- `templates/workflows.md` -- Knowledge graph, text analysis, comparison, SEO pipelines
- `templates/tool-parameters.md` -- Quick reference parameter matrix

### Scripts -- Executable utilities
- `scripts/graph_converter.py` -- 5-format converter (Mermaid, Graphology, DOT, Obsidian, Wikilinks)
- `scripts/workflow_analyzer.py` -- Request classifier with 10-pattern scoring

### Assets
- `assets/obsidian-templates/research-moc-template.md` -- Research MOC template
- `assets/obsidian-templates/seo-strategy-template.md` -- SEO strategy template

## DAG Integrity

No cycles by design:
- `core/types.md` and `core/ontology.md` are pure roots (no dependencies)
- Each layer depends only on previous layers
- Bridges depend on modules; modules never depend on bridges
- `SKILL.md` depends on everything; nothing depends on `SKILL.md`
