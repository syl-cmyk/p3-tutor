# Sources for O3: context and memory in an agent

Checked 2026-11-22. Every page below was opened with WebFetch in this session.

## 1. PRIMARY. Effective context engineering for AI agents
- Address as cited: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened; the tool could not report a final address, so cite the address as written; the Context windows doc links to https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents, which is the same post)
- Context is the tokens sampled: SUPPORTED. "Context refers to the set of tokens included when sampling from a large-language model (LLM)."
- Context rot and attention budget: SUPPORTED (attention budget). "LLMs have an 'attention budget' that they draw on when parsing large volumes of context." The term "context rot" was not confirmed on this page by the fetch; take that term from source 2.
- Just-in-time retrieval with lightweight references: SUPPORTED. "maintain lightweight identifiers (file paths, stored queries, web links, etc.)"
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents"
- Clearing old tool results as the lightest compaction: SUPPORTED. "One of the safest lightest touch forms of compaction is tool result clearing"
- Structured note-taking, NOTES.md: SUPPORTED. "...your custom agent maintaining a NOTES.md file"
- Tool results should be token-efficient: SUPPORTED. Tools promote efficiency "by returning information that is token efficient".
- Writer may cite: YES, as the primary source.

## 2. Context windows (Claude Platform docs)
- Address: https://platform.claude.com/docs/en/build-with-claude/context-windows (opened, no redirect)
- Window includes system prompt, messages, tool results, tool definitions and output: SUPPORTED. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results, images, and documents), and your tool definitions. The output Claude generates for the turn... counts too."
- History accumulates: SUPPORTED. "each user message and assistant response accumulates within the context window, and previous turns are preserved completely."
- Context rot: SUPPORTED. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Window is not training data: SUPPORTED. It is "different from the large corpus of data the language model was trained on" and is a "working memory".
- Up to 1M tokens: SUPPORTED, "up to 1M tokens, depending on the model"; the page lists Claude Sonnet 5.5, Opus 5.5 and others at 1M, and other models (for example Sonnet 4.5) at 200k. Word it "up to 1M on many current models", not "all".
- Compaction and context editing: SUPPORTED. Server-side compaction is "the primary strategy"; context editing offers "Tool result clearing: Clear old tool results in agentic workflows".
- Billing across calls (6,365 input tokens): the page says each input phase "contains all previous conversation history plus the current user message". The word "billed" for that is the lesson's own arithmetic; the page does not give a total.
- Writer may cite: YES.

## 3. Memory tool (Claude Platform docs)
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened, no redirect)
- Client-side: SUPPORTED. "Claude requests file operations, and your application runs them. You control where and how the data is stored."
- /memories folder, persists between sessions: SUPPORTED. "files that persist between sessions"; "stores what it learns in files under `/memories`".
- View before work: SUPPORTED. "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE."
- Security: SUPPORTED. Path traversal ("Your implementation must validate every path in every command"), file size cap ("Track memory file sizes and cap how large a file can grow"), expiration ("Periodically delete memory files that haven't been accessed in a long time").
- Multisession progress-file pattern: SUPPORTED. "Each new session opens by reading those memory files."
- Reply string "File created": the page gives "File created successfully at: {path}". Word the lesson's reply to match.
- Not on this page: the idea that a note can be stale or that an official record should win. That is the lesson's own advice.
- Writer may cite: YES.

## 4. Introducing Contextual Retrieval
- Address as cited: https://www.anthropic.com/engineering/contextual-retrieval (opened; the fetch could not report a final address and showed no redirect)
- Chunks, embeddings, BM25: SUPPORTED. "Break down the knowledge base... into smaller chunks of text"; BM25 complements embeddings for exact terms such as identifiers.
- Under 200,000 tokens, skip RAG: SUPPORTED. "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material)" you can include it all in the prompt; prompt caching makes that faster and cheaper.
- Chunk-context example: SUPPORTED, though with a different example (an SEC filing chunk prefixed with "This chunk is from an SEC filing on ACME corp's performance in Q2 2023."). The makerspace chunk is the lesson's own illustration of the same idea.
- 5.7% to 2.9%: SUPPORTED, with a condition. "Combining Contextual Embeddings and Contextual BM25 reduced the top-20-chunk retrieval failure rate by 49%" (5.7% to 2.9%). Say it is Anthropic's own reported test, not a guarantee for the makerspace.
- Writer may cite: YES.

## 5. Managing context on the Claude Developer Platform
- Address as cited: https://www.anthropic.com/news/context-management. It returns a 308 permanent redirect to https://claude.com/blog/context-management. Cite the final address.
- Opened at the final address.
- Memory is outside the window: SUPPORTED. "The memory tool enables Claude to store and consult information outside the context window through a file-based system."
- Context editing inside the window: SUPPORTED, in other words. It "automatically clears stale tool calls and results from within the context window when approaching token limits." The page says "clears", not "trims".
- 39% with both: SUPPORTED. "combining the memory tool with context editing improved performance by 39% over baseline."
- 29% with editing alone: SUPPORTED. "Context editing alone delivered a 29% improvement."
- Condition the writer must keep: the numbers are from "an internal evaluation set for agentic search", reported by Anthropic. Say "Anthropic reports", name that evaluation, and do not call it a general result. "Over baseline" is a relative performance gain on that test, not a percentage of tokens or of tasks.
- Writer may cite: YES, at https://claude.com/blog/context-management, with the wording above.

## 6. Community (the plan asked for one forum link)
- No official Anthropic forum for agent builders was found. The search said it "couldn't confirm a dedicated Anthropic forum for agent developers". Do not describe any link as a forum for testing skills.
- Opened: the Claude community page, reached through a search-result link: https://claude.com/redirect/claudeai.v1.3bfffdc2-8a57-40f6-8540-bf948a0256e9/community (the page did not state its own address; its relative link is /community, which is not confirmed). It lists two channels:
  - Discord: https://discord.com/invite/6PPFFzqPDZ, described there as "Real-time help, project sharing, and active discussions with thousands of developers."
  - Reddit: https://www.reddit.com/r/ClaudeAI/, described there as "Long-form discussions, project showcases, and community knowledge that sticks around."
- I did not open the Discord invite or the subreddit, so I cannot say how moderated they are, or that they hold agent-building challenges. What the writer may say: "the Claude community page lists a Discord and a subreddit where builders share projects and ask for help". The writer may link the Discord and Reddit addresses as "seen on the community page", not as a place to test skills.
- Third-party claim from search (not opened, do not use): that the Developer Discord has open Q&A on agent engineering.
- Writer may cite: the community page only, described as above.

## Claims the plan makes that no source supports (leave out or word as the lesson's own advice)
- "Context rot" as a term in the primary post: not confirmed there; cite source 2 for it.
- Total input billed 6,365 tokens, and "the manual page is half of call 3": the lesson's own illustrative arithmetic.
- That a note may go stale and that the official training record should win: the lesson's own advice.
- That the memory tool's reply is "File created": the page's text is "File created successfully at: {path}".
- "Windows up to 1M on current Claude models": only "up to 1M, depending on the model".
- That a forum exists for learners to test agent-building skills: not found.
