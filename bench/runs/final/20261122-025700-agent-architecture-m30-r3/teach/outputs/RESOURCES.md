# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on curating what goes in the window: context rot, compaction, clearing old tool results, just-in-time retrieval, note-taking. Use for: what an agent keeps in context and why.
- [Docs: "Context windows" (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts in the window, how history accumulates each turn, context rot, compaction. Use for: how big a call is and what is resent.
- [Docs: "Memory tool" (Claude API)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based memory between sessions, the commands, and the safety rules. Use for: designing notes that last between visits.
- [Docs: "Token counting" (Claude API)](https://platform.claude.com/docs/en/build-with-claude/token-counting)
  How tokens are counted, including tool definitions. Use for: estimating cost per request.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, BM25, and when to skip retrieval. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- Not chosen yet; a community link for building agents is still to be found (see Gaps).

## Gaps

- A high-reputation community for people building agents with model APIs.
