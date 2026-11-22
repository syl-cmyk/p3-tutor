# Plan: lesson for O3 (60 minutes, about 9,000 words)

File to write: `lessons/0001-context-window-and-memory.html` (next number in `lessons/`, which is empty). Meta tags: `p3-minutes` = 60, `p3-objective` = O3.

Note on numbering: the learner's quiz 0001 is about the agent loop, but numbering is per folder, so the lesson is still 0001. Link back to the agent-loop learning record only in the warm-up (there is no earlier lesson file).

**Title:** Context and memory: what an agent can see on each call, and what it can keep

**Win (general):** After this lesson, anyone can decide for an agent what goes into its context window on each call, what gets saved between sessions, and how it finds one fact in a large body of text.

**Primary source:** Anthropic engineering, "Effective context engineering for AI agents" (https://anthropic.com/engineering/effective-context-engineering-for-ai-agents). It covers the window, context rot, just-in-time retrieval, compaction and note-taking in one place, and every other source supports one of its claims.

**Learner fit (from PREFERENCES.md and NOTES.md):** example first, then the idea; real numbers worked step by step; agent traces (user says, tool picked, result, reply); casual voice; short paragraphs. Riley knows the loop (record 0002) and that a model maps text in to text out (record 0001). Riley has NOT been taught tokens, so the lesson must define token before the window. Riley has not called a model from code, so describe API calls in plain words, with at most a three-line Python-shaped sketch of the `messages` list. Budget matters, so cost is a thread through every part.

**Running example, used in every part:** the makerspace assistant. Request: "Is the laser cutter free on Friday?" and its follow-ups. Fixed illustrative numbers (state once, in part 1, as made-up round numbers for the lesson, not measurements):
- system prompt 800 tokens; three tool definitions (search_manual, check_calendar, book_slot) 600 tokens total; user question 30 tokens.
- calendar tool result 350 tokens; assistant's tool request 40 tokens; final reply 60 tokens.
- one machine manual: 120 pages, about 500 tokens a page, so 60,000 tokens; the makerspace has 15 manuals, about 900,000 tokens (assumed).
- illustrative price: $2 per million input tokens and $10 per million output tokens (the same order as Claude Sonnet 5.5 on the pricing page; tell the learner to read the real price from the pricing page).

## Opening and warm-up (unheaded) — 450 words
- Title, 60 minutes, the win in one sentence, one or two sentences tying it to the mission goal "decide what the assistant keeps in context, what it saves between sessions, how it finds the right page".
- Warm-up, answers on demand: (1) In the agent loop, who runs the tool, the model or the program? (2) What did the model have to go on besides its training? (record 0001: only the text it is given.) Both set up part 2.
- Extra detail goes in: a one-line map of the lesson (window, what is kept per step, trimming, retrieval, notes, design).

## Part 1: Context window: the text the model can see on one call — 1,350 words
- **Key sentence:** The model knows only the text you hand it on each call, and there is a limit on how much text that can be. So the first thing to learn is what that text is made of and how it is counted.
- **Example (worked trace of one call):** the call that carries "Is the laser cutter free on Friday?". Add up what is in it: system prompt 800 + tool definitions 600 + question 30 = 1,430 input tokens; the model's output is a tool request of 40 tokens. Show the real shape: a list of messages the program builds. Define token (a piece of text, a few characters to a short word; rough rule about three-quarters of a word, 100 tokens is about 75 words; cite pricing page FAQ that the count depends on the model's tokenizer) at the point it first appears. Define context window (everything in the request plus the reply the model writes) and the size (up to 1M tokens on current models, 200k on others; cite the context-windows page, and say the learner should check the model table for the model the team picks).
- **Figure 1** (after the definition of context window): a stacked horizontal bar "one call". Segments with exact numbers: "Instructions to the assistant (system prompt): 800", "Tool descriptions: 600", "Student's question: 30", then an empty hatched segment "Room left for everything else" and a separate small box "Reply the model writes: 40 (also counts)". Arrow from the bar to a box "Model": reason "all of it is read together". Label each box in plain words, no jargon.
- **Misconceptions to name:**
  1. "The window is just my message." Real case: in the call above, the student's own words are 30 of 1,430 tokens, about 2%; instructions and tool descriptions are the rest (docs: system prompt, tool definitions and tool results all count).
  2. "Output is free / doesn't count." The 40-token tool request and the 60-token reply count in the window and are billed at the higher output rate ($10 vs $2 per million in the example).
