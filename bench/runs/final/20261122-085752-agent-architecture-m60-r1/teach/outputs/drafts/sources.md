# Sources for O3 lesson plan (checked 2026-11-22)

All pages below were opened with WebFetch in this session. Prices, model names and sizes are as the pages showed them today.

## 1. PRIMARY. Effective context engineering for AI agents (Anthropic Engineering)
- Address: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened; the fetch tool does not report redirects). The www form https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents also opened, title "Effective context engineering for AI agents \ Anthropic". Use the www form (it is the form the Anthropic docs link to).
- Context = set of tokens: SUPPORTED. "Context refers to the set of tokens included when sampling from a large-language model (LLM)."
- Context rot / attention budget: SUPPORTED. Recall accuracy drops as tokens in the window increase; LLMs have "an 'attention budget'".
- Just-in-time retrieval with light pointers: SUPPORTED. Agents "maintain lightweight identifiers (file paths, stored queries, web links, etc.)" and load data at runtime.
- Hybrid approach: SUPPORTED. Agents "might employ a hybrid strategy, retrieving some data up front for speed."
- Compaction, Claude Code keeps summary plus five files: SUPPORTED. "compressed context plus the five most recently accessed files."
- Clearing tool results: SUPPORTED. "tool result clearing" called one of the safest, lightest-touch forms of compaction.
- Structured note-taking: SUPPORTED. "the agent regularly writes notes persisted to memory outside of the context window."
- Pokemon example: SUPPORTED. "maintains precise tallies across thousands of game steps."
- Not seen on the page (unchecked here): the plan's "tune for recall first" wording; keep it as lesson advice unless the writer re-reads that section.
- May cite: YES, as primary.

## 2. Claude docs: Context windows
- Address: https://platform.claude.com/docs/en/build-with-claude/context-windows
- Definition: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself."
- Everything counts: SUPPORTED. "the system prompt, every message in `messages` (including tool results, images, and documents), and your tool definitions. The output Claude generates for the turn ... counts too."
- Turns accumulate, each call resends history: SUPPORTED. "Input phase: Contains all previous conversation history plus the current user message"; output "becomes part of the input for the next turn".
- Sizes: SUPPORTED, with a caveat. "up to 1M tokens, depending on the model"; Claude Sonnet 5.5 and others have 1M; "Other Claude models, including Claude Sonnet 4.5 (deprecated), have a 200k-token context window." Point learners to the All models table.
- Context rot: SUPPORTED. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Compaction and context editing: SUPPORTED. Server-side compaction (beta); context editing has "Tool result clearing".
- Cached prefixes occupy the window: SUPPORTED. "Cached prompt prefixes still occupy the context window ... changes what you pay for those tokens, not whether they count."
- Multisession pointer: SUPPORTED. Tip links the memory tool's multisession pattern.
- May cite: YES.

## 3. Claude docs: Memory tool
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- Client-side: SUPPORTED. "Claude requests file operations, and your application runs them"; result returned in a `tool_result` block.
- Persists between sessions under /memories: SUPPORTED. "files that persist between sessions"; stores "under `/memories`".
- Six commands: SUPPORTED. view, create, str_replace, insert, delete, rename.
- View-first protocol: SUPPORTED. "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE"; the API adds it to the system prompt. Empty first view "is not an error".
- Path traversal: SUPPORTED. Warning about `/memories/../../secrets.env`; validate every path.
- Size caps and expiration: SUPPORTED. "Track memory file sizes and cap how large a file can grow"; "Periodically delete memory files that haven't been accessed in a long time."
- Clearing vs compaction: SUPPORTED. "Context editing clears specific tool results on the client. Compaction automatically summarizes the whole conversation on the server."
- Multisession pattern: SUPPORTED. Progress log, new sessions "open by reading those memory files".
- Plan trace detail: the doc's own example is a customer-service ticket; the makerspace trace is the lesson's own, so word it as an illustration.
- May cite: YES.

## 4. Anthropic: Introducing Contextual Retrieval
- Address: https://www.anthropic.com/news/contextual-retrieval (opened; fetch tool gave no final-URL info).
- Chunking: SUPPORTED. Break knowledge base into chunks of "no more than a few hundred tokens".
- Embeddings and BM25: SUPPORTED. BM25 "uses lexical matching to find precise word or phrase matches"; embeddings give semantic search.
- Combine: SUPPORTED. "Embeddings+BM25 is better than embeddings on their own."
- Under 200,000 tokens rule: SUPPORTED. Knowledge base "smaller than 200,000 tokens" needs no RAG; prompt caching makes it cheaper and faster. The "about 500 pages" gloss was not quoted by the fetch; say "about 200,000 tokens" and treat pages as the lesson's own conversion.
- Lost-context example: SUPPORTED. "The company's revenue grew by 3% over the previous quarter." names no company or period.
- Top-20: SUPPORTED. "Passing the top-20 chunks to the model is more effective than just the top-10 or top-5." One test set; present as one result.
- 35% / 49% / 67%: SUPPORTED. Contextual Embeddings 35%, plus Contextual BM25 49%, plus reranking 67% fewer top-20 retrieval failures.
- Plan's "tag each chunk with manual and section" is the lesson's own adaptation, not the post's method; word it that way.
- May cite: YES.

