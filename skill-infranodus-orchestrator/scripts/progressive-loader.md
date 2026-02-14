# Progressive Loading Strategy — Context Engineering

> **Layer**: 5 (Script) | **Dependencies**: `scripts/dag-traversal.md`
> **Tags**: `#script` `#loading` `#context` `#optimization`

## Loading Tiers

### Tier 0: Always Loaded (Index)
```
SKILL.md — Intent classification, routing, activation triggers
Cost: ~3KB
Contains: Frontmatter, activation description, routing decision tree, tool list
```

### Tier 1: Load on Classification (Primary Path)
```
Classified as text editing?  → modules/writing-assistant.md
Classified as analysis?      → modules/graph-generation.md + modules/content-analysis.md
Classified as ontology?      → modules/ontology-creator.md
Classified as SEO?           → modules/seo-analysis.md
Classified as comparison?    → modules/comparative-analysis.md
Classified as research?      → modules/research-engine.md
Classified as memory?        → modules/memory-manager.md
Classified as cognitive?     → modules/cognitive-variability.md
Classified as critical?      → modules/critical-perspective.md
Cost: ~3-5KB per module
```

### Tier 2: Load on Dependency Resolution
```
Module declares its dependencies in header.
Load only the specific core modules needed:
  core/types.md              → Always (tiny, defines shared language)
  core/api-reference.md      → When any tool is invoked
  core/graph-analytics.md    → When graph interpretation needed
  core/text-processing.md    → When text patterns analyzed
  core/ontology.md           → When ontology generation triggered
Cost: ~2-3KB per core module
```

### Tier 3: Load on Trigger (Bridges)
```
Pattern detected in text    → bridges/pattern-detection-bridge.md
Dwelling threshold exceeded → bridges/state-transition-engine.md
Inter-module handoff needed → bridges/workflow-orchestrator.md
Tool invocation needed      → bridges/skill-tool-map.md
Platform-specific needed    → bridges/platform-adapters.md
Cost: ~2-3KB per bridge
```

### Tier 4: Load on Output (Templates)
```
Generating analysis output  → templates/prompts/analysis-prompts.md
Generating AI advice        → templates/prompts/advice-prompts.md
Building chat context       → templates/prompts/chat-prompts.md
Creating ontology           → templates/prompts/ontology-prompts.md
Running pipeline            → templates/workflows/{relevant}.md
Constructing API call       → templates/schemas/tool-parameters.md
Cost: ~1-2KB per template
```

### Tier 5: Load on Reference (Resources)
```
Need cognitive state lookup → resources/cognitive-states-reference.md
Need relation code lookup   → resources/relation-codes-reference.md
Need graph metric interpret → resources/graph-metrics-reference.md
Need naturalness check      → resources/ai-naturalness-rules.md
Cost: ~1-2KB per resource
```

## Context Budget Profiles

### Minimal Operation (Single Tool)
```
SKILL.md (routing)           2KB
core/types.md                2KB
One tool module              2KB
templates/schemas/tool-params 2KB
                            ----
Total:                       ~8KB
```

### Standard Operation (Skill + Tools)
```
SKILL.md (routing)           2KB
core/types.md                2KB
core/api-reference.md        3KB
One skill module             4KB
Two tool modules             4KB
                            ----
Total:                      ~15KB
```

### Full Pipeline Operation
```
SKILL.md (routing)           2KB
core/types.md                2KB
core/api-reference.md        3KB
core/graph-analytics.md      3KB
Primary skill module         4KB
2-3 tool modules             6KB
1 bridge file                3KB
1 workflow template          2KB
1 schema template            2KB
                            ----
Total:                      ~27KB
```

### Maximum (All Modules — Rare)
```
All 35 files loaded          ~60KB
Scenario: Complex multi-skill orchestration with handoffs
```

## Unloading Strategy
When context approaches limits:
1. Unload resources first (can be re-loaded if needed)
2. Unload completed pipeline templates
3. Unload tool modules for completed tools
4. Never unload: SKILL.md, active skill module, core/types.md

## Progressive Disclosure
For the user, information is progressively disclosed:
1. Start with response to immediate need
2. Note patterns/insights if detected (don't dump everything)
3. Offer deeper analysis as follow-up ("Want me to check for gaps?")
4. Trigger handoffs only when genuinely warranted
5. Never mention framework internals at Level 1 (Invisible)
