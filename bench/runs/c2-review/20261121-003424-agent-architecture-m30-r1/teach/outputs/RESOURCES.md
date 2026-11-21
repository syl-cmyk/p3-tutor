# Agent architecture Resources

## Knowledge

- [Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents)
  Engineering post on curating what is in an agent's window, context rot, just-in-time retrieval and long tasks. Use for: deciding what the assistant keeps in context.
- [Claude docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  Official docs on how the window grows, plus the memory tool and context editing. Use for: window limits, token planning, memory tool.
- [Anthropic: Managing context on the Claude Developer Platform](https://www.anthropic.com/news/context-management)
  Announcement of tool-result clearing and the memory tool, with reported gains. Use for: trimming old tool results.
- [Anthropic: Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)
  Chunking, embeddings, BM25 and the source-line fix for chunks. Use for: searching the long manuals.
- [Liu et al.: Lost in the Middle (TACL 2024)](https://arxiv.org/abs/2307.03172)
  Peer-reviewed study of how models use facts at different positions in long inputs. Use for: why more context is not always better.
- [Anthropic: Building effective agents](https://www.anthropic.com/engineering/building-effective-agents)
  Workflows versus agents. Use for: the upcoming workflow-versus-agent objective.

## Wisdom (Communities)

- Your design review and course staff: the only community used so far; no online community has been vetted yet.
