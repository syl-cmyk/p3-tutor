# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Best single source on context as a finite budget, compaction, note-taking memory, just-in-time retrieval and sub-agents. Use for: what to keep in context, what to save, how an agent finds things.
- [Docs: "Context windows" (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official definition of the context window, what counts toward it, context rot, compaction and context editing. Use for: what is in the window at each step, and window limits.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/engineering/contextual-retrieval)
  How retrieval over a long document set works (chunks, embeddings, BM25, reranking) and what it costs. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- Local: your senior design team and its design reviews
  Use for: defending the memory and retrieval choices to people who will question them.

## Gaps

- No verified online community for agent builders yet; find and check one before recommending it.
