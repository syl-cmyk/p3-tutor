# Sources for O3 (context and memory in an agent)

All five pages were opened with WebFetch in this session, at the address written below. None redirected. The two anthropic.com pages did not print their own address in the text, but the fetch of the address below succeeded and returned the matching article.

## 1. PRIMARY. Anthropic Engineering, "Effective context engineering for AI agents"
Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
May the writer cite it: yes.

- Context is finite and recall falls as it fills: SUPPORTED. "Context, therefore, must be treated as a finite resource with diminishing marginal returns." The model's ability to recall information "decreases" as tokens grow. (The words "context rot" are on the context-windows page, source 2, not confirmed here. Cite source 2 for the term.)
- Keep light references, load on demand (just-in-time): SUPPORTED. Agents keep "lightweight identifiers (file paths, stored queries, web links, etc.)" and load data at runtime with tools.
- Compaction (summarize, then new window) and clearing old tool results: SUPPORTED. Tool result clearing is called "one of the safest lightest touch forms of compaction."
- Structured note-taking outside the window: SUPPORTED. The agent saves notes outside its context window and pulls them back in later.
- Sub-agents return short summaries (teaser): SUPPORTED. A sub-agent "returns only a condensed, distilled summary of its work."

## 2. Claude API docs, "Context windows"
Address: https://platform.claude.com/docs/en/build-with-claude/context-windows
May the writer cite it: yes.

- Window is all text the model can reference, including its reply: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself."
- Previous turns accumulate: SUPPORTED. "each user message and assistant response accumulates within the context window, and previous turns are preserved completely."
- System prompt, messages, tool results, tool definitions all count: SUPPORTED. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results, images, and documents), and your tool definitions."
- Up to 1M tokens on current models: SUPPORTED. "up to 1M tokens, depending on the model"; Claude Sonnet 5.5 is on the 1M list.
- Context rot, "more context isn't automatically better": SUPPORTED. "more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Compaction and tool-result clearing: SUPPORTED. Server-side compaction summarizes earlier turns; context editing offers "Tool result clearing: Clear old tool results in agentic workflows."
- Cached prefixes still occupy the window: SUPPORTED. "prompt caching changes what you pay for those tokens, not whether they count."
- Not supported here: nothing in the page says a model "has no memory between calls" in those words. It says the window is the model's "working memory" and that the history is sent as input each turn ("Input phase: all previous conversation history plus the current user message"). Word the "nothing persists inside the model" line as the lesson's own explanation, resting on that sentence.

## 3. Claude API docs, "Memory tool"
Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
May the writer cite it: yes.

- Client-side; model requests, app runs: SUPPORTED. "Claude only requests memory operations. Your application runs each request against storage you control."
- Files under /memories persist between sessions: SUPPORTED. "files that persist between sessions".
- "Assume interruption" and that the API adds it: SUPPORTED. Page text is "ASSUME INTERRUPTION: Your context window might be reset at any moment..." (capitals), and "the API automatically adds this instruction to the system prompt."
- View-first protocol: SUPPORTED. "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE."
- Return string for create: SUPPORTED. "File created successfully at: {path}".
- Security: SUPPORTED. Path traversal ("Validate that all paths start with /memories"), sensitive information, file size cap, memory expiration.
- Keep the directory organized, expire old files: SUPPORTED. "keep the memory directory organized"; "Periodically delete memory files that haven't been accessed in a long time."
- Multisession progress-log pattern: SUPPORTED. Progress log read at the start, updated before the session ends.
- Pairing with compaction: SUPPORTED. "memory preserves the information that must survive summarization."
- Not supported: the lesson's file name `/memories/students/riley.md` and the student example are the lesson's own. The page's example is a customer-service ticket. Do not present the makerspace case as from the page.

## 4. Anthropic Engineering, "Introducing Contextual Retrieval"
Address: https://www.anthropic.com/engineering/contextual-retrieval
May the writer cite it: yes, with the wording limits below.

