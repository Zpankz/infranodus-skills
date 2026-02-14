# Relation Codes — Complete Reference

> **Layer**: 5 (Resource) | **Tags**: `#resource` `#reference` `#ontology` `#relations`

## The 10 Relation Types

### 1. [isA] — Class Membership / Taxonomy
```
Semantics: X is a type/instance of Y
Inverse:   memberOf / hasInstance
Examples:
  [[neural network]] is a type of [[machine learning model]] [isA]
  [[Python]] is an instance of [[programming language]] [isA]
  [[betweenness centrality]] is a form of [[graph metric]] [isA]
```

### 2. [partOf] — Compositional Containment
```
Semantics: X is a component/element/part of Y
Inverse:   hasPart / contains
Examples:
  [[attention head]] is a component of [[transformer architecture]] [partOf]
  [[knowledge graph]] is part of [[InfraNodus platform]] [partOf]
  [[gap analysis]] is a phase of [[text development pipeline]] [partOf]
```

### 3. [hasAttribute] — Properties / Characteristics
```
Semantics: X has property/quality/attribute Y
Inverse:   attributeOf / characterizes
Examples:
  [[graph]] exhibits [[modularity]] [hasAttribute]
  [[BIASED state]] is characterized by [[tunnel vision]] [hasAttribute]
  [[InfraNodus]] supports [[multilingual analysis]] [hasAttribute]
```

### 4. [relatedTo] — General Association
```
Semantics: X is associated/correlated with Y (symmetric)
Inverse:   relatedTo (symmetric)
Examples:
  [[betweenness centrality]] correlates with [[information flow]] [relatedTo]
  [[cognitive variability]] connects to [[creative thinking]] [relatedTo]
  [[SEO optimization]] is associated with [[content strategy]] [relatedTo]
```

### 5. [dependentOn] — Prerequisite / Requirement
```
Semantics: X requires/needs Y to function
Inverse:   enables / prerequisiteFor
Examples:
  [[gap analysis]] requires [[knowledge graph]] [dependentOn]
  [[SEO report]] depends on [[Google search data]] [dependentOn]
  [[cognitive intervention]] depends on [[dwelling time tracking]] [dependentOn]
```

### 6. [causes] — Causal / Produces / Enables
```
Semantics: X leads to/produces/causes Y
Inverse:   causedBy / resultOf
Examples:
  [[cognitive bias]] leads to [[tunnel vision]] [causes]
  [[pattern detection]] triggers [[state transition]] [causes]
  [[content gaps]] create [[innovation opportunities]] [causes]
```

### 7. [locatedIn] — Spatial / Domain Containment
```
Semantics: X exists in/belongs to domain Y
Inverse:   contains / hostsDomain
Examples:
  [[semantic analysis]] operates in [[NLP domain]] [locatedIn]
  [[gap detection]] functions within [[graph analytics]] [locatedIn]
  [[writing patterns]] exist in [[linguistic analysis]] [locatedIn]
```

### 8. [occursAt] — Temporal / Phase / Stage
```
Semantics: X happens during/at phase Y
Inverse:   stageOf / phaseContains
Examples:
  [[gap detection]] happens during [[DIVERSIFIED state]] [occursAt]
  [[pattern detection]] occurs at [[grammar correction phase]] [occursAt]
  [[creative breakthrough]] emerges during [[DISPERSED state]] [occursAt]
```

### 9. [derivedFrom] — Origin / Lineage / Adaptation
```
Semantics: X originates from/is adapted from/evolved from Y
Inverse:   givesRiseTo / foundationOf
Examples:
  [[cognitive variability]] derives from [[network science]] [derivedFrom]
  [[InfraNodus skills]] evolved from [[prompt engineering]] [derivedFrom]
  [[gap analysis]] derives from [[graph theory]] [derivedFrom]
```

### 10. [opposes] — Contradiction / Tension / Contrast
```
Semantics: X contrasts with/opposes/conflicts with Y
Inverse:   opposedBy (symmetric)
Examples:
  [[exploration]] contrasts with [[exploitation]] [opposes]
  [[zooming in]] opposes [[zooming out]] [opposes]
  [[biased thinking]] conflicts with [[diversified thinking]] [opposes]
```

## Usage Rules
1. Each statement must contain exactly one relation code at end
2. Each statement must have minimum 2 entities in [[wikilinks]]
3. Aim for all 10 types in any comprehensive ontology
4. Minimum 8 statements per type for thorough coverage
5. Avoid hub-and-spoke — distribute entities as a network
