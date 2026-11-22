# Sources check: O3 (context and memory in an agent)

All four URLs were opened with WebFetch in this session, exactly as written. None redirected. All four are Anthropic first-party pages (engineering blog, product docs, company news).

## 1. PRIMARY. Effective context engineering for AI agents
- Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- Cite: yes.
- Context is a finite resource: SUPPORTED. "Context, therefore, must be treated as a finite resource with diminishing marginal returns."
- Context rot: SUPPORTED. The page says the model's ability to accurately recall information from context decreases as the window fills.
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents" and starting a new window with the summary.
- Clearing old tool results: SUPPORTED. Called the lightest form of compaction, "tool result clearing".
- Notes outside the window: SUPPORTED. "the agent regularly writes notes persisted to memory outside of the context window."
- Just-in-time retrieval and its trade-off: SUPPORTED. The agent loads data at runtime with tools. "runtime exploration is slower than retrieving pre-computed data."
- Wording caution: the page's term is "context rot" and the fixes it names are compaction, tool result clearing and note-taking. The plan's "accuracy falls" is close; safer to say "the model's recall gets worse".

## 2. Memory tool
- Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
- Cite: yes.
- Client-side, the app runs the operations: SUPPORTED. "The memory tool operates client-side: Claude requests file operations, and your application runs them. You control where and how the data is stored."
- `/memories` directory and `view` and `create` commands: SUPPORTED (commands view, create, str_replace, insert, delete, rename; files under `/memories`).
- Persists across conversations: SUPPORTED. "store and retrieve information across conversations ... files that persist between sessions".
- Model checks memory first: SUPPORTED. "Claude automatically checks its memory directory before starting a task." The first call is `view /memories`, as in the plan's Thursday trace.
- Paired with compaction: SUPPORTED. "memory preserves the information that must survive summarization."
- Team decides storage, size and lifetime: SUPPORTED. The page tells the app to cap file size and expire old files.
- Caution: `create` returns an error if the file exists (overwriting is allowed as an implementation choice). The plan's one-line `create /memories/riley.md` trace is fine. The lesson's "model" here is Claude. Say "the memory tool" is one way, not the only way.

## 3. Context windows
- Address: https://platform.claude.com/docs/en/build-with-claude/context-windows
- Cite: yes.
- Window contents: SUPPORTED. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results ...), and your tool definitions. The output Claude generates for the turn ... counts too."
- Window is not training: SUPPORTED. It "is different from the large corpus of data the language model was trained on, and instead represents a 'working memory'".
- History accumulates, resent each turn: SUPPORTED. "Input phase: Contains all previous conversation history plus the current user message"; previous turns are preserved completely.
- Context rot: SUPPORTED. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Sizes: SUPPORTED. "up to 1M tokens, depending on the model"; other models, 200k. Plan rule (do not fix sizes) is right: the page lists many models.
- Tool result clearing and compaction named: SUPPORTED.
- Does NOT say: the token is about three-quarters of a word; the lesson's 300, 700 and 2,000 token figures; that billing is per resent step. The cost point (input billed again each call) follows from the page's description of resent history but the page does not state it in those words. Word it as the lesson's own explanation.

## 4. Introducing Contextual Retrieval
- Address: https://www.anthropic.com/news/contextual-retrieval
- Cite: yes.
- Chunks of a few hundred tokens: SUPPORTED. Chunks "usually no more than a few hundred tokens".
- Retrieved chunks go into the prompt: SUPPORTED. "the most relevant chunks are added to the prompt sent to the generative model."
- Keyword plus meaning: SUPPORTED. Embeddings "can miss crucial exact matches"; BM25 is "particularly effective for queries that include unique identifiers or technical terms"; combining the two improves retrieval.
- 200,000 tokens: SUPPORTED. "If your knowledge base is smaller than 200,000 tokens (about 500 pages of material)" you can put it all in the prompt, and caching makes this "significantly faster and more cost-effective". The page gives it as a tip, not a rule.
- Caution: the article is about Anthropic's own "contextual retrieval" method. Cite it only for the points above, not for retrieval in general.

## Claims no source supports (leave out or word as the lesson's own advice)
- A token is roughly three-quarters of a word, a page is a few hundred tokens: no opened page says it. Leave out or call it a rough rule of thumb of the lesson.
- All token counts (300, 700, 2,000, 30,000, 900, 8,800 and so on) and the cost arithmetic: illustrative, the lesson's own. Label them illustrative.
- "A bigger window is not free because the manual is paid again each step": the lesson's own reasoning. The context-windows page supports resent history and context rot, not the pricing arithmetic.
- The "Retrieval vs notes are not the same thing" distinction: the lesson's own framing (the memory tool page does call memory "just-in-time context retrieval", so word it carefully).
- The Part 5 sorting rules of thumb (notes vs window vs retrieval): the lesson's own advice, loosely supported by sources 1 and 2.
- Community suggestion (r/LocalLLaMA, Anthropic developer community): not opened or searched. Do not cite or list as a community until a page is opened.
