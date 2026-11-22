# Agent architecture Resources

## Knowledge

- [Anthropic Engineering: "Effective context engineering for AI agents"](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context as a finite resource, just-in-time retrieval, compaction, tool-result clearing and note-taking. Use for: deciding what goes in the window.
- [Claude docs: "Context windows"](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, context rot, compaction. Use for: token and cost reasoning.
- [Claude docs: "Memory tool"](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  A client-side notes folder the model reads and writes across sessions, with security notes. Use for: designing the student-status memory.
- [Anthropic Engineering: "Introducing Contextual Retrieval"](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunks, embeddings, BM25 and chunk context. Use for: searching long manuals.
- [Anthropic: "Managing context on the Claude Developer Platform"](https://claude.com/blog/context-management)
  Memory outside the window plus context editing inside it, with Anthropic's internal results. Use for: how the two fit together.

## Wisdom (Communities)

- [r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/) and the Discord listed on the Claude community page
  Channels where builders share projects and ask for help. Use for: asking how others handle memory and retrieval (listed on the Claude community page; not opened).
