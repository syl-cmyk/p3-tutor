# Sources for O3: context and memory in an agent

All pages below were opened with WebFetch in this session, at the address shown. None redirected to a different address.

## 1. PRIMARY: Anthropic Engineering, "Effective context engineering for AI agents"
Address: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened, no redirect)

- Definition of context: SUPPORTED. "Context refers to the set of tokens included when sampling from a large-language model (LLM)."
- Context rot, attention budget: SUPPORTED. "the model's ability to accurately recall information from that context decreases"; "LLMs have an 'attention budget'".
- Gradient, not a cliff: SUPPORTED. "These factors create a performance gradient rather than a hard cliff".
- Compaction: SUPPORTED. "Compaction is the practice of taking a conversation nearing the context window limit, summarizing its contents..."
- Clearing old tool results: SUPPORTED. "One of the safest lightest touch forms of compaction is tool result clearing".
- Note-taking, reloaded later: SUPPORTED. "the agent regularly writes notes persisted to memory outside of the context window"; "After context resets, the agent reads its own notes and continues".
- Just-in-time retrieval: SUPPORTED. Agents keep lightweight identifiers (file paths, stored queries, links) and load content at runtime through tools.
- Sub-agents: SUPPORTED. A sub-agent "returns only a condensed, distilled summary of its work (often 1,000-2,000 tokens)".
- Not on this page: the lesson's own examples (laser cutter, allergic-to-resin summary). Word these as the lesson's own.

May the writer cite it: YES, as the primary source.

## 2. Claude Docs, "Context windows"
Address: https://platform.claude.com/docs/en/build-with-claude/context-windows (opened, no redirect)

- Window is everything the model can reference, including the reply: SUPPORTED. "all the text a language model can reference when generating a response, including the response itself".
- Previous turns carried forward as input: SUPPORTED. "Input phase: Contains all previous conversation history plus the current user message".
- System prompt, messages, tool results and tool definitions all count: SUPPORTED. "Everything in the request counts toward the context window: the system prompt, every message in `messages` (including tool results...), and your tool definitions."
- Context rot: SUPPORTED. "As token count grows, accuracy and recall degrade, a phenomenon known as context rot." The page does not say "gradient not cliff"; that is on source 1.
- Compaction and tool result clearing: SUPPORTED. Server-side compaction summarizes earlier turns (beta, Claude 4.6 and later); context editing offers "Tool result clearing: Clear old tool results in agentic workflows".
- Window size by model: SUPPORTED. Claude Sonnet 5.5 is in the list with a "1M-token context window"; other models, such as Sonnet 4.5, have 200k. Name the model if you give a size.
- Not on this page: the "program re-sends the transcript" wording for agent loops. The page speaks of API requests and turns; say "each request carries the history".

May the writer cite it: YES.

## 3. Claude Docs, "Memory tool"
Address: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened, no redirect)

- Files persist between sessions in `/memories`: SUPPORTED. "Claude can create, read, update, and delete files that persist between sessions"; "stores what it learns in files under `/memories`".
- Client-side: SUPPORTED. "The memory tool operates client-side: Claude requests file operations, and your application runs them. You control where and how the data is stored".
- Storage, such as a directory or database: SUPPORTED. `/memories` "is a prefix that your handler maps onto real storage, such as a per-user directory or keys in a database."
- Checks memory first: SUPPORTED. "Claude automatically checks its memory directory before starting a task"; the added system prompt says "ALWAYS VIEW YOUR MEMORY DIRECTORY BEFORE DOING ANYTHING ELSE."
- `create` command and its result: SUPPORTED, with a wording fix. The recommended return is "File created successfully at: {path}" (the plan says "File created successfully"; add "at: path"). The page says your application may return other strings.
- Multisession pattern: SUPPORTED. Each new session "opens by reading those memory files" and updates a progress log before it ends. The page frames this for software projects, so the training-status example is the lesson's own adaptation.
- Pairing with compaction: SUPPORTED. "compaction keeps the active context small... and memory preserves the information that must survive summarization."
- Retention and sensitive data: SUPPORTED. Security section: "Claude usually refuses to write sensitive information"; add validation; cap file size; "Periodically delete memory files that haven't been accessed in a long time." The ZDR note says "you control data retention".
- Not on this page: "keep a training status in a database instead of notes". That is the lesson's own advice (though the page does say the store may be a database).

