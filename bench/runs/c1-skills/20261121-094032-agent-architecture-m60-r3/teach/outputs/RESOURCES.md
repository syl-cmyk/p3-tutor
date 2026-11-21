# Agent architecture Resources

## Knowledge

- [Anthropic: Effective context engineering for AI agents](https://anthropic.com/research/effective-context-engineering-for-ai-agents)
  Best single piece on what to keep in an agent's window. Use for: context policy, just-in-time loading, summarizing, notes.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official description of the window and its limits. Use for: current window sizes and how the window fills.
- [Claude docs: Context editing](https://docs.claude.com/en/docs/build-with-claude/context-editing)
  Automatic clearing of old tool results. Use for: cutting cost on long loops.
- [Claude docs: Memory tool](https://docs.claude.com/en/docs/agents-and-tools/tool-use/memory-tool)
  File-based memory run by your own code. Use for: designing notes between sessions.
- [Anthropic: Managing context](https://www.anthropic.com/news/context-management)
  Announcement of context editing and the memory tool, with their own test results. Use for: why the two work together.
- [Liu et al., Lost in the Middle (TACL 2024)](https://aclanthology.org/2024.tacl-1.9/)
  Peer-reviewed study of position effects in long inputs. Use for: arguing against "just paste everything".
- [Lewis et al., Retrieval-Augmented Generation (NeurIPS 2020)](https://arxiv.org/abs/2005.11401)
  The original retrieval-augmented generation paper. Use for: where the chunk-and-retrieve recipe comes from.

## Wisdom (Communities)

- Local: the makerspace staff who answer students today
  Use for: the questions students really ask, as retrieval test cases.

## Gaps

- A practical, trusted guide to chunking manuals and tuning top-k for a small project.
