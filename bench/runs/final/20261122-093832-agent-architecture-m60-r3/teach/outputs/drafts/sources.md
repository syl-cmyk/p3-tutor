# Sources check for O3 (context and memory in an agent)

Every page below was opened with WebFetch in this session, at the address in the plan. None showed a redirect. Two pages (the engineering post and the contextual retrieval post) did not print their own address in the fetched text, so "final address" means the address I opened.

## 1. Effective context engineering for AI agents (PRIMARY SOURCE)
- Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened; dated Sep 29, 2025)
- Smallest set of high-signal tokens: SUPPORTED. "find the smallest set of high-signal tokens that maximize the likelihood of your desired outcome."
- Recall degrades as context grows: SUPPORTED. "the model's ability to accurately recall information from that context decreases." The fetch did not confirm the words "context rot" on this page. Take that term from source 2, which names it.
- Lightweight identifiers, just-in-time loading: SUPPORTED. Agents "maintain lightweight identifiers (file paths, stored queries, web links, etc.)" and load data at runtime.
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents."
- Structured note-taking outside the window: SUPPORTED. The agent "regularly writes notes persisted to memory outside of the context window."
- Sub-agents return condensed summaries: SUPPORTED. "returns only a condensed, distilled summary of its work."
- Cite: yes. It is the best single source, from the vendor's engineering team.

## 2. Context windows (Claude docs)
- Address: https://platform.claude.com/docs/en/build-with-claude/context-windows (opened)
- Window is all text the model can reference, including its reply: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself."
- Each turn's input includes all history: SUPPORTED. "Input phase: Contains all previous conversation history plus the current user message."
- System prompt, messages, tool results, tool definitions all count: SUPPORTED. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results...), and your tool definitions."
- Context rot: SUPPORTED. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Compaction and context editing (tool result clearing): SUPPORTED. "Tool result clearing: Clear old tool results in agentic workflows." Server-side compaction is "available in beta for Claude 4.6 and later models". Say it is a beta feature.
- Multisession tip: SUPPORTED. "For agents that span multiple sessions, design your state artifacts so that context recovery is fast when a new session starts."
- Sonnet 5.5 gets no injected token-budget tags: SUPPORTED. The page lists Claude Sonnet 5.5 among models that "don't receive these injected tags", so the plan's warning is right.
- Caching still counts toward the window: SUPPORTED. "prompt caching changes what you pay for those tokens, not whether they count."
- Sonnet 5.5 has a 1M-token window: SUPPORTED.
- Cite: yes. Primary for Part 1.

## 3. Memory tool (Claude docs)
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened)
- Files under /memories persist between sessions: SUPPORTED. "files that persist between sessions"; Claude "stores what it learns in files under `/memories` and reads them back in later conversations."
- Client-side; Claude asks and the app runs it, returning a tool_result: SUPPORTED. "Claude only requests memory operations. Your application runs each request... and returns the result in a `tool_result` block."
- Commands view, create, str_replace, insert, delete, rename: SUPPORTED. All six have sections under "Tool commands".
- Safeguards: SUPPORTED. Path traversal: "Your implementation must validate every path in every command". Sensitive data: "Claude usually refuses to write sensitive information to memory files. For stronger guarantees, add validation". The page also advises capping file sizes and expiring old files.
- Pairing with compaction: SUPPORTED. "compaction keeps the active context small... and memory preserves the information that must survive summarization."
- System prompt tells it to check memory first: SUPPORTED, with one fix. The API adds this instruction itself ("ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE"). The plan's "the system prompt says to check memory first" is true, but the app does not have to write it.
- Not on the page: a note about training status going stale, "save everything" harms, and "system of record". These are the lesson's own advice. Do not cite them to this page.
- Cite: yes. Primary for Part 4.

