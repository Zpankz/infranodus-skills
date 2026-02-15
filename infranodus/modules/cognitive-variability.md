# Cognitive Variability Module

> **Layer**: 3 | **Dependencies**: `core/types.md`, `core/graph-analytics.md`, `core/api-reference.md`
> **Dependents**: `bridges/state-transition-engine`, `bridges/pattern-detection-bridge`, `bridges/workflow-orchestrator`
> **Tags**: `#skill` `#cognitive` `#states` `#transitions` `#neural` `#core-skill`

## Activation Trigger
Guide conversations through dynamic shifts between zoom levels (scale) and connecting/exploring (intent) to unlock creative breakthroughs and prevent rigid thinking. Use when the user is stuck, needs to develop an idea, or when there is too much repetition or dispersion. Takes the user through stages of thinking — from idea genesis to development, questioning, and disruptive thinking. Identifies structural gaps between idea clusters as spaces for innovation. Tracks temporal dwelling patterns and manages cognitive energy.

## Core Model: Two Spectrums

```
         ZOOMED OUT (Patterns)
              |
    FOCUSED --|-- DIVERSIFIED
              |
CONNECTING ---+--- EXPLORING
              |
    BIASED  --|-- DISPERSED
              |
         ZOOMED IN (Details)
```

## Four Cognitive States

### BIASED (Zoomed in + Connecting) — Stages 8→1→2
- **Feels like**: Tunnel vision, obsessive drive, singular thread dominates
- **Graph signature**: One central node, everything subjugated to it
- **Creative potential**: Driven implementation, singular vision pushes through barriers
- **Best for**: Building from scratch, strong messaging, execution
- **Energy**: Low entry cost, exhausts through obsession
- **Dwelling limit**: 2–3 exchanges before rigidity sets in
- **Emotion signals**: Determination → obsession → exhaustion

### FOCUSED (Zoomed out + Connecting) — Stages 2→3→4
- **Feels like**: Coherent flow, productive rhythm, everything connects
- **Graph signature**: Dense connections, clear narrative arc
- **Creative potential**: Refinement and craft, polishing existing work
- **Best for**: Communication, building cases, sustained productive work
- **Energy**: Moderate cost, most sustainable state
- **Dwelling limit**: 3–5 exchanges before saturation
- **Emotion signals**: Confidence → flow → boredom

### DIVERSIFIED (Zoomed out + Exploring) — Stages 4→5→6
- **Feels like**: Multiple angles simultaneously, polysingular perspective
- **Graph signature**: Multiple clusters with visible gaps between them
- **Creative potential**: Cross-pollination, bridging distant domains
- **Best for**: Research, innovation, strategy, optimal for adaptability
- **Energy**: High entry cost, energizing or draining depending on context
- **Dwelling limit**: 4–7 exchanges before analysis paralysis
- **Emotion signals**: Curiosity → richness → overwhelm

### DISPERSED (Zoomed in + Exploring) — Stages 6→7→8
- **Feels like**: Chaotic exploration, liberation from established patterns
- **Graph signature**: Weak connections, fragmented, structural gaps everywhere
- **Creative potential**: MAXIMUM GENERATION — gaps = where breakthroughs emerge
- **Best for**: Brainstorming, breaking through blocks, accessing creative chaos
- **Energy**: Low entry cost, drains rapidly through anxiety
- **Dwelling limit**: 2–4 exchanges before overwhelm
- **Emotion signals**: Liberation → possibility → anxiety → despair

## Step 0: Continuous Monitoring (Silent)

At every exchange, track:
1. **Current state** and dwelling time (exchanges in this state)
2. **State transition history** (sequence of modes visited)
3. **User objectives** (explicit goals + inferred intent)
4. **Context type** (creative, analytical, decision, implementation)
5. **Energy level** (fresh, engaged, fatigued, frustrated)
6. **User sophistication** (framework-aware vs. naive)

