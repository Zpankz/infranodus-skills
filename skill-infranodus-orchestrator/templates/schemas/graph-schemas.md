# Graph Input/Output Schemas

> **Layer**: 5 | **Dependencies**: `core/types.md`, `core/api-reference.md`
> **Tags**: `#template` `#schema` `#reference` `#symbolic`

## Common Input Parameters

### Text/URL Input (shared across most tools)
```
text: string           # Direct text input (supports [[wikilinks]])
url: string            # URL to analyze (alternative to text)
-- At least one of text/url is required --
```

### Graph Analysis Options
```
includeStatements: boolean    # Return individual statements (default: false)
includeGraph: boolean         # Return raw graph structure (default: false)
addNodesAndEdges: boolean     # Return node/edge arrays (default: false)
includeGraphSummary: boolean  # Include AI summary (default: true)
```

### Entity Detection
```
modifyAnalyzedText:
  "none"                # Standard NLP keyword extraction
  "detectEntities"      # Mix entities and keywords
  "extractEntitiesOnly" # Only formal entities
```

### AI Model Selection
```
modelToUse:
  "claude-opus-4.1" | "claude-opus-4.5" | "claude-sonnet-4" | "claude-sonnet-4.5"
  "gemini-2.5-pro" | "gemini-2.5-flash" | "gemini-2.5-flash-lite"
  "grok-4.1-fast-non-reasoning" | "grok-4.1-fast-reasoning"
  "gpt-4o" | "gpt-4o-mini" | "gpt-5" | "gpt-5-mini"
```

### Gap Analysis
```
gapDepth: number          # Depth of gap analysis (0 = default)
useSeveralGaps: boolean   # Extend to multiple gaps
```

### Localization
```
importLanguage: "EN"|"DE"|"FR"|"ES"|"IT"|"PT"|"RU"|"CN"|"JP"|"NL"|"TW"|"KO"|"AR"|"HE"
importCountry: "US"|"GB"|"CA"|"AU"|"DE"|"FR"|"ES"|"IT"|"NL"|"BE"|"AT"|"CH"|"SE"|"NO"|
               "DK"|"FI"|"PT"|"BR"|"MX"|"AR"|"CL"|"CO"|"JP"|"CN"|"TW"|"KR"|"IN"|"RU"|
               "IL"|"AE"|"SA"|"ZA"|"NG"|"KE"|"EG"
```

### Content Extraction (for URLs)
```
contentToExtract:
  default              # Full page text
  "headerTags"         # H1-H6 content only
  "linkTags"           # Anchor text only
useProxy: boolean      # Proxy for blocked URLs
```

### Text Processing
```
partOfSpeechToProcess:
  "HASHTAGS_AND_WORDS"     # Process both [[wikilinks]] and regular words
  "HASHTAGS_ONLY"          # Only process [[wikilinks]]
  "WORDS_IF_NO_HASHTAGS"   # Words only if no [[wikilinks]] present

doubleSquarebracketsProcessing:
  "PROCESS_AS_HASHTAGS"    # Treat [[wikilinks]] as topic markers
  "EXCLUDE"                # Ignore [[wikilinks]]

mentionsProcessing:
  "CONNECT_TO_ALL_CONCEPTS" # @mentions connect to all co-occurring concepts
```

## Standard Output Schemas

### KnowledgeGraphOutput
```
statistics:
  modularity: number
  clusterCount: number
  nodeCount: number
  edgeCount: number
  diversityStats: { diversity_score, too_focused_on_top_nodes, too_focused_on_top_clusters,
                    top_nodes_entropy, total_clusters, fair_influence_by_cluster }
graphSummary: string
contentGaps: string[]
mainTopicalClusters: string[]
mainConcepts: string[]
topInfluentialNodes: [{ node, degree, bc }]
conceptualGateways: string[]
topRelations: string[]
topBigrams: string[]
statements: Statement[] (if includeStatements)
knowledgeGraph: GraphStructure (if includeGraph)
knowledgeGraphByCluster: object (if includeGraph)
```

### GapsOutput
```
contentGaps: string[]
```

### TopicsOutput
```
topicalClusters: string[]
```

### ResearchQuestionsOutput
```
questions: string[]
```

### ResearchIdeasOutput
```
ideas: string[]
```

### LatentTopicsOutput
```
ideas: string[]
mainTopics: string[]
latentTopicsToDevelop: string[]
```

### LatentConceptsOutput
```
ideas: string[]
latentConceptsToDevelop: string[]
latentConceptsRelations: string[]
```

### GraphRagOutput
```
retrievedStatements: [{ content, categories, topStatementCommunity, similarityScore }]
graphSummary: string
contentGaps: string[]
mainTopicalClusters: string[]
topInfluentialNodes: [{ node, degree, bc }]
```

### SearchOutput
```
results: [{ id (user:graph:query), title, url }]
```

### FetchOutput
```
id: string
title: string
text: string
url: string
```

### StatementsOutput
```
statements: Statement[]
```

### GraphOverview
```
textOverview: string
```

### Memory Graph Naming
```
graphName: string
  - Maximum 28 characters
  - Lowercase only
  - Dashes for spaces
  - No special characters
  Example: "project-research-notes"
```
