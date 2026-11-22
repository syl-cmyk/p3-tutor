# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a limited budget, context rot, compaction, note-taking, just-in-time retrieval. Use for: deciding what an agent keeps in its context.
- [Docs: Context windows (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how turns accumulate, window sizes, clearing and compaction. Use for: cost and limits of the window.
- [Docs: Memory tool (Claude API)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A file-based memory the application stores and the model reads through tool calls. Use for: saving notes between sessions.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings plus keyword search, failure rates, when to skip retrieval. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- None found yet.

## Gaps

- A well-moderated community for agent builders (to be found and verified).