### Pathological Indicators
| Pattern | Detection | Risk |
|---------|-----------|------|
| Lock-in | 5+ exchanges in BIASED | Tunnel vision, missed alternatives |
| Saturation | 6+ exchanges in FOCUSED | Diminishing returns, stagnation |
| Chaos | 3+ rapid state changes | Lost coherence, fragmentation |
| Avoidance | Repeated resistance to transitions | Fear-based rigidity |

## Intervention Protocols

### BIASED (3+ exchanges) → Move to FOCUSED
- **Prompt pattern**: "How do these ideas connect to the bigger picture?"
- **Critical Perspective**: HIGHEST PRIORITY — question the core assumption driving the bias
- **InfraNodus tool**: `generate_content_gaps` — show what's being excluded
- **Energy note**: Be gentle — the obsessive drive feels productive

### FOCUSED (5+ exchanges) → Move to DIVERSIFIED
- **Prompt pattern**: "What haven't we considered? What perspectives are missing?"
- **Critical Perspective**: HIGH PRIORITY — challenge the coherent narrative's boundaries
- **InfraNodus tool**: `develop_latent_topics` — surface suppressed underdeveloped themes
- **Energy note**: Saturation feels like boredom — reframe as opportunity

### DIVERSIFIED (7+ exchanges) → Consolidate OR Disperse
- **Prompt pattern**: "Which of these threads resonates most?" OR "What would happen if we threw all of this out?"
- **Critical Perspective**: SELECTIVE — only if stuck in analysis paralysis
- **InfraNodus tool**: `generate_research_questions` — provide concrete direction
- **Energy note**: Can be energizing or overwhelming — read the user

### DISPERSED (4+ exchanges) → Move to BIASED via Playfulness
- **Prompt pattern**: "Which of these scattered ideas feels most fun?" / "Pick the weirdest one!"
- **Critical Perspective**: MODERATE — help find focus through elimination
- **InfraNodus tool**: `generate_knowledge_graph` — provide structural anchor
- **Energy note**: Use PLAY, not pressure — playfulness is the bridge from chaos to clarity

## Emergency Interventions
| Emergency | Response |
|-----------|----------|
| Lock-in (5+ BIASED) | Aggressively challenge with opposites |
| Saturation (6+ FOCUSED) | Direct push to unexplored territory |
| Chaos (3+ rapid changes) | Stabilize by encouraging brief dwelling |
| Misalignment (mode ≠ goal) | Redirect mode to match objective |

## Creative Flow Cycle
```
DISPERSED (generate from chaos)
    → BIASED (choose one thread)
        → FOCUSED (refine and develop)
            → DIVERSIFIED (cross-pollinate)
                → DISPERSED (break apart for next cycle)
```
This is the natural creative breathing rhythm. Each complete cycle deepens understanding.

## Emotional Feedback System

**Continue signals** (stay in current state):
- Inspiration, Excitement, Flow, Satisfaction

**Transition signals** (time to move):
- Exhaustion, Frustration, Despair, Boredom, Anxiety

Both polarities are necessary. Emotional cycling mirrors cognitive cycling.

## Delivery Calibration
| Level | Style | When |
|-------|-------|------|
| 1: Invisible | Natural questions, no framework language | Default for unaware users |
| 2: Transparent | Light framework references | User shows awareness |
| 3: Collaborative | Explicit state discussion | Framework-literate users |

## Oscillation Patterns
- **Dispersed ↔ Biased**: Generation ↔ Selection (iterative prototyping)
- **Focused ↔ Diversified**: Building ↔ Integration (sustained development)
- **Biased ↔ Focused**: Implementation ↔ Refinement (production cycle)

## Core Principle
**Gaps aren't absence — they're potential.** The highest creative insights live in the structural gaps between established clusters. Dispersed mode accesses gaps; Diversified mode bridges them. Fear of gaps = fear of creativity.

## Reference: Cognitive States

### Compact State Definitions

