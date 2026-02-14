# Knowledge Graph Pipeline — Workflow Template

> **Layer**: 5 | **Dependencies**: `modules/graph-generation`, `modules/ontology-creator`, `modules/memory-manager`
> **Tags**: `#template` `#workflow` `#pipeline` `#knowledge-graph` `#ontology`

## Ontology Creation Pipeline

### Stage 1: Generate Ontology
```
Module: ontology-creator
Input: topic or text
Process:
  1. Extract entities and concepts
  2. Infer relationships between entities
  3. Classify each relation with [relationCode]
  4. Validate network topology (not tree)
Output: Wikilink-formatted ontology statements
```

### Stage 2: Quality Validation
```
Tool: generate_knowledge_graph
Input: { text: ontology_output }
Check:
  - Modularity 0.3-0.6 (not too uniform, not too fragmented)
  - No single entity in >25% of statements (hub avoidance)
  - Cross-cluster edges present (conceptual gateways)
  - All 10 relation codes represented
  - Diversity statistics healthy
```

### Stage 3: Iterative Refinement
```
If quality check fails:
  1. Identify over-represented entities → redistribute
  2. Identify missing relation types → add
  3. Identify disconnected clusters → add bridges
  4. Regenerate and re-check
Repeat until topology is healthy (typically 1-2 iterations)
```

### Stage 4: Persistence
```
Option A: Save as graph
  Tool: create_knowledge_graph
  Input: { name: "ontology-name", text: ontology_output }

Option B: Save as memory
  Tool: memory_add_relations
  Input: { graphName: "ontology-name", text: ontology_output }

Option C: Output for external use
  Format: code block for direct paste into InfraNodus.com
```

## GraphRAG Chatbot Pipeline (from n8n)

### Stage 1: Knowledge Base Setup
```
1. Create persistent graph from source material
   Tool: create_knowledge_graph
   Input: { name: "knowledge-base", text/url: source_material }

2. Optionally add multiple sources to same graph
   Tool: memory_add_relations (repeated)
```

### Stage 2: Query Processing
```
1. User asks a question
2. Retrieve relevant context
   Tool: retrieve_from_knowledge_base
   Input: { name: "knowledge-base", prompt: user_question }
3. Get: retrieved statements with similarity scores
```

### Stage 3: Response Generation
```
1. Construct response using retrieved statements as context
2. Cite specific statements where relevant
3. Identify gaps in knowledge base for the query
```

## Multi-Source Knowledge Integration (from n8n)

### Google Drive → InfraNodus Pipeline
```
Source: PDF / Document uploads
  → Extract text content
  → Generate knowledge graph per document
  → Merge into unified knowledge base
  → Enable cross-document retrieval
```

### Email → Knowledge Graph Pipeline
```
Source: Gmail / email service
  → Extract email content
  → Generate knowledge graph of email threads
  → Label/categorize based on topical clusters
  → Enable email knowledge retrieval
```

## n8n Equivalent
```
Trigger (Webhook/Gmail/Drive)
  → Extract Content
  → InfraNodus (graphAndStatements, doNotSave=false)
  → Store graph reference
  → Later: InfraNodus (graphAndAdvice, requestMode=search)
  → LLM Response Generation
```
