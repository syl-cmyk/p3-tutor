# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Defines context, context rot and the attention budget; covers compaction, structured note-taking, just-in-time retrieval and sub-agents. Use for: what to keep in context, what to save outside it, and how an agent finds information.
- [Docs: "Context windows" (Claude Platform docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of what counts toward the window (system prompt, messages, tool results, tool definitions), how turns accumulate, compaction and overflow. Use for: exact mechanics of the window and how history is carried between calls.
- [Article: "Contextual Retrieval" (Anthropic)](https://anthropic.com/research/contextual-retrieval)
  Explains retrieval over chunks of long documents, with embeddings and BM25, and why chunks lose context. Use for: how the assistant finds the right page in a long manual.

## Wisdom (Communities)

No community yet; the learner's own design team and design reviews are the first place to test these ideas.

## Gaps

- A community of people building small retrieval or agent projects, to find later.
