# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on the context window as a finite resource, compaction, note-taking and just-in-time retrieval. Use for: anything about what an agent keeps in context and what it saves outside it.
- [Docs: "Context windows" (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, context rot, clearing and compaction. Use for: window size and per-call accumulation.
- [Docs: "Memory tool" (Claude API)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  Client-side memory files that persist between sessions, with security notes. Use for: designing notes that survive sessions.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings vs BM25, and why chunks lose context. Use for: finding the right page in a long manual.
- [Docs: "Pricing" (Claude API)](https://platform.claude.com/docs/en/about-claude/pricing)
  Input vs output token prices, cache pricing, rough tokens per page. Use for: cost-per-request estimates.

## Wisdom (Communities)

None found yet.

## Gaps

- A high-trust community where the learner can test agent design (not yet searched).