## 4. Introducing Contextual Retrieval
- Address: https://www.anthropic.com/news/contextual-retrieval (opened; dated Sep 19, 2024)
- Chunking: SUPPORTED. "smaller chunks of text, usually no more than a few hundred tokens."
- Embeddings: SUPPORTED. "convert these chunks into vector embeddings that encode meaning."
- BM25: SUPPORTED. "a ranking function that uses lexical matching to find precise word or phrase matches."
- Chunks lose context: SUPPORTED. They "often destroy context."
- Top-K: PARTLY. The page says "Passing the top-20 chunks to the model is more effective than just the top-10 or top-5." It does not say 3 chunks is right. The plan's "top 3" is the lesson's own illustration.
- Failure rates: SUPPORTED. Top-20 retrieval failure fell from 5.7% to 3.7% with Contextual Embeddings, and to 2.9% with Contextual BM25 added.
- Under 200,000 tokens can go in the prompt: PARTLY. The page says that if the knowledge base is "smaller than 200,000 tokens" it can go directly in the prompt without RAG. I did not confirm the page's words about caching, so do not claim "with caching" is the source's own phrase unless the writer rechecks.
- Not on the page: the vinyl/PVC example, or an "LC-40" exact-name case. These are the lesson's illustrations. The page does support the general point that BM25 matches exact words.
- Cite: yes. Primary for Part 3.

## 5. Pricing (Claude docs)
- Address: https://platform.claude.com/docs/en/about-claude/pricing (opened)
- Input and output priced separately per million tokens: SUPPORTED. The table lists Base input and Output per MTok.
- Sonnet 5.5 at $2 input and $10 output per MTok: SUPPORTED. Output costs more per token.
- Tool use adds to input: SUPPORTED. Input includes the `tools` parameter, `tool_use` blocks and `tool_result` blocks.
- Cache read 0.1x on most models, 0.05x on Sonnet 5.5: SUPPORTED. Sonnet 5.5 cache hit is 0.05x, $0.10 per MTok.
- "10 kB page is about 2,500 tokens": SUPPORTED. "Average webpage (10 kB): ~2,500 tokens", under the web fetch tool section. The "about 4 characters per token" rule is the lesson's arithmetic on that figure, not a quote.
- Tokenizer note: the page says Claude 4.7 and later give about 30% more tokens for the same text. The 4-characters rule is therefore only rough for newer models.
- "its own worked example": PARTLY. The only worked example is for a Managed Agents session on Opus 5.5 (50,000 input, 15,000 output). It is not a four-call agent trace. The plan's $0.019 sum is the lesson's own arithmetic at the page's rates.
- Cite: yes. Rates change, so the lesson should call them an example and tell Riley to check the page.

## 6. Token counting (Claude docs)
- Address: https://platform.claude.com/docs/en/build-with-claude/token-counting (opened)
- Count before sending: SUPPORTED. "determine the number of tokens in a message before you send it to Claude."
- Estimate: SUPPORTED. "The token count is an **estimate**."
- Free: SUPPORTED. "Token counting is **free to use**" (it has its own rate limits).
- About 30% more tokens on newer tokenizers: SUPPORTED. "approximately 30 percent more tokens than on earlier models" for Claude 4.7 and later.
- Cite: yes.

## 7. Community (found through search, then opened)
- Address: https://claude.com/fr/community (opened; the English text is on a /fr/ path; I could not confirm a better address)
- What I saw: Anthropic's own Community page. It lists a "Claude Discord" ("Real-time help, project sharing, and active discussions with thousands of developers"), community events run by Claude Community Ambassadors, and a link to the r/ClaudeAI subreddit.
- Not opened: the Discord invite link on that page (https://discord.com/invite/6PPFFzqPDZ) and r/ClaudeAI itself. Describe them only as "listed on Anthropic's community page". I cannot say how well either is moderated.
- Fit: it is vendor-run and general, not agent-specific. My search found no Discord aimed only at agent builders. The unofficial r/claudecode Discord appeared in search results but I did not open it, so do not list it.
- Cite: yes, as "Anthropic's community page", for asking questions after the lesson. The mission puts comparing vendors out of scope, so do not frame it as a comparison.

## Claims the writer must leave out or word as the lesson's own advice
- "Context rot" as a named term on the engineering post: take it from source 2 instead.
- "Top 3 chunks" as a recommendation: the source says top-20 works better. Say 3 is a small illustration.
- Notes going stale, "save everything" harms, system of record: the lesson's own advice. No source says them.
- The $0.019, $0.16 and $0.023 figures, and the 79,870 and 11,470 token totals: the lesson's own arithmetic at the pricing page's rates, on invented illustrative sizes.
- "Prompt caching with a knowledge base under 200,000 tokens": the "with caching" part was not confirmed on the page.
- "Pricing page's own worked example" for the trace: no such example exists. Do not claim it.
