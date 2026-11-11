# Agent architecture Resources

## Knowledge

- [Article: "Effective context engineering for AI agents" (Anthropic Engineering)](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  Context rot, the attention budget, just-in-time retrieval, compaction, note-taking and sub-agents. Use for: deciding what an agent keeps in context and what it saves outside it.
- [Docs: "Context windows" (Claude Platform docs)](https://platform.claude.com/docs/en/build-with-claude/context-windows)
  What counts toward the window, how turns accumulate, overflow behaviour, compaction. Use for: how the context window works in practice and what is resent on each call.
- [Docs: Memory tool (Claude Platform docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)
  How an agent stores and reads files outside its context between sessions. Use for: designing what the assistant saves between visits. (Linked from the context-windows page; not read in full.)
- [Article: "Contextual Retrieval" (Anthropic)](https://anthropic.com/research/contextual-retrieval)
  Why chunks lose meaning when a manual is split, and how embeddings plus keyword search plus reranking cut retrieval failures. Use for: finding the right page in a long manual.

## Wisdom (Communities)

No community has been chosen yet; the learner's own design team, course instructor and design-review audience are the first places to test these ideas.

## Gaps

- A high-trust community for people building small retrieval-based assistants.
- A worked, small-scale retrieval tutorial in Python for a learner who has never called a model from code.
