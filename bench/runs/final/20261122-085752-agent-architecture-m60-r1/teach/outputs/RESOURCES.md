# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what goes into an agent's context: context rot, just-in-time retrieval, compaction, clearing tool results, note-taking. Use for: any decision about what the assistant keeps in its window.
- [Docs: Context windows (Claude docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Defines the window, shows how history accumulates call by call, and gives window sizes. Use for: what counts toward the window, and checking the size for the model the team picks.
- [Docs: Memory tool (Claude docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How a file-based memory works when the program runs the operations, with commands and security notes. Use for: designing notes saved between sessions.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, BM25, and why chunks need context. Use for: how the assistant finds the right page in a long manual.
- [Docs: Pricing (Claude docs)](https://platform.claude.com/docs/en/about-claude/pricing)
  Input and output token prices, cache rates, tokenizer note. Use for: budget estimates; read real prices here, not from lesson examples.

## Wisdom (Communities)

None verified yet.

## Gaps

- A verified community for testing agent-design skills (forum or subreddit) has not been found yet.
