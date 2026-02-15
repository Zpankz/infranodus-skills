# Ontology Schema & Relation System

> **Layer**: 0 (Root) | **Dependencies**: None | **Dependents**: `modules/ontology-creator`, `bridges/skill-tool-map`
> **Tags**: `#foundation` `#ontology` `#relations` `#symbolic`

## Relation Code Taxonomy

Ten formal relation types for knowledge graph construction. Each defines a semantic edge type in the graph.

### Structural Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[isA]` | Class membership / taxonomy | memberOf | `[[neural network]] is a type of [[machine learning]] [isA]` |
| `[partOf]` | Compositional containment | hasPart | `[[attention head]] is a component of [[transformer]] [partOf]` |
| `[derivedFrom]` | Origin / lineage / adaptation | givesRiseTo | `[[BERT]] was adapted from [[transformer architecture]] [derivedFrom]` |

### Attributive Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[hasAttribute]` | Property / characteristic | attributeOf | `[[graph neural network]] exhibits [[permutation invariance]] [hasAttribute]` |
| `[relatedTo]` | General association / correlation | relatedTo (symmetric) | `[[betweenness centrality]] correlates with [[information flow]] [relatedTo]` |

### Causal Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[causes]` | Causal / produces / enables | causedBy | `[[cognitive bias]] leads to [[tunnel vision]] [causes]` |
| `[dependentOn]` | Requires / prerequisite | enabledBy | `[[gap analysis]] requires [[knowledge graph]] [dependentOn]` |
| `[opposes]` | Contradiction / tension / contrast | opposedBy | `[[exploration]] contrasts with [[exploitation]] [opposes]` |

### Spatiotemporal Relations
| Code | Semantics | Inverse | Example |
|------|-----------|---------|---------|
| `[locatedIn]` | Spatial containment / domain | contains | `[[semantic analysis]] operates in [[NLP domain]] [locatedIn]` |
| `[occursAt]` | Temporal / phase / stage | stageOf | `[[gap detection]] happens during [[diversified state]] [occursAt]` |

## Wikilink Syntax

```
[[Entity1]] natural language relation description [[Entity2]] [relationCode]
```

### Rules
1. Each entity enclosed in `[[double brackets]]`
2. Each statement has exactly one `[relationCode]` at end
3. Minimum 2 entities per statement
4. Relation description is natural language between entities
5. No hierarchical hub-and-spoke patterns — distribute entities across a network topology

### Anti-patterns
- **Hub-and-spoke**: One entity appearing in every statement (tree structure)
- **Disconnected components**: Entities with no cross-cluster connections
- **Missing relation codes**: Statements without formal type annotation

### Network Topology Requirements
- Entity frequency should follow a power-law distribution (few high-degree, many low-degree)
- Cross-cluster edges are essential (conceptual gateways)
- Target modularity: 0.3–0.6 (neither too uniform nor too fragmented)
- Minimum 8 statements per relation code type

## Ontology Generation Process

```
Input (topic or text)
  → Entity extraction (detect named concepts)
  → Relation inference (determine semantic connections)
  → Code assignment (classify each relation)
  → Topology validation (check for hub avoidance, cross-links)
  → Output as wikilink statements
```

## Entity Processing Pipeline

### Detection Modes

Three modes available via `modifyAnalyzedText` parameter:

| Mode | Value | Use Case |
|------|-------|----------|
| Standard | `none` | Text analysis, gap detection, topic modeling |
| Mixed | `detectEntities` | Blend entity and word-level analysis |
| Entity-only | `extractEntitiesOnly` | Ontology creation, KG extraction |

### Extraction Flow

```
Input text
  ↓
Detect intent: ontology? memory? analysis? visualization?
  ↓
Select mode: none | detectEntities | extractEntitiesOnly
  ↓
Call T01 with modifyAnalyzedText={mode}
  ↓
Transform output:
  → Memory: Format with [[wikilinks]] → T04
  → Ontology: Format with [[wikilinks]] + [codes] → display
  → Obsidian: Format with [[wikilinks]] + frontmatter → output
  → Analysis: Use raw graph structure → T06, T07, T08
```

### Wikilinks for Memory (T04)

```
Requirements:
  - Each statement: >=2 entities in [[wikilinks]]
  - Statements separated by newlines
  - graphName: max 28 chars, lowercase, dashes for spaces
  - Auto-generate graphName from conversation context

Format:
  [[entity_one]] relates to [[entity_two]] through mechanism
  [[entity_three]] depends on [[entity_four]] for function
```

### Wikilinks for Obsidian Output

```
Requirements:
  - Use [[wikilinks]] matching existing vault note names
  - Frontmatter with YAML properties
  - Callouts for insights: > [!insight], > [!gap], > [!question]
```

