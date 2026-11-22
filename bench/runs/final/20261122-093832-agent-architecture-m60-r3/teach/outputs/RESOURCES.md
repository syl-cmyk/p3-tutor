# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Covers the context window, context rot, just-in-time loading, compaction and note-taking in one place. Use for: deciding what an agent keeps in context, looks up, or saves.
- [Docs: Context windows (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history is re-sent each turn, compaction and context editing. Use for: sizing a request and understanding growth across steps.
- [Docs: Memory tool (Claude Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How file-based memory across sessions works, client-side, with security notes. Use for: designing what the assistant saves about each student.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, keyword search and why chunks lose context. Use for: finding the right page in a long manual.
- [Docs: Pricing (Claude Docs)](https://platform.claude.com/docs/en/about-claude/pricing)
  Input and output token prices and caching multipliers. Use for: cost per request; rates change, so recheck before the design review.
- [Docs: Token counting (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/token-counting)
  Counting tokens before sending a request. Use for: measuring manuals and prompts instead of guessing.

## Wisdom (Communities)

- None verified yet. Until one is found, use the design team and the course instructor for review.

## Gaps

- A high-reputation community for agent builders, verified by search.