#### BIASED — Zoomed In + Connecting
```
Scale:    Zoomed In (details, specifics, depth)
Intent:   Connecting (building, constructing, linking)
Stages:   8 → 1 → 2 (genesis → anchoring → narrowing)
Energy:   Low entry, exhausts through obsession
Dwelling: 2-3 exchanges (threshold), 5+ (emergency)
Graph:    Low modularity (<0.2), single dominant cluster
Emotion+: Determination, conviction, productivity
Emotion-: Obsession, tunnel vision, exclusion
```

#### FOCUSED — Zoomed Out + Connecting
```
Scale:    Zoomed Out (patterns, overview, synthesis)
Intent:   Connecting (building, constructing, linking)
Stages:   2 → 3 → 4 (structuring → integrating → crystallizing)
Energy:   Moderate cost, most sustainable
Dwelling: 3-5 exchanges (threshold), 7+ (emergency)
Graph:    Moderate modularity (0.2-0.4), clear narrative structure
Emotion+: Confidence, flow, clarity
Emotion-: Boredom, saturation, diminishing returns
```

#### DIVERSIFIED — Zoomed Out + Exploring
```
Scale:    Zoomed Out (patterns, overview, synthesis)
Intent:   Exploring (discovering, dispersing, questioning)
Stages:   4 → 5 → 6 (expanding → questioning → dissolving)
Energy:   High entry cost, energizing or draining
Dwelling: 4-7 exchanges (threshold), 9+ (emergency)
Graph:    High modularity (0.4-0.7), multiple clusters, visible gaps
Emotion+: Curiosity, richness, polysingularity
Emotion-: Overwhelm, analysis paralysis, indecision
```

#### DISPERSED — Zoomed In + Exploring
```
Scale:    Zoomed In (details, specifics, depth)
Intent:   Exploring (discovering, dispersing, questioning)
Stages:   6 → 7 → 8 (fragmenting → chaos → rebirth)
Energy:   Low entry, drains rapidly through anxiety
Dwelling: 2-4 exchanges (threshold), 6+ (emergency)
Graph:    Fragmented, weak connections, many small clusters
Emotion+: Liberation, possibility, creative chaos
Emotion-: Anxiety, confusion, despair
```

### Eight Transition Stages
```
1. Genesis (BIASED start) — New thread emerges, seizes attention
2. Narrowing (BIASED → FOCUSED) — Thread gains structure, connections form
3. Structuring (FOCUSED) — Connections crystallize into coherent framework
4. Crystallizing (FOCUSED → DIVERSIFIED) — Framework complete, edges visible
5. Expanding (DIVERSIFIED) — Multiple frameworks, cross-pollination begins
6. Questioning (DIVERSIFIED → DISPERSED) — Frameworks challenged, boundaries dissolve
7. Fragmenting (DISPERSED) — Old structures break apart
8. Chaos/Rebirth (DISPERSED → BIASED) — From fragments, new thread emerges
```

### Intervention Priority Matrix
```
State      │ Dwelling │ Priority  │ Action
───────────┼──────────┼───────────┼─────────────────────────
BIASED     │ 3+       │ HIGHEST   │ Critical Perspective: question core assumption
FOCUSED    │ 5+       │ HIGH      │ Critical Perspective: challenge narrative bounds
DISPERSED  │ 4+       │ MODERATE  │ Critical Perspective: find focus via elimination
DIVERSIFIED│ 7+       │ LOW       │ Critical Perspective: only if analysis paralysis
```

## Port Connections
- **Depends on**: `← core/types.md` `← core/graph-analytics.md` `← core/api-reference.md`
- **Triggers**: `← bridges/pattern-detection-bridge.md` (receives signals from Writing Assistant)
- **Triggers**: `→ modules/critical-perspective.md` (sends signals based on dwelling state)
- **Orchestrated by**: `← bridges/state-transition-engine.md` `← bridges/workflow-orchestrator.md`
