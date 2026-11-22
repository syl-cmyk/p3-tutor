# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Primary source on what goes into an agent's context: context rot, compaction, note-taking, just-in-time retrieval. Use for: any decision about what the assistant keeps in its window.
- [Docs: "Context windows" (Claude Docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how history accumulates, context rot, compaction. Use for: how the window fills and what it costs.
- [Docs: "Memory tool" (Claude Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How an agent saves and reads notes between sessions through file operations the program runs. Use for: designing what the assistant remembers about each student.
- [Paper: "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" by Lewis et al. (NeurIPS 2020)](https://arxiv.org/abs/2005.11401)
  The original retrieval-augmented generation paper. Use for: why retrieval beats weights-only knowledge, and the idea of external memory.

- [Docs: "Pricing" (Claude Docs)](https://platform.claude.com/docs/en/about-claude/pricing)
  Prices are listed per million input and output tokens, with cheaper cached reads. Use for: estimating cost per request against the sponsor budget.

## Wisdom (Communities)

- [LangChain Forum](https://forum.langchain.com/)
  Discourse forum run by LangChain with a Talking Shop category on building agentic applications; guidelines ban promotion. Use for: asking design questions; it leans toward LangChain tools, and its reputation is not verified.

## Gaps

- A high-reputation, well-moderated community where Riley can test agent designs (not yet found and verified by search).
