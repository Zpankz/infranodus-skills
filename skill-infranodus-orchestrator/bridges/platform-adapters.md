# Platform Adapters — Cross-Platform Integration Patterns

> **Layer**: 4 (Bridge) | **Dependencies**: `core/api-reference.md`, `core/text-processing.md`
> **Dependents**: `SKILL.md` (index), `templates/workflows/*`
> **Tags**: `#bridge` `#hyperedge` `#platform` `#adapters` `#symbolic`

## Purpose
This bridge documents platform-specific integration patterns extracted from the Obsidian Plugin, VSCode Extension, and n8n Workflow Templates. These patterns inform how the orchestrator skill should adapt its behavior based on the user's platform context.

## Platform: Obsidian

### Content Processing
```
Single page: [[Wiki Links]] + Concepts (HASHTAGS_AND_WORDS)
Multiple pages: [[Wiki Links]] Only (HASHTAGS_ONLY)
```

### Context Settings
```json
{
  "partOfSpeechToProcess": "HASHTAGS_AND_WORDS",
  "doubleSquarebracketsProcessing": "PROCESS_AS_HASHTAGS",
  "mentionsProcessing": "CONNECT_TO_ALL_CONCEPTS"
}
```

### Key Patterns
- **Backlink integration**: Linked/unlinked mentions enrichment
- **Vault traversal**: Recursive folder reading for multi-file analysis
- **Shadow DOM rendering**: Isolated React UI within Obsidian
- **iframe communication**: PostMessage protocol to `graph.infranodus.com`
- **AI chat with RAG**: Semantic search → context construction → chat response with `||||` separator for references
- **Statement filtering**: By words, hidden words, topic IDs, connected words
- **Export modes**: Manual (URL) or automatic (API save)

### Iframe PostMessage Protocol
```
→ LOAD_JSON        (send graph data)
→ UPDATE_SELECTED_NODES (highlight nodes)
→ UPDATE_REMOVED_NODES  (hide nodes)
→ TOPICS_UPDATE    (send AI topic names)
← READY            (iframe loaded)
← UPDATE_SELECTED_NODES (user selection)
← UPDATE_REMOVED_NODES  (user removal)
← UPDATE_GROUPS    (cluster selection)
← EXTERNAL_ACTION  (AI actions: question, develop, summarize, context, context_gap)
```

### AI Advice Prompt Construction
```
prompt = words + bigrams + chronological statements (or dotGraph per cluster)
promptGraph = DOT graph filtered by topic + inter-cluster connectors
promptContext = per-topic statement blocks with budget allocation:
  maxSizePerTopic = min((maxPromptSize - currentSize) / totalTopics, threshold)
```

## Platform: VSCode

### Content Processing
- **Code block compression**: Collapse `{...}` and indent blocks to single lines
- **Folder recursion**: Depth 5, text extensions only (50+ file types)
- **Git diff analysis**: Extract added lines from working tree + index changes
- **Stopwords**: `["const", "var", "let"]` (configurable)

### Context Settings (same as Obsidian)
```json
{
  "partOfSpeechToProcess": "HASHTAGS_AND_WORDS",
  "doubleSquarebracketsProcessing": "PROCESS_AS_HASHTAGS",
  "mentionsProcessing": "CONNECT_TO_ALL_CONCEPTS"
}
```

### Key Patterns
- **Webview architecture**: Extension host ↔ Webview ↔ iframe (three-tier)
- **State persistence**: `vscode.setState()`/`getState()` across webview lifecycle
- **Clipboard integration**: Copy graph data with configurable prefix for AI copilots
- **File search**: `workbench.action.findInFiles` with AND-pattern (`^(?=.*term1)(?=.*term2)`) or OR-pattern (`term1|term2`)
- **Global state**: Graph data accessible via `getGraph` command for AI chat integration

### AI Action Prompts
```
question:    "Generate a question that uses the current context and the graph structure below:"
develop:     "Generate an idea that uses the current context and the graph structure below:"
summarize:   "Summarize the content using the current context and the graph structure below:"
context:     "Retrieve the most relevant content from the current context..."
context_gap: "Find the gap in the current context that would bridge the graph structure below:"
```

## Platform: n8n (Workflow Automation)

### Workflow Categories
| Category | Count | Pattern |
|----------|-------|---------|
| GraphRAG Chatbots | 5 | Webhook/Trigger → InfraNodus retrieval → LLM → Response |
| Content Creation | 2 | Input → Extract → Gap Analysis → Idea Generation |
| Marketing/SEO | 2 | URL batch → Content Gap Detection → Optimization |
| Research | 2 | PDF → Extract → Research Questions via Gaps |
| File Sync | 3 | Google Drive ↔ InfraNodus sync |
| Customer Support | 4 | Email/Ticket → Knowledge Graph → Summary/Response |

### Common n8n Node Pattern
```json
{
  "type": "n8n-nodes-infranodus.infranodus",
  "parameters": {
    "operation": "graphAndStatements|graphAndAdvice|search|..."
  }
}
```

### Integration Nodes Used
- InfraNodus (custom node)
- LangChain ChatTrigger
- LangChain Chat (OpenAI, Anthropic)
- Webhook
- Gmail, Google Drive
- Zendesk, Slack
- FireCrawl (content extraction)
- Google Analytics

## Platform: MCP (Model Context Protocol)

### Transport Modes
| Mode | Entry Point | Use Case |
|------|------------|----------|
| stdio | `bin/infranodus-mcp-server.js` | Local (Claude Desktop, Cursor) |
| HTTP/SSE | `src/http-server.ts` | Hosted deployment |

### Authentication
- **stdio**: API key from environment variable
- **HTTP**: OAuth2 authorization code flow with PKCE + direct API key exchange
- **JWT**: Tokens contain original API key for stateless verification

### Handler Pattern
```
Zod schema validation → URL/text resolution → URLSearchParams construction
  → makeInfraNodusRequest(endpoint, body) → transformer function
  → { content: [{ type: "text", text: JSON.stringify(result) }] }
```

## Platform: Claude (Skills)

### Skill Structure
```
skill-<name>/
  SKILL.md    # YAML frontmatter (name, description) + Markdown body
```

### Distribution
- Claude Web/Desktop: Upload `.zip` via Settings → Capabilities
- Claude Code: Copy to `.claude/skills` directory
- GitHub Releases: Automated via `release.yml` workflow

### Activation
The `description` field in YAML frontmatter serves as both documentation and trigger condition. Claude matches user intent against skill descriptions to decide activation.

## Adaptive Behavior Rules
When operating within any platform:
1. Detect platform context from tool availability and user environment
2. Adapt content processing settings accordingly
3. Use platform-native output formats (DOT graph for visualization, wikilinks for Obsidian, clipboard format for VSCode)
4. Respect platform-specific constraints (context size limits, API rate limits)
