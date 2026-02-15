# Pattern Detection Bridge — Writing → Cognitive State Pipeline

> **Layer**: 4 (Bridge) | **Dependencies**: `modules/writing-assistant`, `modules/cognitive-variability`, `core/text-processing.md`
> **Dependents**: `bridges/state-transition-engine`, `bridges/workflow-orchestrator`
> **Tags**: `#bridge` `#hyperedge` `#patterns` `#sensory` `#neural`

## Purpose
This bridge connects the Writing Assistant's pattern detection (sensory system) to the Cognitive Variability engine's state management. It defines the mapping from observable textual patterns to cognitive state diagnosis and intervention triggers.

## Pipeline
```
User Text
  → Writing Assistant (grammar correction + pattern detection)
    → Pattern Detection Bridge (this file)
      → State Diagnosis
        → Cognitive Variability (intervention)
          → Critical Perspective (if threshold met)
```

## Pattern → State Mapping

### Grammar Patterns
| Pattern | Signal | Diagnosed State | Confidence | Action |
|---------|--------|----------------|------------|--------|
| Repetitive sentence structures | Cognitive fixation | BIASED (or entering BIASED) | High | Trigger diversification |
| Error clustering in specific sections | Unclear thinking | Transitioning (unstable) | Medium | Develop those sections |
| Missing transitions between paragraphs | Structural gaps | DIVERSIFIED (fragmented) | Medium | Bridge ideas |
| Tense inconsistency | Temporal confusion | DISPERSED (scattered) | Medium | Ground in perspective |
| Pronoun ambiguity | Undefined concepts | BIASED (assumptions hidden) | Low | Surface assumptions |
| Passive voice clustering | Agency avoidance | FOCUSED (avoiding commitment) | Low | Strengthen stance |

### Punctuation Patterns
| Pattern | Signal | Diagnosed State | Confidence |
|---------|--------|----------------|------------|
| Short sentences, many periods | Drilling down | BIASED | High |
| Long compound sentences | Connecting ideas | FOCUSED | High |
| Question mark clusters | Searching/exploring | DISPERSED | Medium |
| Em-dash / parenthetical density | Holding multiple threads | DIVERSIFIED | Medium |
| Exclamation density | Emotional activation | Transition imminent | Low |

### Structural Patterns
| Pattern | Signal | Diagnosed State | Confidence |
|---------|--------|----------------|------------|
| Single-topic dominance (>60% of content) | Tunnel vision | BIASED | High |
| Uniform paragraph length | Mechanical output | FOCUSED (saturated) | Medium |
| No cross-references between sections | Fragmentation | DIVERSIFIED (no bridges) | Medium |
| Scattered short fragments | Chaos | DISPERSED | High |

## Confidence-Weighted Decision

Multiple patterns compound confidence:
```
Single pattern match: Suggest (don't intervene)
Two pattern match: Monitor + prepare intervention
Three+ pattern match: Intervene — trigger Cognitive Variability
```

## Handoff Protocol

### From Writing Assistant → Cognitive Variability
When pattern detection triggers an intervention:
1. Complete the grammar correction (don't interrupt the primary task)
2. Note detected patterns and their cognitive implications
3. After delivering corrected text, introduce the cognitive observation
4. Use appropriate delivery calibration level (invisible/transparent/collaborative)

### Pattern Detection → Critical Perspective
Certain patterns bypass Cognitive Variability and trigger Critical Perspective directly:
| Pattern | Direct Critical Trigger |
|---------|----------------------|
| Repeated assertion without evidence | Question the assertion's basis |
| Same conclusion reached from different angles | Challenge the convergent framing |
| All examples from single domain | Suggest cross-domain perspectives |
| Consistent avoidance of specific topic | Surface the avoided topic |

## Integration with InfraNodus Tools

When pattern detection needs data-driven confirmation:
| Detection | Tool to Confirm | Decision |
|-----------|----------------|----------|
| Single-topic dominance suspected | `generate_knowledge_graph` → check modularity | If modularity < 0.2 → confirm BIASED |
| Structural gaps detected | `generate_content_gaps` → enumerate gaps | If significant gaps → confirm DIVERSIFIED |
| Error clustering in sections | `develop_text_tool` → deep analysis | Identify which sections need development |
| Topical imbalance | `generate_topical_clusters` → cluster distribution | If one cluster > 60% → confirm imbalance |
