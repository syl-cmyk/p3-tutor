# Sources for O3: context and memory in an agent

All four pages were opened with WebFetch in this session at the address written in the plan. None redirected.

## 1. PRIMARY. Effective context engineering for AI agents (Anthropic Engineering)
Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
May the writer cite it: yes.

- Context is the set of tokens given to the model: supported. "the set of tokens included when sampling from a large-language model (LLM)".
- Context rot, finite attention budget: supported. Recall "decreases" as context grows; models have an "attention budget".
- Smallest set of high-signal tokens: supported. "finding the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome".
- Gradual decline, not a cliff: supported. "a performance gradient rather than a hard cliff".
- Compaction: supported. Summarizing a conversation nearing the window limit and continuing in a fresh window.
- Structured note-taking: supported. The agent "regularly writes notes persisted to memory outside of the context window".
- Just-in-time retrieval with lightweight identifiers: supported. "lightweight identifiers (file paths, stored queries, web links, etc.)".
- Trade-off, slower and needs guidance: supported. "slower than retrieving pre-computed data"; without good guidance an agent can waste context on dead ends.

## 2. Context windows (Claude API docs)
Address: https://platform.claude.com/docs/en/build-with-claude/context-windows
May the writer cite it: yes.

- Window is all text referenced, including the response: supported. "all the text a language model can reference when generating a response, including the response itself"; also "different from the large corpus of data the language model was trained on".
- Turns accumulate, earlier turns preserved: supported. "previous turns are preserved completely"; the output "becomes part of the input for the next turn".
- System prompt, messages with tool results, tool definitions all count: supported. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results...), and your tool definitions."
- Context rot: supported. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot".
- Gradual, not a cliff: NOT on this page. Cite source 1 for that.
- Up to 1M tokens: supported, with a limit. "up to 1M tokens, depending on the model". Other models are 200k. Word it "up to 1M", as planned, not "all current models".
- Compaction and tool result clearing: supported. Server-side compaction (beta); "Tool result clearing: Clear old tool results in agentic workflows" under context editing.
- The page also says the output counts toward the window and that thinking tokens count. The plan does not need the thinking detail.
- Prompt caching exists: supported in one clause (it changes what you pay, not whether tokens count).

## 3. Memory tool (Claude API docs)
Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
May the writer cite it: yes.

- /memories directory: supported. "stores what it learns in files under `/memories`".
- Client-side: supported. "Claude only requests memory operations. Your application runs each request against storage you control and returns the result in a `tool_result` block."
- View then read flow: supported. The docs example views `/memories`, then views a file. An empty store is "not an error" (the plan's step 2 listing "empty" is fine, but the docs say the SDK local tool returns a header and one line for the root, so say "an empty listing" loosely).
- Create result text: partly. The docs' return is "File created successfully at: {path}". The plan's "File created successfully" is a shortened form; write the full text or say "a success message".
- System prompt instruction: supported. "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE" and "ASSUME INTERRUPTION: Your context window might be reset at any moment". The API adds it automatically.
- Keep the directory organized: supported, narrowly. The docs say Claude's tool description already tells it to keep the directory organized; a reinforcing prompt is offered.
- Size caps: supported. "Track memory file sizes and cap how large a file can grow."
- Expiry: supported. "Periodically delete memory files that haven't been accessed in a long time."
- Sensitive data: partly. "Claude usually refuses to write sensitive information"; for stronger guarantees add validation. Word it as "add validation", not "the docs recommend expiry" for sensitive data. Expiry is a separate item.
- Path safety: supported. Validate paths; a path like `/memories/../../secrets.env` is the warning.
- Pairing with compaction: supported. "memory preserves the information that must survive summarization".
- Not supported: no page text says a notes file is "the simplest way"; that is the lesson's own advice.

## 4. Introducing Contextual Retrieval (Anthropic)
Address: https://www.anthropic.com/news/contextual-retrieval
May the writer cite it: yes.

- Chunking: supported. Chunks "usually no more than a few hundred tokens".
- Embeddings versus BM25, exact codes: supported. The example is the query "Error code TS-999", where embeddings may return general error-code content and miss the exact string. The plan's "E-42" is the lesson's own example in the same pattern; do not attribute "E-42" to the post.
- 5.7% to 2.9%: supported, with the precise wording. "Combining Contextual Embeddings and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 49%" (5.7% to 2.9%). Say "top-20-chunk failure rate". Contextual embeddings alone: 5.7% to 3.7%.
- Contextual note on each chunk: supported. A short, chunk-specific explanation added to each chunk before it is embedded and indexed; typically 50 to 100 tokens.
- 200,000 tokens: supported. "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material)" the post suggests putting it all in the prompt; prompt caching makes this cheaper and faster.
- "Real systems combine both": partly. The post combines embeddings and BM25; say "this post combines both", not "real systems".

## Claims no source supports (leave out or word as the lesson's own advice)
- The 100-fold cut, 1% reaching the window, 3,890 tokens and every other makerspace number: invented examples, must be framed as "say" or "for example".
- "Cost grows faster than step count" for a long task: follows from the arithmetic; the docs say turns accumulate, not this inference. State it as the lesson's reasoning.
- Memory is "the simplest way" and "do not store sensitive data without checking" as a rule: the lesson's own advice, with the docs' narrower point as above.
- "Retrieval reads a fixed collection; memory is written by the agent": the lesson's own distinction. The docs only say the memory tool lets Claude create, read, update and delete files.
- Anthropic developer Discord: no page was opened for it. Do not cite one unless the writer finds and opens a real link.
