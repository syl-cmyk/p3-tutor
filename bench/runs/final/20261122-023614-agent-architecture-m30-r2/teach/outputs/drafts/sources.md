# Sources check for O3 (lesson 0001), checked 2026-11-21

All four pages were opened with WebFetch in this session, at the address written.

## Knowledge

### 1. Effective context engineering for AI agents (PRIMARY)
- Address: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened, no redirect noted)
- Maker's own engineering article. May cite: YES.
- Context is the set of tokens: SUPPORTED. "Context refers to the set of tokens included when sampling from a large-language model (LLM)."
- Context rot and finite attention budget: SUPPORTED. "uncovered the concept of context rot"; "LLMs have an 'attention budget'".
- Smallest set of high-signal tokens: SUPPORTED. "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."
- Just-in-time retrieval with light references: SUPPORTED. "maintain lightweight identifiers (file paths, stored queries, web links, etc.)". Runtime lookup slower: SUPPORTED. "runtime exploration is slower than retrieving pre-computed data."
- Compaction and clearing old tool results: SUPPORTED. "One of the safest lightest touch forms of compaction is tool result clearing".
- Structured note-taking: SUPPORTED. "Structured note-taking, or agentic memory, is a technique where the agent regularly writes notes".
- Pokemon aside: PARTLY. Page says "Claude playing Pokemon demonstrates how memory transforms agent capabilities in non-coding domains." The detail "keeps tallies across thousands of steps" was not confirmed in what I read; word it as the page does, or leave out the tallies.
- Sub-agents return 1,000 to 2,000 token summaries: SUPPORTED. "returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)."
- When to use which method: SUPPORTED. "The choice between these approaches depends on task characteristics"; compaction for extended back-and-forth, note-taking for iterative work with milestones, multi-agent for parallel research. The "hybrid of upfront and just-in-time" wording was not confirmed; do not quote it.

### 2. Context windows (Claude API docs)
- Address: https://platform.claude.com/docs/en/build-with-claude/context-windows (opened, no redirect). May cite: YES (primary for Parts 1 and 2 mechanics).
- Window = working memory, not training data: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself ... different from the large corpus of data the language model was trained on ... a 'working memory'".
- Everything counts: SUPPORTED. "the system prompt, every message in messages (including tool results, images, and documents), and your tool definitions. The output Claude generates ... counts too."
- Each turn's input is all history plus new message: SUPPORTED. "Input phase: Contains all previous conversation history plus the current user message".
- Context rot: SUPPORTED. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Compaction and tool-result clearing: SUPPORTED (named: server-side compaction; "Tool result clearing: Clear old tool results in agentic workflows").
- Size: SUPPORTED. "up to 1M tokens, depending on the model". Say "up to about a million tokens on current models"; some models are 200k.
- Prompt caching: SUPPORTED, narrowly. "prompt caching changes what you pay for those tokens, not whether they count."
- Multi-session tip: SUPPORTED. "For agents that span multiple sessions, design your state artifacts so that context recovery is fast when a new session starts."
- "Input and output tokens are priced separately": NOT SHOWN on this page. Only "thinking tokens ... are billed as output tokens" and kept thinking is "billed as input tokens". Word as the lesson's own plain statement, or link the pricing page after opening it.
- The 5,015 versus 1,860 totals are the lesson's own arithmetic (illustrative), resting on the re-sent history sentence above.

### 3. Memory tool (Claude API docs)
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened, no redirect). May cite: YES (primary for Part 3).
- Files persist between sessions: SUPPORTED. "a directory of memory files ... files that persist between sessions".
- Client-side: SUPPORTED. "Claude requests file operations, and your application runs them."
- /memories checked at start: SUPPORTED. "Claude automatically checks its memory directory before starting a task ... stores what it learns in files under /memories". First call is a `view` of `/memories`.
- Commands: SUPPORTED. view, create, str_replace, insert, delete, rename.
- Path traversal: SUPPORTED. "Your implementation must validate every path in every command to prevent directory traversal attacks." Handler "maps onto real storage, such as a per-user directory or keys in a database".
- Sensitive information: PARTLY. "Claude usually refuses to write sensitive information to memory files"; stronger guarantees need your own validation. Do not say it is guaranteed.
- Size caps and expiry: PARTLY. Both are advice to the developer ("Track memory file sizes and cap", "Periodically delete memory files"), not built-in limits.
- "Per-student privacy" and "do not trust a self-reported training note" are the lesson's own advice, not on this page.

### 4. Introducing Contextual Retrieval
- Address: https://www.anthropic.com/engineering/contextual-retrieval?utm_source=tldrai (opened). The clean address https://www.anthropic.com/engineering/contextual-retrieval also opened with no redirect, title "Introducing Contextual Retrieval". Cite the clean one (it was opened here). The plan's alternative anthropic.com/news/contextual-retrieval was NOT opened: do not use it.
- May cite: YES (primary for Part 4).
- RAG steps: SUPPORTED. Documents split into chunks, converted to embeddings, stored in a vector database; the most relevant chunks are retrieved and added to the prompt.
- Chunk loses context: SUPPORTED. "The company's revenue grew by 3% over the previous quarter." names no company or period.
- BM25 versus embeddings: SUPPORTED. For "Error code TS-999", BM25 matches the exact string, which embeddings alone may miss. "Embeddings+BM25 is better than embeddings on their own."
- Under 200,000 tokens: SUPPORTED. Under 200,000 tokens (about 500 pages) you can put the whole knowledge base in the prompt; prompt caching makes this faster and cheaper.
- The "top 3 chunks always returned even if irrelevant" claim and the "60 chunks of 330 tokens" setup are the lesson's own (illustrative), not on this page.

## Wisdom (Communities)

### r/LLMDevs (subreddit): NOT VERIFIED, do not link as verified
- https://www.reddit.com/r/LLMDevs/ could not be opened (the fetch tool is blocked for reddit.com). The community therefore could not be confirmed first-hand.
- What I saw: a directory page, https://thehiveindex.com/communities/r-llmdevs/ (opened), describes it as "A space for Enthusiasts, Developers and Researchers to discuss LLMs and their applications", about 182K members. That page says nothing on rules or moderation. A search also showed a pinned January 2025 rule reminder against unapproved promotions, seen only in a search summary of mirror sites.
- Verdict: the community is real as listed by a third-party directory, but its moderation quality is unconfirmed. The writer may mention it only as "a subreddit for LLM developers, listed by the Hive Index directory", with the directory link, or as plain text with no verification claim. Do not call it high-signal or well moderated.
- Anthropic Discord and r/LocalLLaMA (named in the plan): not searched or opened; leave out.
