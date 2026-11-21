# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what goes into an agent's context, just-in-time retrieval, compaction and note-taking. Use for: context, memory and retrieval decisions.
- [Docs: Memory tool (Claude Platform)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How a file-based memory works, with the application running the file operations. Use for: building notes that persist between sessions.
- [Docs: Context editing (Claude Platform)](https://docs.claude.com/en/docs/build-with-claude/context-editing)
  Automatic clearing of old tool results. Use for: keeping long loops within budget.
- [Article: "Managing context on the Claude Developer Platform" (Claude blog)](https://claude.com/blog/context-management)
  Overview of memory and context editing together; its performance figures are vendor-reported. Use for: when to combine them.
- [Paper: "Lost in the Middle: How Language Models Use Long Contexts" (TACL 2024)](https://aclanthology.org/2024.tacl-1.9/)
  Peer-reviewed evidence that accuracy drops when key information is in the middle of a long input. Use for: arguing against stuffing the context.

## Wisdom (Communities)

- [Hacker News discussion of the context engineering post](https://news.ycombinator.com/item?id=45418251)
  Practitioners comparing experiences. Use for: seeing how others handle context in real agents.

## Gaps

- A high-trust, beginner-friendly source on retrieval search (keyword vs meaning-based) for the manuals.
- A well-moderated community for student agent builders; not yet found.
