# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on the context window, context rot, trimming and compaction, note-taking and just-in-time retrieval. Use for: anything about what an agent keeps in context.
- [Docs: Memory tool (Claude Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How a file-based memory directory persists across conversations, with the program running each file operation. Use for: designing notes between sessions and path checks.
- [Article: "Introducing Contextual Retrieval" (Anthropic Engineering)](https://www.anthropic.com/engineering/contextual-retrieval)
  Why chunks lose context, the fix, and the size below which a knowledge base can just go in the prompt. Use for: retrieval over long manuals.
- [Docs: Context editing (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/context-editing)
  Clearing old tool results as a named feature (beta). Use for: trimming long sessions.
- [Post: "Managing context on the Claude Developer Platform"](https://claude.com/blog/context-management)
  Vendor announcement of context editing and the memory tool. Use for: further reading only, not for numbers.

## Wisdom (Communities)

No community has been verified yet.

## Gaps

- A vetted community where the learner can test agent design choices.