## 5. Claude docs: Pricing
- Address: https://platform.claude.com/docs/en/about-claude/pricing
- Sonnet 5.5 $2 in / $10 out per MTok: SUPPORTED (table row "Claude Sonnet 5.5 | $2 / MTok ... $10 / MTok").
- Cache read 0.1x most models, 0.05x Sonnet 5.5: SUPPORTED. "0.1x base input price on most models"; Sonnet 5.5 0.05x, $0.10 / MTok.
- Tool-use tokens count as input: SUPPORTED. Extra tokens come from the `tools` parameter, `tool_use` blocks and `tool_result` blocks; also a tool-use system prompt (286 tokens on Sonnet 5.5). NOTE: this makes the plan's "three tools = 600 tokens" an illustration only; real counts add overhead.
- Tokenizer varies: SUPPORTED. "How many tokens the same text produces depends on the model's tokenizer, the language, and the type of content."
- "Tokens are pieces of text that models process": SUPPORTED (FAQ).
- NOT SUPPORTED on this page: "100 tokens is about 75 words" (see source 6).
- Output billed at higher rate: SUPPORTED by the table; no sentence states it, the rates show it.
- May cite: YES. Tell the learner prices change; the page itself points to claude.com/pricing for the latest.

## 6. EXTRA. OpenAI Help: What are tokens and how to count them
- Address: https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them
- Rule of thumb: SUPPORTED. "1 token is approximately three-quarters of a word"; "100 tokens are approximately 75 words"; "1 token is approximately 4 characters" (English). These are estimates; counts vary by model.
- Use for: the 75-words rule the pricing page does not state. Describe it as an English rule of thumb from a different provider's help page.
- May cite: YES, for that claim only.

## 7. EXTRA. Weights fixed during a chat
- Address: https://arxiv.org/abs/2507.16003 ("Learning without training: The implicit dynamics of in-context learning", Dherin, Munn, Mazzawi, Wunder, Gonzalvo; Google Research).
- PARTLY SUPPORTED. Abstract: "at inference time an LLM is able to learn new patterns without any additional weight update". It says weights are not updated when a model uses examples in the prompt. It does not say in plain beginner words that "weights are fixed in a chat", and it is a research paper about how in-context learning works, not a product statement.
- May cite: only as "go further", worded narrowly: in-context learning happens with no weight update. For the lesson's plain claim (the model is the same on every call; memory lives in the text and files) keep it as the lesson's own explanation, backed by sources 2 and 3 (the program resends history; memory is files in the app).

## 8. Community. r/LLMDevs
- Address seen: https://thehiveindex.com/communities/r-llmdevs/ (a third-party directory, opened). Reddit pages (www.reddit.com and old.reddit.com) could NOT be opened by the fetch tool, so the subreddit itself is unconfirmed by me.
- What the directory page says: "A space for Enthusiasts, Developers and Researchers to discuss LLMs and their applications"; about 182K members; most common themes "Solution Requests and Self-Promotion"; it says nothing about rules or moderation.
- Search results (mirror snapshots) showed threads on testing agents, frameworks and MCP. Not opened.
- VERDICT: NOT verified as high-trust. Do not put a reddit.com address in RESOURCES.md (not seen exactly in a result nor opened). If the writer names it, say only: "a large Reddit community where people discuss building with LLMs; quality varies and self-promotion is common", with the directory link as the evidence. Better to write a Gap: "No verified, moderated community for LLM agent builders found".
- May cite: only with the wording above; otherwise leave out.

## Not opened, do not cite
- https://claude.com/blog/context-management and https://platform.claude.com/cookbook/tool-use-memory-cookbook (plan item 6): not opened in this session.
- Lewis et al. 2020 RAG paper: not opened.
- Mirror sites and Analytics Vidhya thread list from the community search: not opened.

## Claims in the plan with no source (word as the lesson's own advice or an illustration)
1. All makerspace numbers (800, 600, 30, 350 tokens; 15 manuals; 38,000-token session; 600-token summary) are invented; label as made-up round numbers.
2. "Tune for recall first" for summaries: not checked on the primary page.
3. "About 500 pages" for 200,000 tokens, and "500 tokens a page": the lesson's own conversion.
4. "Cost is 33 times": the lesson's arithmetic (123,250 x $2/M + $0.0010 = $0.2475 vs $0.0075), not a source claim.
5. Safety-training and stale-note design rule (notes for soft facts, lookup for gating facts): the lesson's own advice. The memory doc supports only "expire old files" and "keep notes up to date".
6. "Model weights do not change during a chat" in plain words: only the paper abstract (partly). Word it as the lesson's explanation.
7. "Claude Code keeps the summary plus 5 files" is supported, but "other providers work the same way" is unsourced; keep it as the lesson's remark or drop it.
