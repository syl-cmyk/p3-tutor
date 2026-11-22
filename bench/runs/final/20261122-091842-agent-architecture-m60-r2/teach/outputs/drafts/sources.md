# Sources for O3: context and memory in an agent

Checked 2026-11-22. Every page below was opened with WebFetch in this session.

## Knowledge

### 1. PRIMARY. Anthropic Engineering, "Effective context engineering for AI agents"
- Address: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened, no redirect seen; the page does not print its own address, and Anthropic's docs link to the www.anthropic.com form of the same path)
- Finite resource, diminishing returns: SUPPORTED. "Context, therefore, must be treated as a finite resource with diminishing marginal returns."
- Recall falls as tokens grow (context rot): SUPPORTED in substance. "the model's ability to accurately recall information from that context decreases." The fetched text did not show the words "context rot" or "attention budget", so use the term "context rot" from source 2, which names it.
- Smallest set of high-signal tokens: SUPPORTED. "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome."
- Just-in-time, lightweight pointers: SUPPORTED. Agents "maintain lightweight identifiers (file paths, stored queries, web links, etc.)".
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents,".
- Clearing old tool results: SUPPORTED, with a wording point. "One of the safest lightest touch forms of compaction is tool result clearing." The source treats clearing as a light form of compaction, not a separate technique. Word the plan's "three tools" as the lesson's own grouping.
- Structured note-taking: SUPPORTED. "the agent regularly writes notes persisted to memory outside of the context window."
- The claim "clearing keeps a record that the call happened (a stub)": NOT FOUND on this page. Word as the lesson's own design.
- May the writer cite it? Yes, as primary.

### 2. Claude Platform docs, "Context windows"
- Address: https://platform.claude.com/docs/en/build-with-claude/context-windows (no redirect)
- Definition: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself"; "different from the large corpus of data the language model was trained on"; "working memory".
- Context rot: SUPPORTED. "more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- History resent each turn: SUPPORTED. Input phase "Contains all previous conversation history plus the current user message"; "previous turns are preserved completely".
- Everything counts: SUPPORTED. "the system prompt, every message in messages (including tool results...), and your tool definitions. The output Claude generates for the turn... counts too."
- 1M windows: SUPPORTED. "up to 1M tokens, depending on the model"; many current models are listed at 1M, others at 200k.
- Overflow: SUPPORTED. Input alone over the window gives "a 400 invalid_request_error ('prompt is too long')". On Claude 4.5 and newer, if generation reaches the limit it stops with stop_reason "model_context_window_exceeded". Older models return a validation error instead, so say "on current models".
- Tool result clearing and compaction: SUPPORTED. "Tool result clearing: Clear old tool results in agentic workflows"; server-side compaction "summarizes earlier parts of the conversation" (beta).
- "Clearing removes re-fetchable results while keeping a record": NOT FOUND here. Leave out or word as the lesson's own advice.
- May the writer cite it? Yes.

### 3. Claude Platform docs, "Memory tool"
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (no redirect)
- Client-side: SUPPORTED. "Claude requests file operations, and your application runs them." Storage can be "a per-user directory or keys in a database".
- Commands: SUPPORTED. view, create, str_replace, insert, delete, rename (the page has no "edit" command; say "edit" only loosely).
- Check memory first, assume interruption: SUPPORTED. The auto-added prompt says "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE" and "Your context window might be reset at any moment".
- Path traversal, size cap, expiry: SUPPORTED. The page uses the example `/memories/../../secrets.env`; "Track memory file sizes and cap how large a file can grow"; "Periodically delete memory files that haven't been accessed in a long time."
- Multi-session pattern: SUPPORTED. Later sessions open by reading the memory files; before a session ends it updates the progress log. The page's example is software projects.
- May the writer cite it? Yes.

### 4. Anthropic Engineering, "Introducing Contextual Retrieval"
- Address: https://www.anthropic.com/engineering/contextual-retrieval (opened; the page does not print its own address)
- RAG steps: SUPPORTED. Split into chunks, embeddings, vector database, BM25 for exact terms, merge by rank fusion, top-K chunks into the prompt.
- Skip RAG under about 200,000 tokens: SUPPORTED. "about 200,000 tokens (roughly 500 pages)"; prompt caching makes it faster and cheaper.
- Failure rates in the top 20: SUPPORTED. 5.7% standard embeddings, 3.7% contextual embeddings, 2.9% plus contextual BM25, 1.9% with reranking.
- E-42 example: NOT in the page. The page's own example is "Error code TS-999" (BM25 matches the exact string). Use TS-999 as the source's case, or call E-42 the lesson's own invention.
- May the writer cite it? Yes.

### 5. Claude Platform docs, "Token counting"
- Address: https://platform.claude.com/docs/en/build-with-claude/token-counting (no redirect)
- Estimates: SUPPORTED. "The token count is an estimate."
- Free: SUPPORTED. "Token counting is free to use", with rate limits.
- 30 percent: SUPPORTED, with a limit. "Claude 4.7 and later models... The same input text produces approximately 30 percent more tokens than on earlier models. The exact increase depends on the content." So 1,000 to 1,300 is only an illustration.
- May the writer cite it? Yes.

### 6. Anthropic, "Managing context on the Claude Developer Platform" (optional, go further)
- Address: https://claude.com/blog/context-management (https://www.anthropic.com/news/context-management returned a 308 redirect to this address; I opened the final one)
- SUPPORTED. "Context editing automatically clears stale tool calls and results"; "The memory tool enables Claude to store and consult information outside the context window".
- I did not read any performance percentages. Do not cite any.
- May the writer cite it? Yes, for those two sentences only.

## Wisdom (Communities)

### LangChain Forum
- Address: https://forum.langchain.com/ (opened). Example thread: https://forum.langchain.com/t/building-reliable-ai-agent-workflows-with-langgraph-and-rag/4945 (opened).
- What I saw: a Discourse forum run by LangChain. Categories include OSS Product Help, LangSmith Product Help, LangChain Academy and "Talking Shop" ("general discussion about LangChain and building agentic applications"). The example thread asks about RAG, agent memory (short-term and long-term) and tool failures, and a LangChain staff member replied.
- Not confirmed: the guidelines page contents and any moderation policy. Describe it only as "the official LangChain forum, with staff replies", not as "well moderated". It centres on the LangChain tools, so say so.
- May the writer cite it? Yes, as a verified community, described as above.

## Not kept
- r/LocalLLaMA, r/LangChain, r/ClaudeAI and the Anthropic Discord: the plan names them, but I did not open them. Search showed only third-party Reddit mirror pages, which I cannot confirm. Do not link them.

## Claims with no support, for the writer
- Clearing leaves a stub and the result can be re-fetched, said to be "described in the docs": not found. Make it the lesson's own advice.
- The E-42 query: the lesson's own example. The source uses TS-999.
- Dollar figures, token counts, the 67 times saving, the Dana trace: invented for the lesson. Label as made up.
