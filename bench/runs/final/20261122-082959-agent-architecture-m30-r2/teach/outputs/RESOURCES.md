# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what goes in an agent's context, context rot, compaction, notes and just-in-time retrieval. Use for: deciding what the assistant keeps in its context.
- [Docs: "Context windows" (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history is carried forward, clearing and compaction. Use for: sizing and trimming the context.
- [Docs: "Memory tool" (Claude Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  File-based memory that persists between sessions, run by your own application. Use for: saving student training status between visits.
- [Article: "Introducing Contextual Retrieval" (Anthropic)](https://www.anthropic.com/news/contextual-retrieval)
  Chunking, embeddings, keyword search and why chunks lose context. Use for: finding the right page in a long manual.

## Wisdom (Communities)

- [Hugging Face Agents Course: Discord and community](https://huggingface.co/learn/agents-course/en/unit0/discord101)
  Course Discord with question and showcase channels. Use for: asking about agent designs and sharing what you built.
