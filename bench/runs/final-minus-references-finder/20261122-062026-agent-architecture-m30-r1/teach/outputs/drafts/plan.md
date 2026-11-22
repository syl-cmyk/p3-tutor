# Plan: O3, context and memory in an agent (30 min, 4,500 words)

Lesson file to be written: `lessons/0001-<slug>.html` (suggested slug `context-window-and-agent-memory`). Meta: p3-minutes 30, p3-objective O3.

**Title:** Context management: what an agent sees, keeps and looks up

**Win (general):** By the end you can say, for any agent, what the model sees on each call, what is carried from step to step, and what must be saved outside the window (as notes or as a searchable store) to last between sessions.

**Learner facts to use (from NOTES and records 0001, 0002):** Riley knows the agent loop (model asks, action runs, result returns, repeat) and that a model only has training plus the text it is given. Riley has NOT been taught tokens, the context window, or cost. Quiz 0001 may have left open whether the program runs the tool and whether every step is a separate model call, so Part 2 re-teaches "every step is a separate call" from scratch, gently. Style: example first, real numbers, casual, short paragraphs, hints not answers. Mission link: the makerspace assistant answers from long machine manuals and must remember each student's training status between visits.

**Numbers rule:** all token counts below are made-up illustrative numbers, and the lesson must say so in one line ("round numbers I made up, so the arithmetic is easy"). Do not state a tokens-per-word ratio unless the writer finds and cites one. No new term appears in an example before the part that explains it.

## Opening and warm-up (300 words)
- Title, "30 minutes", the win sentence, two sentences tying it to the makerspace assistant (manuals are long, training status must survive between visits).
- Warm-up recall (answers on demand): (1) In the agent loop, who runs the tool, the model or the program? (2) Why can a chatbot state an outdated fact with confidence? (links to records 0002 and 0001; no new terms).