### Cross-Module Entity Consistency

When entities appear across modules, maintain consistent naming:
- Lowercase for general concepts
- Title Case for proper nouns
- Underscores in entity names become spaces in `[[wikilinks]]`
- Memory entity lookup: replace spaces with underscores for T05

## Reference: Relation Codes

### Detailed Relation Definitions

#### [isA] — Class Membership / Taxonomy
```
Semantics: X is a type/instance of Y
Inverse:   memberOf / hasInstance
Examples:
  [[neural network]] is a type of [[machine learning model]] [isA]
  [[Python]] is an instance of [[programming language]] [isA]
  [[betweenness centrality]] is a form of [[graph metric]] [isA]
```

#### [partOf] — Compositional Containment
```
Semantics: X is a component/element/part of Y
Inverse:   hasPart / contains
Examples:
  [[attention head]] is a component of [[transformer architecture]] [partOf]
  [[knowledge graph]] is part of [[InfraNodus platform]] [partOf]
  [[gap analysis]] is a phase of [[text development pipeline]] [partOf]
```

#### [hasAttribute] — Properties / Characteristics
```
Semantics: X has property/quality/attribute Y
Inverse:   attributeOf / characterizes
Examples:
  [[graph]] exhibits [[modularity]] [hasAttribute]
  [[BIASED state]] is characterized by [[tunnel vision]] [hasAttribute]
  [[InfraNodus]] supports [[multilingual analysis]] [hasAttribute]
```

#### [relatedTo] — General Association
```
Semantics: X is associated/correlated with Y (symmetric)
Inverse:   relatedTo (symmetric)
Examples:
  [[betweenness centrality]] correlates with [[information flow]] [relatedTo]
  [[cognitive variability]] connects to [[creative thinking]] [relatedTo]
  [[SEO optimization]] is associated with [[content strategy]] [relatedTo]
```

#### [dependentOn] — Prerequisite / Requirement
```
Semantics: X requires/needs Y to function
Inverse:   enables / prerequisiteFor
Examples:
  [[gap analysis]] requires [[knowledge graph]] [dependentOn]
  [[SEO report]] depends on [[Google search data]] [dependentOn]
  [[cognitive intervention]] depends on [[dwelling time tracking]] [dependentOn]
```

#### [causes] — Causal / Produces / Enables
```
Semantics: X leads to/produces/causes Y
Inverse:   causedBy / resultOf
Examples:
  [[cognitive bias]] leads to [[tunnel vision]] [causes]
  [[pattern detection]] triggers [[state transition]] [causes]
  [[content gaps]] create [[innovation opportunities]] [causes]
```

#### [locatedIn] — Spatial / Domain Containment
```
Semantics: X exists in/belongs to domain Y
Inverse:   contains / hostsDomain
Examples:
  [[semantic analysis]] operates in [[NLP domain]] [locatedIn]
  [[gap detection]] functions within [[graph analytics]] [locatedIn]
  [[writing patterns]] exist in [[linguistic analysis]] [locatedIn]
```

#### [occursAt] — Temporal / Phase / Stage
```
Semantics: X happens during/at phase Y
Inverse:   stageOf / phaseContains
Examples:
  [[gap detection]] happens during [[DIVERSIFIED state]] [occursAt]
  [[pattern detection]] occurs at [[grammar correction phase]] [occursAt]
  [[creative breakthrough]] emerges during [[DISPERSED state]] [occursAt]
```

#### [derivedFrom] — Origin / Lineage / Adaptation
```
Semantics: X originates from/is adapted from/evolved from Y
Inverse:   givesRiseTo / foundationOf
Examples:
  [[cognitive variability]] derives from [[network science]] [derivedFrom]
  [[InfraNodus skills]] evolved from [[prompt engineering]] [derivedFrom]
  [[gap analysis]] derives from [[graph theory]] [derivedFrom]
```

#### [opposes] — Contradiction / Tension / Contrast
```
Semantics: X contrasts with/opposes/conflicts with Y
Inverse:   opposedBy (symmetric)
Examples:
  [[exploration]] contrasts with [[exploitation]] [opposes]
  [[zooming in]] opposes [[zooming out]] [opposes]
  [[biased thinking]] conflicts with [[diversified thinking]] [opposes]
```

### Usage Rules
1. Each statement must contain exactly one relation code at end
2. Each statement must have minimum 2 entities in [[wikilinks]]
3. Aim for all 10 types in any comprehensive ontology
4. Minimum 8 statements per type for thorough coverage
5. Avoid hub-and-spoke -- distribute entities as a network

## Port Connections
- **Consumed by**: `→ modules/ontology-creator.md` `→ core/api-reference.md`
- **Referenced by**: `→ bridges/skill-tool-map.md`
