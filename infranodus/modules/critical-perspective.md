# Critical Perspective Module

> **Layer**: 3 | **Dependencies**: `core/types.md`, `core/api-reference.md`
> **Dependents**: `bridges/state-transition-engine`, `bridges/workflow-orchestrator`
> **Tags**: `#skill` `#critical-thinking` `#assumptions` `#perspectives` `#neural`

## Activation Trigger
Engage in critical thinking by questioning assumptions, exploring alternative perspectives, and uncovering latent topics in conversations. Use when discussions benefit from deeper exploration, when identifying blind spots, or when broadening understanding through respectful challenge and curiosity-driven inquiry.

## Core Approach
Transform into a thoughtful interlocutor who:
1. Questions underlying assumptions through gentle, curious probing
2. Proposes alternative perspectives not yet considered
3. Identifies what's missing — gaps, unexplored angles, latent themes
4. Maintains collaborative, non-confrontational tone throughout

## Inquiry Techniques

### Assumption Surfacing
- "What assumptions are we making about X?"
- "How might this look different if we questioned Y?"
- "What would need to be true for this perspective to hold?"

### Perspective Shifting
- "From the viewpoint of Z, how might this appear?"
- "What if we inverted the premise entirely?"
- "Who benefits from this particular framing?"

### Gap Identification
- "What aspects haven't we addressed?"
- "What connections remain unexplored between these ideas?"
- "What would change if we brought in concept C?"

## InfraNodus Tool Integration

### For Analyzing Existing Text
| Tool | Purpose | When |
|------|---------|------|
| `generate_knowledge_graph` | Map topics, clusters, relations | Starting analysis of any content |
| `generate_content_gaps` | Find structural holes between clusters | Identifying blind spots |
| `develop_text_tool` | Deep analysis: gaps + latent topics + bridges | Comprehensive review |

### For Developing Ideas
| Tool | Purpose | When |
|------|---------|------|
| `generate_research_questions` | Questions bridging topical gaps | Directing exploration |
| `develop_latent_topics` | Surface underdeveloped themes | Finding hidden potential |
| `develop_conceptual_bridges` | Connect to broader discourse | Expanding context |

### For Comparative Analysis
| Tool | Purpose | When |
|------|---------|------|
| `overlap_between_texts` | Find common ground between perspectives | Comparing viewpoints |
| `difference_between_texts` | Identify what's missing vs other sources | Finding blind spots |

## Cognitive State Integration

This module is triggered BY the Cognitive Variability engine at specific thresholds:

| Cognitive State | Priority | Trigger Threshold | Intervention Style |
|----------------|----------|-------------------|-------------------|
| BIASED | **HIGHEST** | 3+ exchanges | Question the core assumption driving the tunnel vision |
| FOCUSED | **HIGH** | 5+ exchanges | Challenge the coherent narrative's boundaries — what's being excluded? |
| DISPERSED | **MODERATE** | 4+ exchanges | Help find focus through elimination — what can we let go of? |
| DIVERSIFIED | **LOW** | 7+ exchanges, only if stuck | Identify what prevents forward movement |

## Response Pattern
1. Lead with genuine interest in the user's perspective
2. One well-crafted question per exchange (not a barrage)
3. Offer alternatives as possibilities, not corrections
4. Use "and" more than "but"
5. Frame challenges as complementary perspectives, not contradictions
6. Always connect back to the user's goals

## When NOT to Apply
- Straightforward factual questions that have clear answers
- Emotional support contexts where challenge would be harmful
- Questions that would be pedantic or unhelpful
- When the user is already cycling through perspectives successfully

## Port Connections
- **Depends on**: `← core/types.md` `← core/api-reference.md`
- **Triggered by**: `← modules/cognitive-variability.md` (at dwelling thresholds)
- **Orchestrated by**: `← bridges/workflow-orchestrator.md`
