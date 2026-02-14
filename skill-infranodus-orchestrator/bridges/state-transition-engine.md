# State Transition Engine — Cognitive State Machine

> **Layer**: 4 (Bridge) | **Dependencies**: `core/graph-analytics.md`, `modules/cognitive-variability`, `modules/critical-perspective`
> **Dependents**: `SKILL.md` (index), `bridges/workflow-orchestrator`
> **Tags**: `#bridge` `#hyperedge` `#state-machine` `#transitions` `#symbolic` `#neural`

## Purpose
This bridge file formalizes the cognitive state machine — the transitions between states, their triggers, guards, and effects. It connects the Cognitive Variability module's state definitions with the Critical Perspective module's intervention protocols and the Writing Assistant's pattern detection.

## State Machine Definition

```
States: { BIASED, FOCUSED, DIVERSIFIED, DISPERSED }
Events: { dwelling_exceeded, pattern_detected, user_request, emergency, goal_change }
Guards: { dwelling_time, energy_level, user_sophistication, context_type }
```

## Transition Table

| From | To | Trigger | Guard | Action | Priority |
|------|-----|---------|-------|--------|----------|
| BIASED | FOCUSED | dwelling ≥ 3 | energy > low | "How do these connect to bigger picture?" | Normal |
| BIASED | FOCUSED | critical_perspective | priority = HIGHEST | Question core assumption | High |
| BIASED | DISPERSED | emergency_lockin | dwelling ≥ 5 | Aggressively challenge with opposites | Emergency |
| FOCUSED | DIVERSIFIED | dwelling ≥ 5 | energy > low | "What haven't we considered?" | Normal |
| FOCUSED | DIVERSIFIED | critical_perspective | priority = HIGH | Challenge narrative boundaries | High |
| FOCUSED | DISPERSED | boredom_signal | emotional = boredom | Break pattern with novelty | Normal |
| DIVERSIFIED | FOCUSED | dwelling ≥ 7, user wants focus | goal = production | "Which thread resonates most?" | Normal |
| DIVERSIFIED | DISPERSED | dwelling ≥ 7, user wants novelty | goal = exploration | "What if we threw all this out?" | Normal |
| DIVERSIFIED | FOCUSED | analysis_paralysis | dwelling ≥ 7 | Critical perspective: what prevents movement? | Emergency |
| DISPERSED | BIASED | dwelling ≥ 4 | energy > low | "Which scattered idea feels most fun?" | Normal |
| DISPERSED | BIASED | playfulness | any | Use play, not pressure | Normal |
| DISPERSED | FOCUSED | user_request | explicit request | Direct stabilization | Override |
| ANY | ANY | user_explicit | user names target state | Direct transition | Override |
| ANY | stable | chaos_detected | 3+ rapid changes | Encourage brief dwelling | Emergency |

## Graph-to-State Mapping

The graph structure output from InfraNodus tools maps directly to cognitive states:

| Graph Metric | BIASED | FOCUSED | DIVERSIFIED | DISPERSED |
|-------------|--------|---------|-------------|-----------|
| Modularity | < 0.2 | 0.2–0.4 | 0.4–0.7 | > 0.7 or fragmented |
| Top node dominance | Very high | Moderate | Low | Low/chaotic |
| Cluster count | 1–2 | 2–4 | 4–8 | Many small |
| Gap count | Few | Few | Many significant | Many trivial |
| Diversity score | Low | Moderate | High | Chaotic |
| Narrative coherence | Singular thread | Clear arc | Multiple arcs | No arc |

## Dwelling Time Thresholds

| State | Threshold | Extended | Critical |
|-------|-----------|----------|----------|
| BIASED | 2–3 | 4 (intervention) | 5+ (emergency) |
| FOCUSED | 3–5 | 6 (intervention) | 7+ (emergency) |
| DIVERSIFIED | 4–7 | 8 (intervention) | 9+ (emergency) |
| DISPERSED | 2–4 | 5 (intervention) | 6+ (emergency) |

## Emotional Signal Processing

### Continue Signals (stay in current state)
| Emotion | Typical State | Interpretation |
|---------|--------------|----------------|
| Inspiration | Dispersed/Diversified | Active creative processing |
| Excitement | Transitions | Healthy movement validates direction |
| Flow | Focused | Right mode for current work |
| Satisfaction | Biased completion | Implementation reward |

### Transition Signals (time to move)
| Emotion | Typical State | Target |
|---------|--------------|--------|
| Exhaustion | Any overstayed | Force movement to adjacent state |
| Frustration | Biased/Focused lock-in | Break pattern → Diversified/Dispersed |
| Despair | Dispersed extended | Need structure → Biased via play |
| Boredom | Focused saturation | Need novelty → Diversified |
| Anxiety | Dispersed/Diversified | Need simplicity → Focused/Biased |

## Creative Flow Cycle (Optimal Traversal)
```
DISPERSED → BIASED → FOCUSED → DIVERSIFIED → DISPERSED
(generate)   (choose)   (refine)   (cross-pollinate)  (break apart)
```

## Strategic Oscillation Patterns
```
Iterative Prototyping:  DISPERSED ↔ BIASED   (generate ↔ select)
Sustained Development:  FOCUSED ↔ DIVERSIFIED (build ↔ integrate)
Production Cycle:       BIASED ↔ FOCUSED      (implement ↔ refine)
```

## Delivery Calibration Rules
| User Signal | Calibration Level | Style |
|-------------|-------------------|-------|
| No framework awareness | Level 1: Invisible | Natural questions only |
| Mentions "thinking state" | Level 2: Transparent | Light framework language |
| Uses state names | Level 3: Collaborative | Explicit state discussion |
| Requests specific state | Override | Direct transition |
