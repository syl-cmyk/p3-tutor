# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Covers context, context rot, compaction, note-taking and just-in-time retrieval for agents. Use for: what to keep in the window and what to put outside it.
- [Docs: "Context windows" (Claude API)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Explains what counts toward the window and how each turn re-sends the history. Use for: token mechanics and why cost grows with steps.
- [Docs: "Memory tool" (Claude API)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A client-side memory directory that persists between sessions, with safety notes. Use for: designing per-student notes.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings versus exact-word search, and when to skip retrieval. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- None verified yet; see Gaps.

## Gaps

- A verified, well-moderated community for agent builders to test these skills.
