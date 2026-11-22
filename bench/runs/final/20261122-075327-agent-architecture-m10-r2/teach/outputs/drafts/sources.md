# Sources check for O3 (context and memory in an agent)

All pages below were opened with WebFetch in this session.

## 1. PRIMARY. Anthropic Engineering, "Effective context engineering for AI agents"
- Address: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened exactly as written; the page text did not state its own final address, so no redirect was seen or confirmed).
- Context is the set of tokens in a call, finite resource: SUPPORTED. "Context refers to the set of tokens included when sampling from a large-language model (LLM)." and "Context, therefore, must be treated as a finite resource with diminishing marginal returns."
- Context rot, recall falls as tokens grow: SUPPORTED. The page says the model's "ability to accurately recall information from that context decreases" as tokens grow.
- Larger windows do not remove the clutter problem: SUPPORTED. "context windows of all sizes will be subject to context pollution and information relevance concerns."
- Just-in-time retrieval with lightweight identifiers: SUPPORTED. Agents "maintain lightweight identifiers" and load data at runtime.
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit" and summarizing it into a new window.
- Clearing old tool results as the lightest compaction: SUPPORTED. "One of the safest lightest touch forms of compaction is tool result clearing."
- Structured note-taking outside the window, read back later: SUPPORTED. The agent "regularly writes notes persisted to memory outside of the context window"; "These notes get pulled back into the context window at later times."
- May the writer cite it: YES, as the primary source.

## 2. Claude Docs, "Memory tool"
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (no redirect; the page metadata gives the same address).
- Memory is a directory of files that persists across conversations: SUPPORTED. "store and retrieve information across conversations in a directory of memory files ... files that persist between sessions".
- Client-side, Claude requests and the app runs: SUPPORTED. "Claude requests file operations, and your application runs them."
- `view` and `create` commands, `/memories` path: SUPPORTED (both are documented; files are stored under `/memories`). The success text is "File created successfully at: {path}", so the lesson's "File created successfully" is a fair shortening.
- Checked first thing: SUPPORTED. "Claude automatically checks its memory directory before starting a task."
- Path validation for security: SUPPORTED. "Your implementation must validate every path in every command to prevent directory traversal attacks."
- Standard tool-use loop: SUPPORTED. "the standard tool-use loop"; the app "sends the conversation back so Claude can continue".
- PARTLY SUPPORTED: "one file per student, path checked so one student's session cannot read another's". The page says `/memories` can map to "a per-user directory or keys in a database" and that paths must be restricted to `/memories`. It does not say one file per student. Word it as the lesson's own design choice built on those two facts.
- May the writer cite it: YES.

## 3. Anthropic Engineering, "Introducing Contextual Retrieval"
- Address: https://www.anthropic.com/engineering/contextual-retrieval (opened as written; the page text did not state a final address, no redirect seen).
- Chunks lose context and get missed: SUPPORTED. "traditional RAG solutions remove context when encoding information".
- Adding explanatory context to each chunk: SUPPORTED. "prepending chunk-specific explanatory context to each chunk before embedding".
- Under about 200,000 tokens (about 500 pages) can go in the prompt: SUPPORTED. "smaller than 200,000 tokens (about 500 pages of material)".
- Failure rates 5.7% to 3.7% (embeddings), 2.9% (plus keyword search, BM25), 1.9% (plus reranking): SUPPORTED. These are top-20-chunk retrieval failure rates, down 35%, 49% and 67%. Say "top-20-chunk retrieval failures" in the lesson.
- May the writer cite it: YES.

## 4. Anthropic, context management announcement
- Address: https://claude.com/blog/context-management (the plan's address https://www.anthropic.com/news/context-management returned a 308 permanent redirect to this one; use the final address).
- Describes context editing and the memory tool: SUPPORTED. A product update dated 29 September 2025. It says context editing "automatically clears stale tool calls and results", and the memory tool lets Claude "store and consult information outside the context window through a file-based system".
- It was in public beta at the time of writing, and it reports internal evaluation numbers (39%, 29%, 84%), which the lesson should not quote.
- May the writer cite it: YES, as a "further reading" link only, described as a vendor announcement.

## 5. Claude Docs, "Context editing"
- Address: https://platform.claude.com/docs/en/build-with-claude/context-editing (no redirect; the page metadata gives the same address). Read the first 100,000 of 102,210 characters.
- Clearing old tool results as a named feature: SUPPORTED. "The `clear_tool_uses_20250919` strategy clears tool results when conversation context grows beyond your configured threshold." Old results are replaced by placeholder text.
- It was marked beta on the page, so do not call it a settled feature.
- May the writer cite it: YES, as a "further reading" link.

## Claims in the plan that no source supports (leave out, or word as the lesson's own advice or arithmetic)
- "Cost grows faster than the length of the conversation": no page says it. It is the lesson's own arithmetic (1,418 + 1,568 + 1,638 = 4,624). Present it as that arithmetic.
- The comparison table cells "re-indexed on change" and "until deleted": no page says these. Present them as the lesson's simplification.
- "One file per student" as the privacy answer: see source 2, partly supported only.
- The 400 tokens per page figure is derived from 200,000 tokens over about 500 pages. It is the lesson's own derived figure, as the plan already notes.
- All trace token counts and the 20-machine, 2,000-token example are illustrative, not from a source.