May the writer cite it: YES.

## 4. Anthropic, "Introducing Contextual Retrieval"
Address: https://www.anthropic.com/news/contextual-retrieval (opened, no redirect)

- RAG definition: SUPPORTED. RAG "is a method that retrieves relevant information from a knowledge base and appends it to the user's prompt."
- 200,000 tokens, about 500 pages, skip retrieval: SUPPORTED. If the knowledge base is "smaller than 200,000 tokens (about 500 pages of material)", include it all in the prompt.
- 400 tokens per page: PARTLY SUPPORTED. The page never says it. It follows only by dividing 200,000 by 500. Call it "about 400 tokens a page, from 200,000 tokens being about 500 pages".
- Chunks and embeddings: SUPPORTED. Chunks are "usually no more than a few hundred tokens"; an embedding model turns them into vectors that encode meaning.
- Chunk loses context: SUPPORTED. The page's example is "The company's revenue grew by 3% over the previous quarter", which names neither company nor period. The "6 mm laser cutter" chunk is the lesson's own example of the same idea; do not attribute it to the page.
- Failure rates: SUPPORTED. These measure "1 minus recall@20" (relevant documents missed in the top 20 chunks): 5.7% baseline, 3.7% with Contextual Embeddings, 2.9% with Contextual Embeddings plus Contextual BM25, 1.9% with reranking added. The plan's "1.9% with the full combination" must say "with reranking added". Say these are the source's own tests.
- Keyword matching for exact terms: SUPPORTED. BM25 "is particularly effective for queries that include unique identifiers or technical terms"; the example is "Error code TS-999". Use that wording; the plan's "E-17" is the lesson's own example.

May the writer cite it: YES, with the two wording fixes above (reranking; 400 per page is derived).

## 5. Community page (Wisdom): Hugging Face Agents Course, Discord community
Addresses opened:
- https://huggingface.co/learn/agents-course/en/unit0/discord101 (opened, no redirect)
- https://huggingface.co/learn/agents-course/en/unit0/introduction (opened, no redirect)

What I saw: the course is run by Hugging Face. The discord101 page lists course channels on the Hugging Face Community Discord: `agents-course-questions` ("ask questions and help your classmates"), `agents-course-showcase` ("show your best agents"), plus announcements, general and a `smolagents` library channel. The introduction page says learners "put your agent to compete against other agents in a challenge", with a leaderboard to "compare the agents' performance", and suggests joining Discord study groups.

Verdict: SUPPORTED as a place where learners can test agent-building skills (challenge with a leaderboard, showcase and questions channels). I did not open the Discord server itself, so I cannot vouch for its moderation or size; the discord101 page does not mention the challenge. A search snippet said "over 100,000 members" but I did not confirm it on a page I opened, so do not state it. This is a course community, not a general forum; describe it that way. Search results also showed forum threads (discuss.huggingface.co) about trouble getting into the course Discord; I did not open them.

May the writer cite it: YES, described only as above, with the two page addresses.

## Not supported by any source (leave out or word as the lesson's own advice)
- All token counts in the traces, the makerspace figures, and the cost arithmetic (480,000; 2.4 million): illustrative; label as such.
- The laser cutter vs 3D printer mix-up, the allergy-in-summary example, "needs the 40 W laser": the lesson's own cases.
- "Clearing loses listings but they can be re-fetched" and "tell the summary what must survive": the lesson's own advice. Source 1 supports only that tool result clearing is a light form of compaction.
- "Keep notes short and organized" because notes cost tokens when read: the memory tool page says Claude keeps its directory organized and suggests capping `view` output; the token-cost point is the lesson's own reasoning.
- "Retrieval means the model does not learn the manuals; replace the manual and the next answer changes": the lesson's own reasoning from RAG appending text to the prompt.
- "A token is roughly three-quarters of a word": not on any opened page. Leave out or call it a rule of thumb.
- "The program always retrieves first, or search_manual is a tool": the lesson's own framing.
- "Prices vary": not checked; the lesson's own caution.