- **Sources:** context-windows doc (definition, everything counts, sizes); pricing page (input vs output price; tokenizer note; tool-use token overhead); primary source (definition of context as "the set of tokens included when sampling").

## Part 2: Message history: what is kept between steps, and what it costs — 1,450 words
- **Key sentence:** The model does not remember anything between calls; the program sends the whole history again each time. That is why every step of the loop gets more expensive than the last.
- **Example (numbered trace, two calls of the same request):**
  1. Call 1 input 1,430 tokens; model asks for check_calendar (40 tokens out).
  2. The program (not the model) runs the tool; the result is 350 tokens.
  3. Call 2 input = 1,430 + 40 + 350 = 1,820 tokens; model writes the 60-token reply "Friday 2 to 4 pm is free."
  4. Total input billed across the request = 1,430 + 1,820 = 3,250 tokens; output 100 tokens; cost = 3,250 x $2/M + 100 x $10/M = $0.0065 + $0.0010 = $0.0075.
  Then a second student message the next minute ("Book 2 pm"): input now includes everything before it, so it starts above 1,900 (1,820 + 60 + new question); show the arithmetic with a made-up 20-token question: 1,820 + 60 + 20 = 1,900.
  Second contrast, same request but the whole 60,000-token manual is pasted into the prompt every call: call 1 = 61,430, call 2 = 61,820, total input 123,250 tokens, cost = $0.2465 + $0.0010 = $0.2475, which is 33 times the $0.0075. This sets up retrieval in part 4 without naming it yet.
  Mention in a margin note: prompt caching makes repeated prefixes cheaper (reads at a fraction of the input price, 0.1x on most models; 0.05x on Sonnet 5.5) but they still fill the window (cite pricing page and context-windows page: "cached prompt prefixes still occupy the context window"). Do not teach caching further.
- **Figure 2** (after the trace): two stacked bars side by side, "Call 1: 1,430 in" and "Call 2: 1,820 in", with Call 2's extra pieces labelled "Model's tool request: 40" and "Calendar answer: 350"; arrow from call 1's bar to call 2's bar, reason "program adds what happened and sends it all again". Third bar for the pasted-manual version at 61,820 drawn with a broken axis or a scale note, labelled "Same call with the whole manual pasted in: 61,820".
- **Misconceptions:**
  1. "The model remembers the earlier steps by itself." Real case: delete the 350-token calendar result from the list and call 2 cannot know Friday's slots; the model is a function of the text it receives (ties to record 0001). Say plainly that model weights do not change during a chat.
  2. "Cost is per question." Cost is per call, and each call re-reads the history: the 3,250 vs 1,430 figures.