## Part 1: Context window: all the text the model can see on one call (700 words)
- **Key sentence:** The model knows only what is in the text you send it on this call, so you are the one choosing what it gets to see. That is why we start with what that text is and how it is measured.
- Words: 700. Extra detail goes into the worked trace (listing every piece), not a new topic.
- **Worked example (first, then the idea):** one request to the makerspace assistant, "Is the laser cutter free Friday?", written out as the full text sent on call 1, with made-up sizes: system prompt 800 tokens, tool definitions 600, user message 40, total 1,440 input tokens. Then define token (the unit the model reads and writes in, and the unit that cost and the limit are counted in), context window (all the text the model can reference when generating, including its own reply), and that everything counts: system prompt, messages, tool results, tool definitions, the output ([context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Windows can be up to 1M tokens depending on the model (same doc). Say the window is "working memory", separate from training.
- **Figure 1 (stacked bar, vertical layout):** "What fills one call". Segments with exact numbers: System prompt 800, Tool definitions 600, User message 40, total 1,440, with an empty "room left" segment labelled "space for the reply and later steps". Labels in plain words ("the assistant's standing instructions", "the list of tools it may use", "the student's question"). Comes after the definition of context window. Arrows: none; bracket labelled "1,440 tokens in".
- **Misconceptions:**
  - "The model remembers what it learned from earlier chats." Real case: send the same question in a fresh call with no history and it has no idea about the student's name given an hour ago; training is fixed, only the sent text changes.
  - "Context window means how much it knows." Real case: it is the size of the desk, not the library; a 1M window still holds nothing the call does not contain.
- **Practice check (MCQ, equal-length options):** which of these count toward the window (system prompt, tool definitions, the reply, a tool result). Feedback for every option.

## Part 2: Message history: what carries from one step to the next (650 words)
- **Key sentence:** Every step of the loop is a fresh call, and the only thing that links the steps is the history your program sends again each time. So the window fills a little more with every step, and so does the bill.
- Words: 650. Extra detail goes into the trace (all three calls, with the running total).
- **Worked example (numbered trace, "Is the laser cutter free Friday, and what is the thickest acrylic I can cut?"):**
  1. Call 1 input 1,440 (from Part 1). Model replies with a request to run `check_calendar`, 60 tokens.
  2. The program (not the model) runs it; result is 160 tokens.
  3. Call 2 input = 1,440 + 60 + 160 = 1,660. Model requests `search_manual`, 50 tokens.
  4. Result is 1,500 tokens (a manual page).
  5. Call 3 input = 1,660 + 50 + 1,500 = 3,210. Final reply 120 tokens.
  6. Total input sent across the three calls: 1,440 + 1,660 + 3,210 = 6,310, though the "new" content is much smaller. The big page is sent again at every later step.
- Explain: each model call is a separate call; "history" is a list your program keeps and resends ([context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows): previous turns are preserved completely, each output becomes input of the next turn). Caching changes what you pay for repeated text, not whether it counts toward the window (same doc); mention in one sentence only, do not teach caching. Tie to budget: cost per request follows the tokens sent, so long histories cost.
- **Figure 2 (three growing boxes, vertical):** call 1 = 1,440; call 2 = 1,660; call 3 = 3,210, each box showing the pieces (start 1,440; +60 request; +160 calendar result; +50 request; +1,500 manual page). Arrow label between boxes: "everything above is sent again, plus what was just added". Comes after the trace.
- **Misconceptions:**
  - "The model keeps the conversation going on its own between steps." Real case: if the program forgets to append the calendar result in call 2, the model asks for the calendar again; the loop repeats forever or hits a step limit.
  - "A tool result is only used once." Real case: the 1,500-token page is paid for in call 3 and again in every later call of the conversation.
- **Practice check (numeric):** a fourth call adds a 70-token request and a 200-token result; how many tokens does call 4 send? (Answer 3,210 + ... must be fresh; the writer should compute: 3,210 + 120 final reply is not sent if done, so instead use a different scenario: calls with a 90-token result. Keep numbers new, not the same as the quiz.) Hint first, solution on demand.

## Part 3: Context rot and compaction: keeping the window small and useful (550 words)
- **Key sentence:** Fuller is not better: the more the window holds, the worse the model gets at using any one piece of it. So an agent has to trim as it goes, and what it trims, it loses.
- Words: 550. Extra detail goes into one more concrete case of clearing, not a new technique.
- **Worked example:** the same assistant, 40 steps into a long booking chat for a group of students. History is 62,000 tokens (made up), most of it old manual pages the assistant already used. Three options shown as a trace: (1) clear old tool results, keeping a note that the call happened and re-fetchable; (2) compaction: summarize the conversation and start a new window from the summary; (3) do nothing and pay for and degrade on all 62,000. Say which facts the summary must keep: the booking just made, the student's constraints; show a summary that drops the exact page number, and why that is the cost of compaction.
- Definitions: context rot (accuracy and recall degrade as token count grows, so curating matters as much as capacity, [context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)); context as "a finite resource with diminishing marginal returns" in the idea form: aim for the smallest set of high-signal tokens ([Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)); compaction = summarize a conversation nearing the limit and start a new window from the summary (same article); tool result clearing = drop old re-fetchable results and keep a record the call happened ([context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)).
- **Figure 3 (before/after, vertical):** "Before: 62,000 tokens" bar with segments (old manual pages 48,000; old tool calls and replies 10,000; system and tools 1,440 rounded to 1,500; latest messages 2,500; total 62,000) and "After clearing and summary" bar (system and tools 1,500; summary 1,000; latest messages 2,500; total 5,000). Arrow reason: "summarize and clear old results". After the compaction definition.
- **Misconceptions:**
  - "A bigger window solves the problem, just paste everything in." Real case: the doc itself says accuracy and recall degrade as token count grows, and each call re-sends all of it, so a 62,000-token history costs about 62,000 input tokens on every later call.
  - "Compaction keeps everything, just shorter." Real case: a summary that says "checked manual for acrylic limits" has lost the actual limit; anything you cannot afford to lose goes in a note (Part 5).

## Part 4: Retrieval: loading only the page you need (600 words)
- **Key sentence:** A manual is far too long to keep in the window, so the assistant keeps a way to find the right page and loads only that. This is how it answers from long manuals without paying for the whole manual on every call.
- Words: 600. Extra detail goes into the trace (search, then read).
- **Worked example (trace):** Manuals: 120 pages at about 1,500 tokens each = 180,000 tokens (made up). Student asks "What's the max acrylic thickness on the laser cutter?" 1. Model calls `search_manual("laser cutter acrylic maximum thickness")`. 2. The program searches the manual index and returns 3 short snippets, each with a page number and about 100 tokens, 300 total. 3. Model sees page 42 snippet says "Acrylic up to 12 mm", calls `read_page(42)`. 4. The program returns page 42, 1,500 tokens. 5. Reply: "Up to 12 mm (manual p. 42)". Total content loaded: 1,800 tokens instead of 180,000, 1 percent. Compare costs across 3 calls (stuffing: 180,000 x 3 = 540,000; retrieval: far less; compute in writer's table).
- Definitions: retrieval = finding the relevant pieces in a store outside the window and loading only those; just-in-time = keep light pointers (file paths, page numbers, stored queries) and load on demand; hybrid with some upfront context is common; runtime exploration is slower than pre-computed lookups ([Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Note that a retrieval tool is just a tool in the loop from record 0002; do not teach how search works inside (embeddings are out of scope; say only "the search itself can be plain keywords or something fancier, the next lessons can look at it").
- **Figure 4 (flow, vertical):** "Retrieval for one question". Boxes: "Student's question" -> "Search the manual (returns 3 snippets, 300 tokens)" -> "Read page 42 (1,500 tokens)" -> "Answer with page number". Side box "Manual store: 120 pages, 180,000 tokens, stays outside the window". Arrow reasons: "ask for the pages that match", "pick the best snippet and ask for the whole page", "the page is now in the window". After the trace.
- **Misconceptions:**
  - "Retrieval means the model has read the whole manual." Real case: it has seen 3 snippets and 1 page; if the answer is on page 57 and the search missed it, it cannot know, and it may answer wrongly with confidence.
  - "Retrieval is the same as memory." Real case: the manual is the same for every student and nobody changes it; a student's training status changes and has to be written down (Part 5).

## Part 5: Notes as memory: what survives between sessions (650 words)
- **Key sentence:** When a session ends, the window is gone, so anything the assistant must know next time has to be written somewhere outside it and read back. That is all "memory" means for an agent.
- Words: 650. Extra detail goes into a second session in the trace (read back), not new topics.
- **Worked example (two sessions, trace):** Session 1, 4 March: student Dana says she finished laser cutter safety training. 1. Model calls memory `create /memories/students/dana.md` with "laser cutter: trained 2026-03-04; 3D printer: not trained". 2. The program writes the file to its own store and returns "File created successfully". 3. Reply. Session 2, 19 March, a brand new window with no history: 1. The system prompt tells the model to check its memory first. 2. `view /memories` returns a list of files. 3. `view /memories/students/dana.md` returns the line. 4. Dana asks to book the laser cutter; the assistant books it, and says the 3D printer needs training first. Explain that the memory tool works exactly like the tools of record 0002: client-side, the model asks and the application runs the operation on storage you control ([memory tool doc](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)); and the notes-outside-the-window idea ([Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents), structured note-taking, such as a NOTES.md or to-do list the agent reads back after a reset).
- Table to include (comparison, not a figure): what lives where. Rows: system prompt and tools (every call, resent); message history (this session, resent each step); retrieved manual pages (loaded on demand, then in history); notes or memory files (between sessions, read on demand). Columns: lives where, lasts how long, costs tokens when.
- Design cautions in a few sentences: a note can go stale (training can expire; write the date), store only what is needed, storing student data is a privacy decision for the team, and the application must restrict memory operations to the memory folder (path traversal) ([memory tool doc](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)).
- **Figure 5 (timeline, vertical or two lanes):** Two sessions as two windows. Session 1 window (ends, labelled "gone when the session ends") writes to the "Memory folder (outside the window)" box via arrow "write: laser trained 4 March"; Session 2 window starts empty and reads from the folder via arrow "read first, before answering". Comes after the trace.
- **Misconceptions:**
  - "The model remembers Dana because it talked to her before." Real case: session 2's window starts empty; if the program did not save and reload the note, the assistant would ask her about training again, or worse assume she is trained.
  - "Memory is a built-in feature of the model that stores itself." Real case: with the memory tool Claude only requests operations; if the app's handler does not write the file, nothing is saved.

## Part 6: Choosing what to keep: a worked example, then practice (700 words)
- **Key sentence:** Now put the pieces together: for each thing the assistant needs, decide whether it lives in the window, in a search over the manuals, or in a saved note. This is the decision you will defend at your design review.
- Words: 700 (worked example 300, faded practice 300, hints and solutions 100). Extra detail goes into the worked example's reasoning, one more case of the same rule.
- **Rule of thumb (three questions):** Does it change between sessions? (note) Is it big and only sometimes needed? (retrieve) Is it needed on every step? (keep in the window, short).
- **Worked example (fully shown):** Sort six items for the makerspace assistant: "assistant's rules and tone" (window, every call), "machine manuals" (retrieval), "Dana's training status" (note, with date), "the booking Dana just made in this chat" (history; also write a note only if it must be known next visit; the calendar is the real record), "calendar" (a tool call each time; it changes and belongs to the booking system), "list of tool descriptions" (window, keep short). Explain each choice in one line.
- **Faded practice (steps removed progressively), four new items with a different shape:** (a) "the safety rules for the 3D printer: 40 pages", (b) "which students have had the soldering training", (c) "what the student asked two steps ago in this chat", (d) "the bandsaw's maintenance schedule that changes weekly". Step 1 given as a template with the first item's answer filled in; step 2 half-filled (reason missing); steps 3 and 4 blank. Hints before solutions (hint 1: ask "does it change?"; hint 2: ask "is it needed every step?"), solutions on demand. Note: do not reuse these items in the quiz.
- A cost line at the end: say that the choice is also the cost lever for the sponsor's budget, because tokens sent per call decide the bill.
- **Figure:** none here (re-use the table from Part 5 as the filled-in template).
- **Misconception:** "Put everything in the system prompt, it is simplest." Real case: 180,000 tokens of manuals sent on every call, three calls per request, 540,000 input tokens per question (from Part 4).

## Summary and go further (350 words, not a headed part beyond the sixth: put inside the Part 6 section as sub-blocks, or as unnumbered closing blocks per the lesson template)
- **Summary, 4 lines:** (1) the model sees only the window on each call, and tokens measure it and the cost; (2) each step is a new call that resends the history, so the window and the bill grow; (3) trim with clearing and compaction, and look up long material with retrieval instead of pasting it in; (4) between sessions, only what was written outside the window survives, as notes you read back.
- Prompt: "Explain in your own words why the assistant can recall Dana's training next week even though the window was emptied" (writer: do not supply the answer).
- Go further: **primary source** [Effective context engineering for AI agents](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents); others below; community: the writer should search for one real community (for example the Anthropic developer Discord or a subreddit about LLM agents) and cite what it found; do not type any URL from memory.
- Closing: ask follow-up questions in the chat; a short quiz on this lesson is ready when they want it. Link back to the agent-loop material (record 0002) in text; no earlier lesson files exist yet (the `lessons/` folder is empty), so no relative lesson links.
- Cheat sheet candidate: one page "What lives where" table plus the three questions from Part 6 (for the cheatsheet skill after the lesson).

## Word budget
| Part | Words |
|---|---|
| Opening and warm-up | 300 |
| 1 Context window | 700 |
| 2 Message history | 650 |
| 3 Context rot and compaction | 550 |
| 4 Retrieval | 600 |
| 5 Notes as memory | 650 |
| 6 Worked example and practice (incl. summary and go further, 350) | 1,050 |
| **Total** | **4,500** |

(Part 6 is 700 words of its own plus 350 for summary and sources, so six headed parts at most.)

## Notes for the writer
- Practice question in Part 1 and 2 must be different from quiz questions; the quiz will test fresh items (e.g. the quiz may ask about sorting new items, so do not reuse Dana, laser, or the exact numbers in quiz items).
- Part 2's numeric check must use new numbers; the writer should compute them and double check the sum.
- Four figures are listed (1 to 4) plus the timeline (5); the lesson template says 2 to 4 is typical, so the writer may merge Figure 1 into the trace and keep figures 2, 4, 5 if space is short.
- Model-specific facts (window sizes, which models keep thinking blocks, context awareness) are skipped on purpose: out of scope (comparing products) and not needed for the win. Say at most "windows go up to 1M tokens depending on the model".

## Sources
1. **PRIMARY:** Anthropic Engineering, "Effective context engineering for AI agents", https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened). Supports: context is finite with diminishing returns and context rot; smallest set of high-signal tokens; just-in-time retrieval with lightweight references (file paths, queries, links) and the hybrid trade-off; compaction; clearing tool results; structured note-taking persisted outside the window (to-do list, NOTES.md).
2. Claude Docs, "Context windows", https://platform.claude.com/docs/en/build-with-claude/context-windows (opened). Supports: definition of the context window as working memory including the reply; everything (system prompt, messages, tool results, tool definitions, output) counts; turns accumulate and prior turns are preserved; context rot; windows up to 1M tokens depending on model; caching changes cost not window use; compaction and tool result clearing.
3. Claude Docs, "Memory tool", https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened). Supports: client-side memory, file operations under /memories (view, create, str_replace, insert, delete, rename), the application runs them and returns a tool_result, memory persists between sessions, the view-first protocol, path traversal protection, cap file size and expire old memory, pairing with compaction (compaction keeps the window small, memory keeps what must survive summarizing), multisession pattern.
4. Optional: Anthropic, "Effective harnesses for long-running agents" (linked from the docs above, not opened; the writer should open it before citing, or leave it out).
