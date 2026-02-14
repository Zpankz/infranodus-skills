# Text Processing & NLP Patterns

> **Layer**: 1 | **Dependencies**: `core/types.md` | **Dependents**: `modules/writing-assistant`, `modules/content-analysis`, `bridges/pattern-detection-bridge`
> **Tags**: `#core` `#nlp` `#text` `#processing` `#neural`

## Entity Detection Modes

| Mode | Behavior | Use Case |
|------|----------|----------|
| `none` | Standard NLP — extract keywords, bigrams, concepts | General text analysis |
| `detectEntities` | Hybrid — extract named entities alongside keywords | Mixed content with proper nouns |
| `extractEntitiesOnly` | Only formal entities (names, organizations, concepts) | Ontology generation, entity mapping |

## Text Input Patterns

### Wikilink Syntax for Entity Marking
```
[[Entity Name]] connects to [[Another Entity]] through specific relation
```
- Double brackets signal explicit entity boundaries
- Processed as hashtags internally (treated as topic markers)
- Enable precise entity extraction without NLP ambiguity
- Used in: ontology creation, memory storage, knowledge graph input

### Statement Segmentation
Text is decomposed into atomic statements:
- Each statement = one proposition or assertion
- Statements retain: content, categories, hashtags, community assignment
- Chronological ordering preserved for temporal analysis
- Top statements per cluster represent the cluster's core meaning

### Text Condensing (from Obsidian Plugin)
Before analysis, text is cleaned:
1. Strip markdown formatting (headers, bold, italic)
2. Remove wiki-link brackets (keep inner text)
3. Strip LaTeX expressions
4. Remove images and tables
5. Normalize whitespace
Result: plain text suitable for NLP processing

### Code Block Compression (from VSCode Extension)
For source code analysis:
1. JavaScript/TypeScript: Collapse `{...}` blocks to single lines
2. Python: Collapse indented blocks after `:` to single lines
3. Other: Pass through unchanged
Purpose: Reduce noise while preserving structural keywords

## Content Extraction from URLs

### URL-to-Text Pipeline
```
URL → /convert/url API endpoint
  → Parse response:
     - title: string
     - headerTags: string[] (h1-h6)
     - linkTags: string[] (anchor text)
     - text: string (full extracted text)
  → Validate: ≥20 letters, sufficient whitespace
  → Retry with proxy if initial extraction fails
```

### Content Extraction Modes
| Mode | Returns | Use Case |
|------|---------|----------|
| `default` | Full extracted text | Comprehensive analysis |
| `headerTags` | Only h1-h6 content | Structural/SEO analysis |
| `linkTags` | Only anchor text | Link relationship analysis |

## Pattern Detection System

### Grammatical Patterns as Cognitive Signals
| Pattern | Detection Method | Cognitive Signal | Suggested Action |
|---------|-----------------|------------------|-----------------|
| Repetitive sentence structures | Sentence template matching | Bias/fixation | Diversify → Cognitive Variability |
| Error clustering | Error density per section | Unclear thinking | Develop → Content Analysis tools |
| Missing transitions | Gap between paragraph topics | Structural gaps | Bridge → Ontology Creator |
| Tense inconsistency | Verb tense tracking | Temporal imbalance | Ground → perspective shift |
| Pronoun ambiguity | Unresolved reference detection | Undefined concepts | Name → explicit entity marking |
| Passive voice clustering | Voice ratio analysis | Agency gaps | Strengthen → active argumentation |

### Punctuation Rhythm Analysis
| Pattern | Cognitive State Indicator |
|---------|--------------------------|
| Short sentences, frequent periods | Drilling down — possibly obsessive (BIASED) |
| Long flowing compound sentences | Exploring/connecting (FOCUSED) |
| Question mark clusters | Dispersed/exploratory thinking (DISPERSED) |
| Em-dash / parenthetical density | Holding multiple threads (DIVERSIFIED) |
| Exclamation density | Emotional activation (transition signal) |

### Structural Pattern Detection
| Pattern | Implication | Action |
|---------|------------|--------|
| Repetitive paragraph length | Mechanical writing | Vary rhythm |
| All paragraphs same structure | Template-driven | Break pattern |
| No cross-references | Disconnected sections | Add bridges |
| Single-topic dominance | Hub-and-spoke | Distribute |

## AI-Detection Avoidance Rules

### Red Flags to Never Generate
- Transitions: "Moreover", "Furthermore", "In conclusion", "Additionally"
- Hedging: "It's important to note", "It's worth mentioning", "Interestingly"
- Formulaic: "In today's world", "As we've seen", "Let's delve into"
- Corporate: "leverage", "synergy", "paradigm shift", "holistic approach"
- Enthusiasm: "Absolutely!", "Great question!", "Wonderful insight!"
- Structure: Perfect parallel constructions, uniform sentence length

### Natural Writing Markers
- Varied sentence length (mix short punchy with longer flowing)
- Active voice dominant
- Specific over generic (concrete examples over abstractions)
- Conversational connectors ("but", "and", "so", "though")
- Author-specific quirks preserved (creative punctuation, idiosyncratic style)

## Port Connections
- **Depends on**: `← core/types.md`
- **Consumed by**: `→ modules/writing-assistant.md` `→ modules/content-analysis.md` `→ bridges/pattern-detection-bridge.md`
- **Referenced by**: `→ resources/ai-naturalness-rules.md`
