# Chat & Conversational Prompt Templates

> **Layer**: 5 | **Dependencies**: `core/api-reference.md`, `bridges/platform-adapters`
> **Tags**: `#template` `#prompts` `#chat` `#rag`

## RAG Chat Prompt (from Obsidian Plugin)

### User Message Construction
```
{userQuestion}
{optional subPromptPrefix}
<--- answer the question above considering the context & previous conversation we had below --->
{JSON.stringify(statementsWithIds)}
{JSON.stringify(chatHistory)}
each response you provide should be followed with the separator |||| and the ids of the
context statements above where you got the information from in square brackets
```

### Sub-Prompt Prefixes
These can be prepended to the user's question for directive control:
```
"elaborate on this statement:"
"challenge this idea:"
"generate an interesting question:"
"summarize it:"
"check if it's true:"
```

### Response Parsing
```
responseText.split("||||")
→ [0]: AI response text
→ [1]: Reference IDs like "[2][7][15]"

Reference format: [n] where n is the statement ID from the context array
Clicking [n] reveals the source statement for verification
```

## AI Topic Naming Prompt (from Obsidian Plugin)

### Construction
```
promptContext:
  [cluster {community}]: {topStatementContent}
  [cluster {community2}]: {topStatementContent2}

prompt (per cluster):
  { text: "concept1, concept2, concept3", id: clusterId, community: communityId }
```

### Purpose
Generate short, human-readable names for topical clusters identified by graph analysis.

## Cognitive Variability Chat Patterns

### Invisible Transition Prompts
| Transition | Natural Prompt |
|-----------|---------------|
| BIASED → FOCUSED | "How do you see these ideas connecting to the bigger picture?" |
| FOCUSED → DIVERSIFIED | "What perspectives might we be missing here?" |
| DIVERSIFIED → FOCUSED | "Which of these threads resonates most with your goal?" |
| DISPERSED → BIASED | "What's the one idea here that feels most alive to you?" |

### Playfulness Prompts (Dispersed → Biased)
```
"If you had to bet everything on one of these scattered ideas, which would it be?"
"Which of these is the weirdest? Let's start there."
"Pick the one that makes you slightly uncomfortable — that's usually the good one."
```

### Critical Perspective Prompts
```
"What assumption is this whole line of thinking resting on?"
"If someone from a completely different field read this, what would surprise them?"
"What are we NOT talking about that might matter more?"
```

## Contextual DOT Graph for Chat

### Per-Cluster Format
```dot
[cluster {id}: {aiName}]
concept1 -- concept2
concept2 -- concept3
concept3 -- concept4
inter-cluster: concept2 -- concept_from_other_cluster
```

### Filtered by Selection
When user selects specific nodes/topics, filter DOT graph to show only:
1. Lines where ALL selected nodes appear
2. Lines where at least one connected node appears
3. Inter-cluster connector lines for selected clusters
