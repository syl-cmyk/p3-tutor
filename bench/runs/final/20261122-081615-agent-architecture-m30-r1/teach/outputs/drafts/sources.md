# Sources check for O3 (context and memory in an agent)

All pages below were opened with WebFetch in this session. No redirects were reported.

## Knowledge

### 1. PRIMARY: Anthropic Engineering, "Effective context engineering for AI agents"
Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Cite: yes. Primary source.
- Context engineering definition: supported. "Context engineering refers to the set of strategies for curating and maintaining the optimal set of tokens".
- Attention budget: supported (LLMs have an "attention budget" they draw on when parsing large context).
- Context rot: supported (named as a source of declining recall as tokens in the window increase).
- "smallest possible set of high-signal tokens": supported, the article's guiding principle.
- Just-in-time with lightweight identifiers: supported. Agents "maintain lightweight identifiers (file paths, stored queries, web links, etc.)" and load data at runtime.
- Hybrid approach: supported ("a hybrid strategy, retrieving some data up front for speed").
- Compaction: supported. "taking a conversation nearing the context window limit, summarizing its contents".
- Tool result clearing: supported, called one of the safest, lightest-touch forms of compaction.
- Structured note-taking: supported. The agent "regularly writes notes persisted to memory outside of the context window".
- Not checked on this page: the plan's "keep decisions and open problems, drop repeated output" detail. Word it as the lesson's own advice unless the writer re-reads the article.

### 2. Claude Docs, "Context windows"
Address: https://platform.claude.com/docs/en/build-with-claude/context-windows
Cite: yes.
- Context window = working memory, includes the response, different from training data: supported. "all the text a language model can reference when generating a response, including the response itself. This is different from the large corpus of data the language model was trained on, and instead represents a 'working memory'".
- Everything counts: supported. "the system prompt, every message in `messages` (including tool results, images, and documents), and your tool definitions. The output Claude generates for the turn... counts too."
- History resent each turn: supported. Input phase "Contains all previous conversation history plus the current user message"; the response "becomes part of the input for the next turn".
- Context rot: supported. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Up to 1M tokens: supported ("up to 1M tokens, depending on the model").
- Compaction: supported (server-side compaction, summarizes earlier parts; beta for Claude 4.6 and later).
- Tool result clearing: supported (context editing lists "Tool result clearing: Clear old tool results in agentic workflows").
- Partly supported or not on this page: the claim "cost follows tokens, so a longer history costs more on every later call". The page only says prompt caching changes what you pay and gives 1M pricing notes. Present the cost point as the lesson's own reasoning, or cite the pricing page after opening it.
- Plan wording: "models with up to 1M windows still show recall degradation" is the plan's inference. The page says degradation happens "as token count grows" and 1M is a window size. Word it that way.

### 3. Claude Docs, "Memory tool"
Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
Cite: yes.
- Client-side, Claude requests, your app runs: supported. "Claude only requests memory operations. Your application runs each request against storage you control and returns the result in a `tool_result` block."
- Files under `/memories`: supported.
- Commands view, create, str_replace, insert, delete, rename: supported.
- Create success text: supported, but the exact string is "File created successfully at: {path}". The plan's trace says "File created successfully". Use the full string or say "a success message".
- Check memory first: supported. "Claude automatically checks its memory directory before starting a task"; the system prompt says "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE."
- Pairing with compaction: supported. "memory preserves the information that must survive summarization."
- Security: supported. Restrict to `/memories`; cap file sizes; delete files not accessed in a long time; "Claude usually refuses to write sensitive information... add validation that strips sensitive data".
- Multisession pattern: supported (progress log, each new session opens by reading memory files).
- Create on an existing path: the page says create returns "Error: File {path} already exists" by reference behavior, but Claude's tool description says "creates or overwrites". The plan's `str_replace` update trace is fine.
- Not on this page (lesson's own advice): "official training status should come from the university system"; "do not save calendar availability". Label these as design opinion.

### 4. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks"
Address: https://arxiv.org/abs/2005.11401
Cite: yes. Cite for concepts only (it is a 2020 paper).
- Parametric memory (weights): supported. Models "store factual knowledge in their parameters."
- Non-parametric memory: supported. "a dense vector index of Wikipedia, accessed with a pre-trained neural retriever."
- Limits of parametric-only: supported. "providing provenance for their decisions and updating their world knowledge remain open research problems"; "their ability to access and precisely manipulate knowledge is still limited."
- Partly supported: the plan says RAG "was proposed to reduce" outdated facts and missing sources. The abstract names these as open problems that motivate the work but, as read, does not describe how RAG fixes them. Word it as "motivated by".
- Not supported by this page: the chunk/keyword/embedding steps, "fixed vs tool" wiring, and the "say not found" advice. The chunking steps come from the engineering article (just-in-time) or are the lesson's own advice. Label the keyword-versus-meaning-similarity line as a plain-words aside.

## Wisdom (Communities)

### 5. LangChain Forum (Discourse, run by LangChain)
Address: https://forum.langchain.com/
Cite: yes, with a limited description.
What the page shows: a Discourse forum run by LangChain, with categories Announcements, OSS Product Help, LangSmith Product Help, LangChain Academy, and "Talking Shop" ("general discussion about LangChain and building agentic applications"). A linked guidelines page (https://forum.langchain.com/guidelines, opened) says: the forum is community-run and the LangChain team does not monitor every post; discussions stay on technical topics; promotion or solicitation is grounds for an instant ban; search before posting; participants agree to a Code of Conduct.
What I could not confirm: how many moderators there are, how active it is right now (no post dates shown), and whether it is high-reputation. It is a vendor-run forum, so it leans toward LangChain tools and not agent design in general. Describe it only as "LangChain's official community forum, with a Talking Shop category for building agent apps and written guidelines that ban promotion". Do not call it "well moderated" or "high reputation".
Not used: r/LLMDevs and r/LocalLLaMA. Reddit could not be opened (WebFetch blocked reddit.com), and search showed only a mirror, so neither is kept.

## Claims in the plan that no opened source supports (leave out or word as the lesson's own advice)
- Cost per token grows with longer history, as a statement about pricing: not on the pages opened.
- The 40,000-token manual, 240,000 total, 1,025-token breakdown and every other token count: made-up numbers, label them so.
- Design opinions: save slow facts and look up fast ones, take official training status from the university system, tell the model to answer "not found in the manual".
- Keyword versus meaning-similarity search, and chunking into pages: not on the RAG abstract page.
- "RAG fixes outdated facts and missing sources": the abstract only names them as open problems.
