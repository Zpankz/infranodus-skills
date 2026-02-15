# DAG Traversal — Module Loading Algorithm

> **Layer**: 5 (Script) | **Dependencies**: All layers
> **Tags**: `#script` `#algorithm` `#dag` `#traversal` `#symbolic`

## Architecture DAG

```
Layer 0 (Roots):
  core/types.md ─────────────────┐
  core/ontology.md ──────────────┤
                                 │
Layer 1 (Core Functions):        │
  core/graph-analytics.md ◄──────┤
  core/text-processing.md ◄──────┤
  core/api-reference.md ◄────────┘
          │
Layer 2 (Tools):
  modules/graph-generation.md ◄──┐
  modules/content-analysis.md ◄──┤
  modules/research-engine.md ◄───┤── (depend on Layer 0+1)
  modules/comparative-analysis.md◄┤
  modules/seo-tools.md ◄─────────┤
  modules/memory-manager.md ◄────┤
  modules/search-discovery.md ◄──┘
          │
Layer 3 (Skills):
  modules/cognitive-variability.md ◄──┐
  modules/critical-perspective.md ◄───┤── (depend on Layer 0+1+2)
  modules/writing-assistant.md ◄──────┤
  modules/ontology-creator.md ◄───────┤
  modules/seo-analysis.md ◄───────────┘
          │
Layer 4 (Bridges):
  bridges/skill-tool-map.md ◄─────────┐
  bridges/state-transition-engine.md ◄─┤── (depend on Layer 2+3)
  bridges/pattern-detection-bridge.md ◄┤
  bridges/platform-adapters.md ◄───────┤
  bridges/workflow-orchestrator.md ◄───┘
          │
Layer 5 (Templates & Resources):
  templates/prompts/*.md ◄─────────────┐
  templates/workflows/*.md ◄───────────┤── (depend on all above)
  templates/schemas/*.md ◄─────────────┤
  resources/*.md ◄─────────────────────┘
          │
Layer 6 (Index):
  SKILL.md ◄─── (depends on everything, loads selectively)
```

## Progressive Loading Algorithm

### Step 1: Intent Classification
```
Read user input → Classify intent:
  text_editing → Writing Assistant path
  analysis → Graph Generation path
  ontology → Ontology Creator path
  seo → SEO Analysis path
  comparison → Comparative Analysis path
  research → Research Engine path
  memory → Memory Manager path
  cognitive → Cognitive Variability path
  critical → Critical Perspective path
  search → Search Discovery path
```

### Step 2: Load Primary Module
```
Load the module matching classified intent
This module's header declares its dependencies
```

### Step 3: Load Dependencies (Topological Order)
```
For the primary module, resolve dependencies bottom-up:
  1. Core types (always loaded — minimal footprint)
  2. Required Layer 1 modules (as declared)
  3. Required Layer 2 tool modules (as declared)
  4. The primary Layer 3 skill module itself
```

### Step 4: Check for Handoff Triggers
```
During execution, monitor for:
  - Pattern detection signals → load pattern-detection-bridge
  - Dwelling thresholds → load state-transition-engine
  - Cross-skill triggers → load workflow-orchestrator
  - Tool invocations → load skill-tool-map for resolution
```

### Step 5: Lazy Load on Demand
```
Templates: Only loaded when generating specific output formats
Resources: Only loaded when reference data is needed
Bridges: Only loaded when inter-module routing is triggered
```

## Dependency Resolution

### Topological Sort of All Modules
```
1.  core/types.md               (no deps)
2.  core/ontology.md            (no deps)
3.  core/graph-analytics.md     (deps: 1)
4.  core/text-processing.md     (deps: 1)
5.  core/api-reference.md       (deps: 1)
6.  modules/graph-generation    (deps: 1, 3, 5)
7.  modules/content-analysis    (deps: 1, 3, 4, 5)
8.  modules/research-engine     (deps: 1, 5)
9.  modules/comparative-analysis(deps: 1, 5)
10. modules/seo-tools           (deps: 1, 5)
11. modules/memory-manager      (deps: 1, 2, 5)
12. modules/search-discovery    (deps: 1, 5)
13. modules/cognitive-variability(deps: 1, 3, 6, 7, 8)
14. modules/critical-perspective (deps: 1, 7, 8, 9)
15. modules/writing-assistant   (deps: 1, 4, 6, 7, 10)
16. modules/ontology-creator    (deps: 1, 2, 6, 11, 12)
17. modules/seo-analysis        (deps: 1, 6, 7, 9, 10)
18. bridges/skill-tool-map      (deps: 6-17)
19. bridges/state-transition    (deps: 3, 13, 14)
20. bridges/pattern-detection   (deps: 4, 13, 15)
21. bridges/platform-adapters   (deps: 4, 5)
22. bridges/workflow-orchestrator(deps: 13-21)
```

## Context Budget Management
```
Total available context: varies by platform
Priority allocation:
  1. SKILL.md routing (always loaded) — ~2KB
  2. Primary skill module — ~3-5KB
  3. Required core modules — ~2-3KB each
  4. Required tool modules — ~1-2KB each
  5. Bridge files (on demand) — ~2-3KB each
  6. Templates (on demand) — ~1-2KB each
  7. Resources (on demand) — ~1-2KB each

Estimated total for typical operation: 15-25KB
Maximum with all modules: ~60KB
```

## Cycle Detection Guard
```
No cycles exist in this DAG by design:
- Types/Ontology are pure source nodes (no dependencies)
- Each layer depends only on previous layers
- Bridge files depend on modules but modules never depend on bridges
- SKILL.md depends on everything but nothing depends on SKILL.md
```
