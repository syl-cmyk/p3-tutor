# Sources check for lesson 0001 (objective O3)

All pages below were opened with WebFetch in this session. No redirects were reported for any of them.

## Knowledge

### 1. PRIMARY. Anthropic, "Effective context engineering for AI agents"
Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
Cite: yes (primary).
- Context rot, finite attention budget: supported. "Studies on needle-in-a-haystack style benchmarking have uncovered the concept of context rot." and LLMs "have an 'attention budget'".
- "Smallest set of high-signal tokens": supported. "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."
- Just-in-time retrieval with lightweight pointers: supported. Agents "maintain lightweight identifiers (file paths, stored queries, web links, etc.)" and load data at runtime with tools.
- Compaction: supported. "Compaction is the practice of taking a conversation nearing the context window limit", summarizing it and starting a new window.
- Clearing old tool results as lightest form: supported. "One of the safest lightest touch forms of compaction is tool result clearing."
- Structured note-taking: supported. The agent "regularly writes notes persisted to memory outside of the context window", pulled back in later.
- Hybrid up-front and on-demand: supported. "the most effective agents might employ a hybrid strategy".

### 2. Claude API docs, "Context windows"
Address: https://platform.claude.com/docs/en/build-with-claude/context-windows
Cite: yes.
- Window is all text the model can reference, including its response; working memory: supported. "all the text a language model can reference when generating a response, including the response itself", "a 'working memory' for the model".
- Each turn's input is all earlier history plus the new message: supported. "Input phase: Contains all previous conversation history plus the current user message"; "previous turns are preserved completely" (bullet "Progressive token accumulation").
- System prompt, messages, tool results, tool definitions all count: supported. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results...), and your tool definitions."
- Up to 1M tokens: supported. "up to 1M tokens, depending on the model". Claude Sonnet 5.5 is listed with a 1M window.
- Accuracy and recall degrade (context rot): supported. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot." Also "curating what's in context [is] just as important as how much space is available".
- Compaction and tool-result clearing: supported. Server-side compaction (beta for Claude 4.6 and later) and context editing "Tool result clearing: Clear old tool results in agentic workflows".
- Prompt caching changes price, not whether tokens count: supported. "prompt caching changes what you pay for those tokens, not whether they count."
- Billing: supported on this page only for thinking tokens ("billed as output tokens once, when they are generated"; kept blocks "billed as input tokens, like the rest of the conversation history"). The plan says "the thinking docs"; this page says it. Word it as about thinking tokens, not as a general rule. The general statement "every call re-bills the whole history as input" is the lesson's own reasoning from "Input phase: all previous conversation history"; do not attribute the word "billed" to the page for ordinary messages.
- Note for writer: the page says server-side compaction is the primary strategy for long-running agents; the "context awareness" section applies to some models only. Not needed in the lesson.

