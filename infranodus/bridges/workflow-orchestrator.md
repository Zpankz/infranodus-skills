# Workflow Orchestrator — Inter-Module Routing DAG

> **Layer**: 4 (Bridge) | **Dependencies**: All `modules/*`, `bridges/state-transition-engine`, `bridges/pattern-detection-bridge`, `bridges/skill-tool-map`
> **Dependents**: `SKILL.md` (index)
> **Tags**: `#bridge` `#hyperedge` `#routing` `#dag` `#orchestration` `#symbolic` `#neural`

## Purpose
This bridge defines the directed acyclic graph of inter-module routing — when one module hands off to another, what triggers the handoff, and what context flows between them. It is the central nervous system of the orchestrator skill.

## Module Interaction DAG

```
                    ┌─────────────────────────┐
                    │     User Input           │
                    └────────────┬─────────────┘
                                 │
                    ┌────────────▼─────────────┐
                    │   SKILL.md (Router)       │
                    │   Intent Classification   │
                    └──┬───┬───┬───┬───┬───────┘
                       │   │   │   │   │
          ┌────────────┘   │   │   │   └────────────┐
          ▼                ▼   │   ▼                ▼
    ┌──────────┐   ┌──────────┐│┌──────────┐  ┌──────────┐
    │ Writing  │   │ Ontology ││ │   SEO    │  │ Research │
    │ Assistant│   │ Creator  │││ Analysis │  │ (Direct) │
    └────┬─────┘   └──────────┘│└──────────┘  └──────────┘
         │                     │
         │ patterns            │
         ▼                     │
    ┌──────────────┐          │
    │ Pattern      │          │
    │ Detection    │          │
    │ Bridge       │          │
    └──────┬───────┘          │
           │                   │
           ▼                   │
    ┌──────────────┐          │
    │ State        │◄─────────┘
    │ Transition   │  (all modules can query state)
    │ Engine       │
    └──────┬───────┘
           │
           ▼
    ┌──────────────┐     ┌──────────────┐
    │ Cognitive    │────►│ Critical     │
    │ Variability  │     │ Perspective  │
    └──────────────┘     └──────────────┘
```

## Routing Decision Table

### Primary Intent Classification
| User Intent | Primary Module | Secondary Modules |
|------------|---------------|-------------------|
| "Fix/edit/improve my text" | Writing Assistant | → Pattern Bridge → Cognitive Variability |
| "Analyze this text/topic" | Graph Generation tools | → Content Analysis → Research Engine |
| "Create ontology/knowledge graph" | Ontology Creator | → Graph Generation → Memory Manager |
| "SEO analysis/optimization" | SEO Analysis | → Content Analysis → Writing Assistant |
| "Compare texts/perspectives" | Comparative Analysis | → Critical Perspective |
| "Generate research questions/ideas" | Research Engine | → Content Analysis |
| "Save/remember/store this" | Memory Manager | → Ontology Creator |
| "Find/search my graphs" | Search Discovery | |
| "I'm stuck/blocked" | Cognitive Variability | → Critical Perspective |
| "Question my assumptions" | Critical Perspective | → Content Analysis |
| "Brainstorm/explore ideas" | Cognitive Variability (DISPERSED) | → Research Engine |
| "Help me focus/decide" | Cognitive Variability (BIASED) | → Critical Perspective |

### Handoff Protocols

#### Writing Assistant → Cognitive Variability
**Trigger**: Pattern detection identifies cognitive state signals
**Context passed**:
```
{
  patterns_detected: PatternSignal[],
  diagnosed_state: CognitiveState,
  confidence: number,
  corrected_text: string (already delivered to user)
}
```
**Flow**: Invisible — cognitive intervention follows naturally after text correction

#### Cognitive Variability → Critical Perspective
**Trigger**: Dwelling time exceeds threshold for current state
**Context passed**:
```
{
  current_state: CognitiveState,
  dwelling_time: number,
  priority: "highest" | "high" | "moderate" | "low",
  state_history: string[],
  intervention_type: string
}
```
**Flow**: Critical questions emerge naturally from the conversation state

#### SEO Analysis → Writing Assistant
**Trigger**: User wants to create/improve content based on SEO findings
**Context passed**:
```
{
  priority_keywords: string[],
  content_gaps: string[],
  supply_demand_gaps: string[],
  existing_text: string (if available)
}
```
**Flow**: Writing Assistant receives SEO context for optimized content creation

#### Writing Assistant → Ontology Creator
**Trigger**: Missing transitions or pronoun ambiguity detected
**Context passed**:
```
{
  undefined_entities: string[],
  structural_gaps: string[],
  text_section: string
}
```
**Flow**: Ontology Creator structures the implicit entities and relations

#### Ontology Creator → Memory Manager
**Trigger**: Ontology generation complete, user wants persistence
**Context passed**:
```
{
  ontology_text: string (wikilink format),
  graph_name: string,
  relation_count: number
}
```
**Flow**: Direct save via `memory_add_relations`

## Concurrent Module Activation Rules

1. **Maximum 2 active modules** at any time (primary + secondary)
2. **Writing Assistant** always runs first when text correction is involved
3. **Pattern Detection Bridge** activates silently alongside Writing Assistant
4. **Cognitive Variability** is always monitoring (Step 0) but only intervenes when triggered
5. **Critical Perspective** only activates when explicitly triggered by Cognitive Variability or direct user request
6. **SEO Analysis** and **Writing Assistant** can run sequentially but not in parallel

## Error and Fallback Routing

| Failure Mode | Fallback |
|-------------|----------|
| InfraNodus API unavailable | Operate without tools; rely on skill knowledge alone |
| Tool returns error | Log, continue with available data, inform user |
| State detection uncertain | Default to FOCUSED (most stable) |
| Multiple skills triggered | Prioritize by user's explicit intent |
| Circular handoff detected | Break cycle, return to primary intent |

## Progressive Context Loading Order
When the orchestrator activates, load modules in this order:
```
1. SKILL.md (intent classification + routing rules)
2. Core module relevant to classified intent
3. Tool module(s) needed for the task
4. Bridge files if handoff is needed
5. Templates only when generating specific outputs
6. Resources only when reference data is needed
```
This minimizes context usage while ensuring all necessary modules are available.
