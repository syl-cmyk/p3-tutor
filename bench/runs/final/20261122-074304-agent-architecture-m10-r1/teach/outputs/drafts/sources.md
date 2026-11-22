# Sources check for O3 (context and memory in an agent)

All pages below were opened with WebFetch in this session.

## 1. PRIMARY: Anthropic Engineering, "Effective context engineering for AI agents"
Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (opens; the plan's address without "www" also opened, and the page did not state a redirect target, so use the www form, which the Claude docs also link to).

- Context is the set of tokens given to the model: SUPPORTED. "Context refers to the set of tokens included when sampling from a large-language model (LLM)."
- Context rot and attention budget: SUPPORTED. Recall accuracy falls as the window grows ("context rot"); LLMs have an "attention budget".
- Just-in-time retrieval with lightweight pointers: SUPPORTED. Agents "maintain lightweight identifiers (file paths, stored queries, web links, etc.)" and load data at runtime.
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents" and continuing with the summary.
- Tool result clearing: PARTLY SUPPORTED. Called "one of the safest lightest touch forms of compaction", so word it as a light form of compaction, not "the safest".
- Structured note-taking (to-do list, NOTES.md): SUPPORTED. "Like Claude Code creating a to-do list, or your custom agent maintaining a NOTES.md file".
- Hybrid approach: SUPPORTED. "the most effective agents might employ a hybrid strategy, retrieving some data up front for speed" (rest is just in time).
- "Do the simplest thing that works": SUPPORTED, as the authors' advice.
- NOT on this page as far as seen: short-term versus long-term split, "save_note" tools, cost per token. Those are the lesson's own framing.
May cite: YES. It is a vendor engineering post (Anthropic), describe it as that.

## 2. Claude Platform Docs, "Context windows"
Address: https://platform.claude.com/docs/en/build-with-claude/context-windows (opens, no redirect).

- Context window as working memory, distinct from training data: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself. This is different from the large corpus of data the language model was trained on, and instead represents a 'working memory'".
- Each turn re-sends history; output becomes part of next input: SUPPORTED. "Input phase: Contains all previous conversation history plus the current user message"; output "becomes part of the input for the next turn".
- Tool results and tool definitions count: SUPPORTED. "the system prompt, every message in messages (including tool results...), and your tool definitions. The output Claude generates ... counts too."
- More context not better; context rot: SUPPORTED. "more context isn't automatically better. As token count grows, accuracy and recall degrade, a phenomenon known as context rot."
- Compaction and tool result clearing: SUPPORTED. Server-side compaction summarizes earlier parts (beta); context editing lists "Tool result clearing: Clear old tool results in agentic workflows".
- Token counting API: SUPPORTED ("use the token counting API to estimate").
- Window sizes: SUPPORTED. 1M tokens for many current models (up to 1M, depending on the model); 200k for others such as Claude Sonnet 4.5.
- Multi-session agents: PARTLY. Tip says to design state artifacts for fast context recovery when a new session starts, and points to the memory tool; it does not describe "notes" in detail.
- NOT on this page: the definition of a token as about three-quarters of a word, and that you pay per token in and out (pricing is only linked). The writer should state those as the lesson's own plain wording, or leave out the 3/4 figure.
May cite: YES (official vendor docs).

## 3. Oracle agent memory page (https://docs.oracle.com/en-us/iaas/Content/generative-ai/memory.htm)
Not re-opened; the plan says it returned 404. Do NOT cite. Not kept.

## Community suggestion (Anthropic Discord, r/LocalLLaMA)
No URL was opened or searched here. Do not link it; name the design review itself.

## Claims no source supports (word as the lesson's own advice or leave out)
- The short-term (window) versus long-term (stored) labels, and "the model does not remember; the program stores and reloads" as a stated rule. Docs support the re-sending and the multi-session tip, not these labels.
- A token is roughly three-quarters of a word.
- The cost arithmetic (2,920 tokens, 1.7%, 30,000 old results, etc.) is the lesson's own illustration, not from any source.
- "No PVC or vinyl, chlorine gas (manual p. 14)" is an invented example; label it as such.
- Retrieval can miss and give wrong pages: lesson's own caution (sources only describe just-in-time loading).
- "Retrieval does not always use vector search": neither page was seen to say this; keep as the lesson's wording.
