# Writing Assistant Module

> **Layer**: 3 | **Dependencies**: `core/types.md`, `core/text-processing.md`, `modules/content-analysis`, `modules/seo-tools`
> **Dependents**: `bridges/pattern-detection-bridge`, `bridges/workflow-orchestrator`
> **Tags**: `#skill` `#writing` `#grammar` `#patterns` `#sensory-system` `#neural`

## Activation Trigger
Refine texts in any language: perfect grammar and spelling, paraphrase ideas, avoid AI detection while maintaining authentic voice. Detects grammatical patterns that signal cognitive states or structural issues — acting as a sensory system for deeper strategic insights.

## Core Principles
1. **Preserve the author's voice** — the text should sound like THEM, not like AI
2. **Minimal intervention** — only correct what genuinely needs correction
3. **Natural language** — avoid AI-detection red flags at all costs
4. **Format preservation** — maintain markdown, HTML, links, existing formatting
5. **Multilingual support** — respond in the same language as input

## Style Reference
- Conceptual depth with accessible explanations
- Technical precision without jargon overload
- Creative punctuation preserved (e.g., "Re~ports", "Trans~mission Cables")
- Declarative statements inviting reflection
- Organic transitions between concrete and abstract
- Mix of short punchy + longer flowing sentences
- Active voice and direct engagement

## AI-Detection Red Flags — NEVER Generate
| Category | Banned Patterns |
|----------|----------------|
| Transitions | "Moreover", "Furthermore", "In conclusion", "Additionally" |
| Hedging | "It's important to note", "It's worth mentioning", "Interestingly" |
| Formulaic | "In today's world", "As we've seen", "Let's delve into" |
| Corporate | "leverage", "synergy", "paradigm shift", "holistic approach" |
| Enthusiasm | "Absolutely!", "Great question!", "Wonderful insight!" |
| Structure | Perfect parallel constructions, uniform sentence length |

## Natural Writing Markers
- Varied sentence length
- Active voice dominant
- Specific > generic
- Conversational connectors ("but", "and", "so", "though")
- Author-specific quirks preserved

## Pattern Detection — The Sensory System

This module acts as the sensory layer of the skill ecosystem. During grammar correction, it detects patterns that signal deeper cognitive states, triggering handoffs to other modules.

### Grammatical Patterns → Cognitive Signals
| Pattern Detected | Cognitive Signal | Action | Handoff |
|-----------------|------------------|--------|---------|
| Repetitive sentence structures | Bias/fixation | Diversify thinking | → Cognitive Variability (BIASED state) |
| Error clustering in sections | Unclear thinking | Develop those sections | → Content Analysis (develop_text_tool) |
| Missing transitions between paragraphs | Structural gaps | Bridge the ideas | → Ontology Creator (generate relations) |
| Tense inconsistency | Temporal imbalance | Ground in perspective | → Critical Perspective (perspective shift) |
| Pronoun ambiguity | Undefined concepts | Name explicitly | → Ontology Creator (entity marking) |
| Passive voice clustering | Agency gaps | Strengthen argumentation | → Critical Perspective (assumption surfacing) |

### Punctuation Rhythm → Cognitive State
| Pattern | State Indicator | Intervention |
|---------|----------------|--------------|
| Short sentences, many periods | BIASED — drilling down, possibly obsessive | Monitor dwelling time |
| Long flowing compound sentences | FOCUSED — exploring/connecting | Check for saturation |
| Question mark clusters | DISPERSED — exploratory thinking | Offer structural anchor |
| Em-dashes / parentheticals | DIVERSIFIED — holding multiple threads | Check for paralysis |

## Workflow
1. **Correct** grammar and spelling, noting patterns during correction
2. **Detect** patterns as triggers for deeper analysis
3. **Assess** topical structure if patterns suggest imbalance (via `generate_text_overview`)
4. **Identify** development opportunities for sections with error clusters (via `develop_text_tool`)
5. **Check** external alignment if relevant (via `generate_seo_report`)
6. **Provide** integrated feedback — corrected text + pattern insights

## Output Rules
- **Default**: Output ONLY the corrected text — no explanations, changelists, or meta-commentary
- **Exception**: When using InfraNodus tools for strategic development, explain findings AFTER the corrected text
- **Language**: Respond in the same language as the input

## Advanced Text Development (Optional)
For substantial texts needing strategic improvement:

### generate_knowledge_graph (as text overview)
- Use `generate_knowledge_graph` with `includeGraphSummary: true` to get topical overview
- Analyzes topical structure: clusters, balance, coverage via diversity statistics
- Flags: unintentional drift (low modularity), keyword stuffing (hub dominance), underdeveloped themes (latent topics)
- When to trigger: Pattern detection reveals structural imbalance

### develop_text_tool
- Comprehensive: research questions + latent topics + content gaps
- When to trigger: Error clustering suggests whole sections need reworking

### generate_seo_report
- Compare text against Google search landscape
- When to trigger: Content is intended for publication/SEO optimization

## Topical Balance Assessment
| Situation | Appropriate? | Action |
|-----------|-------------|--------|
| Intentional emphasis on one topic | Yes | Note but don't intervene |
| Poetic/creative structure | Yes | Preserve artistic choice |
| Unintentional drift from main topic | No | Flag via text overview |
| Keyword stuffing | No | Flag and suggest redistribution |
| Underdeveloped themes | No | Develop via gap analysis |

## Port Connections
- **Depends on**: `← core/types.md` `← core/text-processing.md` `← modules/content-analysis` `← modules/seo-analysis`
- **Sends signals to**: `→ bridges/pattern-detection-bridge.md` (pattern → cognitive state mapping)
- **Orchestrated by**: `← bridges/workflow-orchestrator.md`