### 3. Claude API docs, "Memory tool"
Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
Cite: yes.
- Persists across conversations as files under /memories: supported. "store and retrieve information across conversations in a directory of memory files"; "files under `/memories`".
- Client-side: supported. "Claude requests file operations, and your application runs them. You control where and how the data is stored".
- Six commands: supported. view, create, str_replace, insert, delete, rename are all documented.
- tool_use and tool_result flow: supported. Application "returns the result in a `tool_result` block".
- View memory first: supported. "Claude automatically checks its memory directory before starting a task"; the API adds "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE" to the system prompt. Word it as "the API adds an instruction to view memory first".
- Success message for create: supported exactly. "File created successfully at: {path}". The plan's Part 5 step 3 text is correct.
- Create on an existing path: the reference behavior returns "Error: File {path} already exists", though the tool description says "creates or overwrites". Keep the Monday example on a new path (it is).
- Safeguards: supported. Path traversal ("Your implementation must validate every path in every command"), file size ("cap how large a file can grow"), expiration ("Periodically delete memory files that haven't been accessed in a long time"), sensitive information ("Claude usually refuses to write sensitive information... add validation"). Word the sensitive-data point as "validate and strip sensitive data", not "do not store".
- Compaction plus memory: supported. "compaction keeps the active context small... memory preserves the information that must survive summarization."
- Partly supported: "memory keeps the window focused". The page says memory "keeps the active context focused on the current task".
- Not supported (lesson's own advice, label it so): that training status should live in a separate record; that model-written notes can be stale or wrong. The page does not say this.

### 4. Claude API docs, "Token counting"
Address: https://platform.claude.com/docs/en/build-with-claude/token-counting
Cite: yes.
- Counts of 14 and 403: supported. The system "You are a scientist" with user "Hello, Claude" returns `{ "input_tokens": 14 }`; the request with one `get_weather` tool and "What's the weather like in San Francisco?" returns `{ "input_tokens": 403 }`. Note: the 403 request has NO system prompt and has a different user message, so word it as "adding one small tool definition and a different question brings it to 403", not "adding a tool to the first request". The page does not say in prose that "tool definitions cost tokens"; it is the lesson's inference, backed by the context-windows page sentence above.
- Tokens as the unit for limits and costs: partly supported. The page says token counts help "Proactively manage rate limits and costs". It does not define tokens as "a word or piece of a word"; leave that as the lesson's own plain explanation, with no ratio.
- Estimate: supported. "The token count is an estimate."
- About 30 percent more tokens: supported. "Claude 4.7 and later models ... The same input text produces approximately 30 percent more tokens than on earlier models... Recount prompts against the model you plan to use".

### 5. Anthropic, "Introducing Contextual Retrieval"
Address: https://www.anthropic.com/news/contextual-retrieval
Cite: yes.
- Chunking, embeddings, BM25 with an error-code example: supported. The page gives the query "Error code TS-999" in a technical support database. (The fetch summary did not quote the BM25 sentence itself; the plan's "BM25 finds exact matches that meaning-search can miss" is the page's point, but quote only "Error code TS-999" and keep the BM25 wording general.)
- Chunks lose context: supported. The chunk "The company's revenue grew by 3% over the previous quarter" does not name the company or period.
- 200,000-token threshold: supported. Knowledge base "smaller than 200,000 tokens (about 500 pages of material)" can go in the prompt without RAG; prompt caching makes this faster and cheaper.
- 5.7% to 1.9%: supported. "reduced the top-20-chunk retrieval failure rate by 67% (5.7% → 1.9%)" for reranked contextual embeddings plus contextual BM25.
- Not on the page as read: "a few hundred tokens or fewer" for chunk size, and "retrieval keeps the window small". Treat those as the lesson's own description.

## Wisdom (Communities)

### 6. Claude Discord, listed on Anthropic's community page
Address of the listing page: https://claude.com/community (opened)
Join link as printed on that page: https://discord.com/invite/6PPFFzqPDZ (taken from the opened page; I did not open the invite itself)
Cite: yes, with the listing page as the address and the invite as the join link.
- What I saw: the page, on Anthropic's own site, describes the Claude Discord as "Real-time help, project sharing, and active discussions with thousands of developers." Reddit r/ClaudeAI at https://www.reddit.com/r/ClaudeAI/ is also listed there ("Long-form discussions, project showcases").
- What I could not confirm: a dedicated agent-building channel, channel names, or moderation rules. A DigitalOcean article says the server covers the API and Model Context Protocol, but that is a third-party description. The "33,930+ members" figure is unverified; do not quote it.
- Describe it as: "The official Claude Discord, linked from Anthropic's community page: a place to ask for help and share projects." Do not say it is moderated, agent-specific or a test of skills. Use it to ask a question or share a small build, which is the closest honest fit for "test your skill".

## Claims no source supports (leave out or word as the lesson's own advice)
- "Count the manuals' tokens first; start without retrieval if they fit; add retrieval for cost" is the lesson's advice. The source only gives the 200,000-token threshold and the caching point.
- Training status belongs in the makerspace record, not in notes; model-written notes can be stale. Lesson's advice.
- A token is "a word or a piece of a word". No opened page says this in those words; no tokens-per-word ratio.
- Chunk size "a few hundred tokens or fewer", and the "Set power to 60%" machine-label example, are the lesson's own.
- "Billing: input and output tokens are billed" for ordinary messages and "history is resent so each step costs more" are inferences. The opened pages give "billed" only for thinking tokens. The resend itself is supported ("all previous conversation history plus the current user message").
- Every makerspace token count is illustrative; none comes from a source.
