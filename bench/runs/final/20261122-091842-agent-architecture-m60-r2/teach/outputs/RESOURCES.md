# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a limited budget, context rot, just-in-time retrieval, compaction, clearing old tool results and note-taking outside the window. Use for: the big picture of what to keep, fetch and save.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history grows each turn, context rot, overflow behaviour. Use for: exact definitions and limits.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side memory files the model reads and writes through tool calls. Use for: designing notes between sessions, and their security caveats.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings, BM25 exact matching and reranking, with failure rates. Use for: how to find the right page in a long manual.
- [Docs: Token counting (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/token-counting)
  Tokens are estimates that differ by model; a free counting endpoint. Use for: cost estimates for the design review.

- [Blog: "Managing context on the Claude Developer Platform"](https://claude.com/blog/context-management)
  Short note on context editing and the memory tool working together. Use for: a quick overview of both features.

## Wisdom (Communities)

- [LangChain forum](https://forum.langchain.com/)
  The official LangChain Discourse forum; its Talking Shop category covers building agentic applications, including RAG and agent memory. Use for: asking how others design agent memory and retrieval (centred on LangChain tools).

## Gaps

- A community with confirmed moderation rules for agent design; the LangChain forum is listed, but its moderation was not confirmed.