- Chunks of a few hundred tokens: SUPPORTED. Documents are split "usually no more than a few hundred tokens".
- Embeddings vs BM25: SUPPORTED. Embeddings "can miss crucial exact matches"; BM25 handles exact terms.
- BM25 and error codes: PARTLY SUPPORTED. The page gives the example of a query with a unique identifier, the error code "TS-999". I did not confirm the exact sentence "works well for unique identifiers such as an error code". Do not put that in quotation marks. Say "BM25 is useful for exact terms such as an error code".
- Real systems combine both: SUPPORTED. Contextual Embeddings and Contextual BM25 together cut retrieval failures by 49%, and reranking brings it to 67%. (Combining is the article's recommended approach, not a claim about all real systems. Word it as "the article combines both".)
- Chunks lose context: SUPPORTED. Traditional RAG "often destroy[s] context", so a chunk may not say which company or period it is about. The fix of attaching a note naming the source is the article's whole idea (contextual retrieval).
- Under about 200,000 tokens, include everything and cache: SUPPORTED. "smaller than 200,000 tokens (about 500 pages of material)"; prompt caching makes this faster and cheaper.
- Baseline top-20 failure 5.7%: SUPPORTED. "Without Contextual Retrieval, the top-20-chunk retrieval failure rate was 5.7%." Say "in the article's tests"; it is a figure for their datasets.
- Top-K chunks added to the prompt: not separately checked in this read. Leave out the phrase "top K", or say "the best few chunks".
- Plan's "400 tokens per page" is the plan's own arithmetic (200,000 / 500). The page gives only the 200,000 and 500 pages. Label it "about" and "say".

## 5. Claude API docs, "Pricing"
Address: https://platform.claude.com/docs/en/about-claude/pricing
May the writer cite it: yes.

- Claude Sonnet 5.5 at $2 input and $10 output per MTok: SUPPORTED (table). Output is 5 times the input price here.
- Cache read at a fraction, 0.1x on most models and 0.05x on Sonnet 5.5: SUPPORTED. "Cache read (hit): 0.1x base input price on most models"; Sonnet 5.5 is 0.05x ($0.10 per MTok).
- Tools and tool results count as input tokens: SUPPORTED. Tool use is priced on "the total number of input tokens sent to the model (including in the `tools` parameter)"; `tool_result` blocks add tokens.
- Average 10 kB web page is about 2,500 tokens: SUPPORTED. "Average webpage (10 kB): ~2,500 tokens". The "about 4 characters per token" is the plan's own division (10,000 / 2,500); the page does not say it. Write "works out to about 4 characters" and say it is rough.
- Newer tokenizer gives about 30% more tokens: SUPPORTED. "Claude 4.7 and later models ... approximately 30% more tokens for the same text."
- Token definition: SUPPORTED. "Tokens are pieces of text that models process." The same FAQ says the count depends on tokenizer, language and content, and points to the Token counting tool.
- Not on this page: a statement that Sonnet 5.5 is a "small budget" model. Say only that it is one example price.

## Claims no source supports (word as the lesson's own, or leave out)

- The made-up sizes: 400, 600, 15 and 1,015 tokens; 40 booking rows at 1,200 tokens; 1,500-token manual result; 120-page manual at 48,000 tokens; 3 chunks of 300 tokens. These stay labelled "say" or "for example".
- The sums and cost figures ($0.096, $0.0038, 25 times, 10,915, $0.022, 2,650, $0.01 notes file) are the lesson's arithmetic from the page prices. Recompute them.
- "Retrieval can miss the right page, so show the page used" is the lesson's advice, backed in part by the 5.7% figure.
- "A stale note is the same failure as an outdated chatbot fact" is the lesson's own point (no source says it).
- "Save the training status in notes, not the live calendar" is the lesson's design advice. The memory page supports only the mechanism.
- Sizes of an "about 3,000 tokens per call" typical request, and "5,000-token notes file", are illustrations.
- The exact quote "works well for unique identifiers such as an error code" (not confirmed, see source 4).
- The phrase "context rot" is confirmed on source 2 only.
- The plan lists no community or forum source, and none was opened. Do not name one.
