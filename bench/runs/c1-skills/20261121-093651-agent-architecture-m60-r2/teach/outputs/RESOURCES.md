# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a limited budget, context rot, just-in-time retrieval, notes. Use for: deciding what the assistant keeps in context.
- [Docs: Context windows (Claude Platform)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  How the window fills over a conversation. Use for: precise definitions and limits.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
  File-based memory that is client-side. Use for: designing what is saved between sessions.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Why chunks lose meaning and how contextual embeddings plus BM25 cut retrieval failures. Use for: finding the right page in a long manual.
- [Article: "Managing context on the Claude Developer Platform" (Anthropic)](https://www.anthropic.com/news/context-management)
  Context editing and memory together. Use for: trimming stale tool results.

## Wisdom (Communities)

- Local: the makerspace's own staff.
  Use for: deciding which student facts are worth remembering and what questions students really ask.

## Gaps

- A trusted source on token pricing that stays current; check the provider's pricing page when budgeting.