- **Sources:** context-windows doc (progressive token accumulation, each turn's input is all previous history plus new message; output becomes next input); memory-tool doc (client-side: the application runs the operations and returns tool_result); pricing page (input/output rates, cache multipliers, tool_use and tool_result tokens count as input).

## Part 3: Context rot and trimming: keeping the window small and useful — 1,300 words
- **Key sentence:** A bigger window does not mean better answers, because the model gets worse at using text as the window fills. So you keep the smallest set of useful text in it and trim the rest as the work goes on.
- **Example (trace of a long session):** a student spends 40 turns configuring a booking series; history reaches 38,000 tokens (illustrative), 30,000 of it old tool results (calendar dumps of 350 tokens each re-fetched, long manual pages). Walk three options with numbers: (a) do nothing: every further call carries 38,000 tokens; (b) clear old tool results: drop 30,000, keep a one-line record that the calendar was checked, so the history falls to 8,000 and the next call costs 8,000 not 38,000 in input; (c) compaction: summarize the 40 turns into about 600 tokens of "booked Fri 2 pm laser; student prefers mornings; waiting on safety training" and restart with that plus recent turns (Claude Code keeps the summary plus the 5 most recently accessed files, per primary source). Say what each loses: a summary can drop a detail, so tune for recall first.
- **Figure 3:** line or bar chart "tokens in the window at each call", x = call number 1 to 40, plotting the 38,000 rising line and a drop to 8,000 after clearing and a drop to about 600 plus recent turns after compaction. Labels: "Window if nothing is trimmed", "After clearing old tool results", "After summarizing". Arrow reasons: "old results can be fetched again", "summary replaces turns". Comes after the three-option trace.
- **Misconceptions:**
  1. "Bigger window means I can stuff everything in." Real case: with a 1M-token window, still pay for every token on every call (part 2 arithmetic), and recall degrades as the window fills (context rot, from both docs).
  2. "Summaries lose nothing." Real case: a summary that omits "student has not finished the safety training" lets the assistant book a machine the student cannot use.
- **Sources:** primary source (context rot, attention budget, compaction, clearing tool results, 5 files detail); context-windows doc (context rot defined, compaction and context editing pointers); memory-tool doc ("context editing clears specific tool results ... compaction summarizes the conversation").

## Part 4: Retrieval: fetching only the page that matters — 1,500 words
- **Key sentence:** When the material is too big to put in the window, keep it outside and pull in only the few pieces the question needs. Retrieval is how the assistant finds the right page in a long manual.
- **Example (trace):** student asks "What speed and power for 3 mm acrylic on the laser cutter?" 1. Offline, the program splits the 120-page manual (60,000 tokens) into chunks of about 300 tokens: 60,000 / 300 = 200 chunks, and builds an index. 2. The model calls search_manual("3 mm acrylic speed power laser"). 3. The program scores the 200 chunks and returns the top 3 (about 900 tokens), each tagged with manual name and page. 4. The model reads them and replies with the setting and the page. Cost: about 900 tokens instead of 60,000, so about 98.5% fewer manual tokens per call (900 / 60,000 = 1.5%). Then a second short case: the query "error E-12" (invented code in the lesson's sample manual) is best caught by exact word matching (BM25), while "my cut edges look burnt" is best caught by meaning (embeddings); define each in one plain sentence, and say that combining both beats either (Anthropic contextual retrieval post). Define top-k as "how many chunks you hand to the model", with the tradeoff: too few and the answer is not there, too many and you refill the window (the Anthropic post found top 20 beat top 10 and top 5 for their test set; present as one result, not a rule).
- **Skip-retrieval rule (decision):** if the whole knowledge base is under about 200,000 tokens (about 500 pages) you can put it in the prompt and use prompt caching; one 60,000-token manual would qualify, but the makerspace's 15 manuals (900,000 tokens in the example) do not, so retrieval is needed (cite the Anthropic post; say the cost from part 2, 33 times, is why the team should still check). Also mention the "just-in-time" version: the agent keeps a light pointer (manual name, page number) and loads the page only when needed, which is what search_manual returns (primary source).
- **Figure 4:** left-to-right pipeline with exact numbers: "Manual: 120 pages, 60,000 tokens" -> "Cut into 200 pieces of about 300 tokens" (reason: small enough to fetch one at a time) -> "Index: a way to score each piece against a question" -> "Top 3 pieces returned: 900 tokens" (reason: only the best matches go to the model) -> "Model's window". A second small box under the index: "Exact words (BM25)" and "Meaning (embeddings)". Comes after step 4 of the trace.
- **Misconceptions:**
  1. "Retrieval means the model searched its memory / the web." Real case: search_manual is a tool the program runs on the makerspace's own files; the model never sees the other 197 chunks.
  2. "The top result is always the right one." Real case: a chunk that says "reduce speed to 60%" with no machine name can be returned for the wrong machine; the contextual retrieval post's example is a chunk saying revenue grew 3% with no company named; fix by tagging each chunk with its manual and section (cheap version of the post's method).
- **Sources:** Anthropic "Introducing Contextual Retrieval" (https://www.anthropic.com/news/contextual-retrieval) for chunking, embeddings, BM25, the 200,000-token rule, top-20 result and the lost-context example; primary source for just-in-time retrieval and the hybrid approach; pricing page for the cost comparison. (A RAG paper such as Lewis et al. 2020 can be added to Go further only if its URL is opened during writing; none was opened while planning, so do not cite it.)

## Part 5: Memory across sessions: notes the agent writes and reads — 1,400 words
- **Key sentence:** When a session ends, the window is gone. Anything the assistant should know next time has to be saved outside the window and read back in, either as notes it writes or as records it looks up.
- **Example (trace across two sessions):** Session 1 (Monday): student Riley says "I prefer morning slots and I finished the laser safety course." 1. Model calls memory view /memories (checks for notes first; the memory tool's built-in protocol). 2. Program returns an empty directory. 3. Model creates /memories/students/riley.md with "prefers mornings". 4. The program ends the session; the window is discarded. Session 2 (Thursday): 5. new window, only the instructions and tool descriptions are there (1,430 tokens); the model views /memories, finds riley.md (about 30 tokens) and offers a morning slot. Then the key design judgment, with a second trace line: training status is not stored as a note; "has Riley passed laser training?" is answered by a lookup tool (check_training(student_id)) against the team's database, because a note written on Monday can be stale on Thursday and a wrong "yes" lets someone use a machine unsafely. Rule: notes for soft, useful, low-risk facts (preferences, what was tried); lookups for facts that change or that gate safety.
- **Table (not a figure):** four things the assistant could hold, with where each lives and who owns it: the conversation so far (window, program resends); the machine manuals (outside, retrieval); the student's preferences (notes/memory files, model writes); the training status and bookings (database, tools; source of truth). Columns: what, where it lives, how it gets into the window, how long it lasts.
- **Figure 5:** two timelines "Session 1" and "Session 2" with a "Notes folder" box between them. Numbers: Session 1 window ends discarded; notes file riley.md about 30 tokens; Session 2 starts at 1,430 + 30 = 1,460 tokens. Arrows: "model writes note" (reason: so it survives the end of the session), "model reads note at start" (reason: new window starts empty). A side box "Training database" with arrow "looked up fresh each time" (reason: must be current).
- **Practical points (brief, in a margin note):** the memory tool is client-side: the program decides where the files live (a folder or a database) and must only allow paths under /memories (path-traversal warning); cap file size and expire old notes; privacy of per-student notes is a team decision. The tool's six commands are view, create, str_replace, insert, delete, rename; name them in one sentence only.
- **Misconceptions:**
  1. "Memory means the model learned something / is retrained." Real case: after Monday the model's weights are unchanged; Thursday's offer of a morning slot came from a 30-token file read into a fresh window.
  2. "Everything the assistant knows about a student should go in notes." Real case: the Monday note says "completed laser safety course" but the safety record shows it expired on Wednesday; the note is wrong by Thursday. That is why status comes from the lookup.
- **Sources:** memory-tool doc (what it is, client-side, how a call works, commands, security, expiration and size caps, the "always view memory first" protocol, pairing with compaction); primary source (structured note-taking, Pokemon example with progress over thousands of steps: say it in one sentence as proof the approach works over long tasks).

## Part 6: Designing the assistant's context: worked example, then your turn — 1,100 words
- **Key sentence:** Now put the pieces together: for each thing the assistant needs, decide whether it sits in the window, is retrieved, is a note, or is a lookup. Do one together, then one yourself.
- **Worked example (fully shown):** the request "Book the laser cutter for 3 mm acrylic on Friday afternoon and remember I like mornings." Table row by row: instructions (window, always); tool descriptions (window); manual advice on acrylic (retrieve top 3 chunks, 900 tokens); Friday's slots (calendar tool, 350 tokens, clear the result after booking); Riley's training status (lookup, fresh); preference "mornings" (write a note). Total window for the final call: 1,430 + 40 + 900 + 350 + 20 (booking confirmation) + a handful of calls, tallied to a stated number of about 2,800 tokens, with each addend shown (use: 1,430 + 40 + 900 + 350 + 60 = 2,780). Compare with paste-everything (60,000+) to close the loop to the budget.
- **Practice task with fading steps** (fresh case, not the worked one): the request "Which bandsaw blade fits for 2 cm plywood, is the bandsaw free Tuesday morning, and has Sam done bandsaw training?" Step 1 given (list the four needs); step 2 half given (classify each as window / retrieve / note / lookup, first one filled in); step 3 blank (add up a window size from numbers supplied: system 800, tools 600, question 40, 3 manual chunks 900, calendar 350, training result 60, tool requests 3 x 40; the learner computes the total input of the last call). Hints before solutions, solutions on demand (a button). Provide the arithmetic in the solution: 800 + 600 + 40 + 900 + 350 + 60 + 120 = 2,870. The quiz must use a different case.
- **Checks inside the lesson:** short practice question after parts 1 to 5 each (immediate feedback, option lengths equal, correct answer position varied): e.g. part 2 "Call 3 of a request adds a 500-token tool result; what changes in the cost of call 3 versus call 2?"; keep these to about 80 to 100 words each and count them in the part budgets above (practice questions are counted inside each part's budget).
- **Sources:** all of the above, as already cited; the memory-tool doc's multisession pattern (progress log read at the start of each session) as the "going further" idea.

## Summary, go further, closing (unheaded or one short heading) — 450 words
- **Summary (3 to 5 lines):**
  1. The model sees only the window: instructions, tool descriptions, history, tool results and its own reply, all counted in tokens.
  2. The program resends the whole history every call, so cost and clutter grow every step.
  3. Trim: clear old tool results, summarize, and keep only high-value tokens.
  4. Retrieve: keep big material outside and fetch the few pieces needed.
  5. Remember: save low-risk notes outside the window; look up anything that changes or gates safety.
- Prompt: explain in your own words, in two sentences, why the assistant can book Thursday's slot correctly even though Monday's window is gone.
- Go further: primary source first (Effective context engineering), then context-windows doc, memory-tool doc, contextual retrieval post. Community for testing the skill: pick one only if found while writing and verified by a search result (none was verified during planning; do not invent one). NOTES.md does not say the learner refuses communities.
- Closing: remind that they can ask questions in the chat, and a short quiz on the lesson is ready when they want it. Mention what the next lesson covers (workflows versus agents, then multi-agent splits).
- Also: record every source in `RESOURCES.md`; if a cheat sheet is made, one page "What goes where: window, retrieval, notes, lookup" with the table from part 5.

## Word budget

| Part | Words |
|---|---|
| Opening and warm-up | 450 |
| 1 Context window | 1,350 |
| 2 Message history | 1,450 |
| 3 Context rot and trimming | 1,300 |
| 4 Retrieval | 1,500 |
| 5 Memory across sessions | 1,400 |
| 6 Designing the context: worked example and practice | 1,100 |
| Summary, go further, closing | 450 |
| **Total** | **9,000** |

Where the extra detail goes if a part runs short: more steps in the traces (e.g. a third call in part 2, a second query in part 4), one more concrete case of the same idea, and a short recap line at the end of each part. Never a new topic. Out-of-scope reminders: no comparing AI companies, no training or math inside models, no deployment. Keep the "Claude" docs as documentation of a general idea; say once that other model providers work the same way if a team picks another.

## Sources and the claim each supports

1. PRIMARY. Anthropic Engineering, Effective context engineering for AI agents: https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened). Context definition; context rot and attention budget; smallest set of high-signal tokens; just-in-time retrieval with light pointers and the hybrid approach; compaction (Claude Code keeps the summary plus five recent files); clearing tool results; structured note-taking; sub-agents (left for a later lesson).
2. Claude docs, Context windows: https://platform.claude.com/docs/en/build-with-claude/context-windows (opened). Window = all text the model can reference, including its reply; everything counts (system prompt, messages, tool results, tool definitions); turns accumulate and each call resends history; sizes (1M on current models, 200k on others); context rot; compaction and context editing; cached prefixes still occupy the window.
3. Claude docs, Memory tool: https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened). Client-side file memory under /memories; example trace; six commands; the view-first protocol; security (path traversal, size caps, expiration); pairing with compaction; multisession pattern.
4. Anthropic, Introducing Contextual Retrieval: https://www.anthropic.com/news/contextual-retrieval (opened). Chunking, embeddings, BM25, the skip-RAG rule under about 200,000 tokens, lost-context chunk example, top-20 result, 35%/49%/67% failure reductions (optional, one sentence).
5. Claude docs, Pricing: https://platform.claude.com/docs/en/about-claude/pricing (opened). Input vs output per-million-token rates; cache read multipliers; tool_use/tool_result and tool definition tokens count as input; tokenizer varies by model; example rates for Sonnet 5.5 ($2 in, $10 out per MTok).
6. Search results seen but not opened (do not cite in the lesson without opening them): Claude blog on context management (https://claude.com/blog/context-management); Claude cookbook memory tool (https://platform.claude.com/cookbook/tool-use-memory-cookbook).

## Checks for the writer
- Every part opens with its key sentence; read in order they tell the story: window -> history is resent -> trim -> retrieve -> notes -> design.
- Terms introduced in order: token, context window (part 1); message history, input vs output cost (2); context rot, clearing, compaction (3); chunk, retrieval, BM25, embeddings, top-k (4); memory, notes, lookup (5). No example uses a term before its part.
- Misconception ids: none exist yet in the workspace for O3 (keys/0001.json is for the agent loop quiz); do not invent M-ids in the lesson. Quiz must not reuse the practice questions or the numbers in the part 6 practice task.
- The prices and sizes are illustrative; label them so, and point to the pricing page.
