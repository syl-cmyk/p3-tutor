# Plan: O3, 10 minutes (target about 1,500 words; floor 1,200)

**Title:** Context and memory: what an agent sees now, and what it keeps for later

**Win (general):** By the end, anyone who learns this can say what is inside a model's context window at each step of an agent loop, what survives between steps and between sessions, and when to use retrieval or saved notes to bring the right information in.

**Builds on:** learning record 0001 (the model knows only training plus the text it is given), learning record 0002 (the agent loop: every step is a model call, the program runs the tools). No earlier lessons exist yet, and `GLOSSARY.md`, `RESOURCES.md` and `cheatsheets/` do not exist. The lesson should create entries for them. Quiz 0001 is ungraded, so the warm-up recalls the loop, not a score.

**Learner style (PREFERENCES.md):** example first, then the idea. Real numbers and real text. Examples come from the agent itself: what the user says, which tool is picked, what comes back, what it replies. Short and casual. End with why it matters in the real world. Every practice hint comes before its solution.

**Key terms to define, in this order:** token, context window, context rot, memory, session, notes, retrieval, chunk. Each is defined where it first appears.

## Word budget (total 1,520)

| Block | Words |
|---|---|
| Opening (win, why it matters for the mission) plus warm-up recall | 90 |
| Part 1: Context window | 250 |
| Part 2: Context between steps | 270 |
| Part 3: Notes between sessions | 270 |
| Part 4: Retrieval | 270 |
| Part 5: Worked example then faded practice | 280 |
| Part 6: Summary and go further | 90 |

Extra detail beyond 120 words per minute goes only into more steps in the traces in parts 2 and 5, and one short recap line at the end of parts 3 and 4. No new topics.

## Opening and warm-up (90 words)
- The win, in one sentence. One sentence on the mission: the makerspace assistant must answer from long manuals and remember each student's training status.
- Warm-up (answers on demand): "In the agent loop, who runs the tool, the model or the program?" and "Is each step a separate model call?" Both come from learning record 0002 and were never checked.

## Part 1. Context window: what the model can see on one call
- **Key sentence:** The model can only use the text it is handed on each call, and that text has a size limit. So the first thing to know is what fills that space.
- **Words:** 250.
- **Define:** token (a small chunk of text, roughly three-quarters of a word, so a page is a few hundred tokens), then context window (everything the model reads and writes on one call, with a fixed maximum size).
- **Worked example (first call of the makerspace assistant).** Show the real text sent:
  1. The system prompt: "You are the makerspace assistant..." (about 300 tokens, illustrative).
  2. Tool descriptions for `search_manual` and `check_calendar` (about 700 tokens).
  3. The student's question: "Is the laser cutter free Friday?" (about 10 tokens).
  4. The model's reply, which also counts toward the window.
  - Say these numbers are illustrative sizes, not measured.
- **Figure 1 (stacked horizontal bar, "What fills one call").** Four segments in order: "Instructions" (300), "Tool descriptions" (700), "Student question" (10), "Model's reply" (100). A bracket over all four labelled "Context window (the limit)". Draw it after the part's list. Arrows: none. If any, "adds up to" only.
- **Misconceptions:**
  - "The window holds only my question." Wrong. System prompt, tool descriptions, tool results and the reply all count. The numbers above show the question is 10 of about 1,110 tokens ([context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)).
  - "The context window is what the model learned in training." Wrong. Training is a separate thing; the window is working memory for this call. Tie back to record 0001.

## Part 2. Context between steps: what the loop carries forward
- **Key sentence:** The model remembers nothing from one call to the next, so the program sends everything again each step. That is why the window fills up and why cost grows.
- **Words:** 270. The extra detail goes into a longer numbered trace.
- **Worked example (trace, a booking request).** Use these numbers, which add up:
  1. User: "Book the laser cutter Friday 2 pm." Call 1 input: 2,000 tokens (instructions, tools, question). The model asks to call `check_calendar`. Output: 100.
  2. The program runs the tool. The result is 500 tokens: "Fri 2 pm: free."
  3. Call 2 input: 2,000 + 100 + 500 = 2,600. The model asks to call `book_slot`. Output: 100.
  4. The result is 1,500 tokens (a confirmation plus a long policy text).
  5. Call 3 input: 2,600 + 100 + 1,500 = 4,200. Output: 150, the final reply "Booked."
  6. Input tokens billed in total: 2,000 + 2,600 + 4,200 = 8,800. The text alone is only 4,200 long. Output total: 350.
- **Figure 2 (three growing bars, "Same history, sent again").** Bars for call 1 = 2,000, call 2 = 2,600, call 3 = 4,200, each stacked as "carried over" and "new this step". Label under the bars: "Input tokens per call". Arrow from bar 1 to bar 2 and from bar 2 to bar 3: "everything is sent again, plus the new result". Draw it after step 6 of the trace.
- **Then say:** context rot (accuracy falls as the window fills, even before the limit), so keep only what helps. One line each on the two fixes: clear old tool results, or summarise the history (called compaction) ([context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Do not teach the fixes in depth.
- **Misconceptions:**
  - "The model remembers the earlier steps by itself." Wrong. Call 3 only knows the calendar result because it was in the 4,200 tokens sent. Remove the 500-token result and the model cannot know the slot was free.
  - "A bigger window means I can paste everything and it is free." Wrong. A 30,000-token manual pasted in is paid for again on every step: three steps cost 90,000 input tokens for the manual alone. Quality also drops from context rot.

## Part 3. Notes between sessions: what survives when the conversation ends
- **Key sentence:** When a session ends, the window is gone. So anything the assistant must know next time has to be written down outside the window and read back in.
- **Words:** 270. A short recap line at the end.
- **Define:** session (one conversation from first message to end), notes (text saved in a file or a database by the program, outside the window), memory (what you choose to put back into the window from those notes).
- **Worked example (two visits by one student).** Real text:
  1. Visit 1 (Monday): student says "I finished the laser cutter safety training." The model calls the memory tool: `create /memories/riley.md` with "Laser cutter training: done, Mon." The program saves the file.
  2. Session ends. The window is thrown away.
  3. Visit 2 (Thursday): new session, an empty window. The model first calls `view /memories`, then `view /memories/riley.md`. The program returns the file text.
  4. The student asks to book the laser cutter. The model sees "training: done" in its window and books it.
  - Source for the mechanism: the memory tool is client-side. The model asks for file operations; the app runs them on storage the developer controls ([memory tool doc](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)).
- **Figure 3 (two-lane timeline, "Window resets, notes stay").** Top lane: two boxes "Monday session window" and "Thursday session window", separated by a gap labelled "window cleared". Bottom lane: one box "Notes file: riley.md". Arrow from Monday box to notes: "model asks program to save". Arrow from notes to Thursday box: "model asks program to read". Draw it after step 4.
- **Misconceptions:**
  - "The model learns from the chat and will remember Riley next time." Wrong. Training does not change during use. Without the saved file, Thursday's window has no trace of Monday. Test case: delete `riley.md` and the assistant asks for the training status again.
  - "The memory tool stores data on the model provider's side." Wrong. It runs in the app, so the team decides where files live, how big they get, and how long they last.

## Part 4. Retrieval: finding the right page in a long manual
- **Key sentence:** A long manual will not fit in the window every step, and it should not. So the assistant fetches just the pieces it needs, when it needs them.
- **Words:** 270. A short recap line at the end.
- **Define:** chunk (a short piece of a document, usually a few hundred tokens), retrieval (a search that finds the chunks that best match the question, and puts only those in the window).
- **Worked example (one question).** Real numbers:
  1. Student: "What speed do I use for 3 mm acrylic on the laser cutter?"
  2. The manual (40 pages, about 30,000 tokens) was split into chunks of about 300 tokens each, ahead of time, about 100 chunks.
  3. The model calls `search_manual` with "laser cutter acrylic 3 mm speed". The program returns the top 3 chunks, about 900 tokens.
  4. The model reads chunk 2, "Acrylic 3 mm: speed 20 mm/s, power 60%", and replies with the setting and the page number.
  5. Window cost: 900 tokens instead of 30,000.
  - Keep search as a plain keyword-or-meaning match. Mention that exact words like a machine model number are caught better by keyword search and wording matches by meaning, so many systems use both ([contextual retrieval](https://www.anthropic.com/news/contextual-retrieval)). Do not explain embeddings or BM25.
  - Rule of thumb from that source: if the knowledge base fits in about 200,000 tokens (roughly 500 pages), it is possible to skip retrieval and include it all, with caching helping cost. For this assistant, say it is a cost and quality choice to weigh, not a rule.
- **Figure 4 (left-to-right flow, "Retrieval keeps the window small").** Boxes: "Manual (about 100 chunks)" then "Search" then "Top 3 chunks (about 900 tokens)" then "Context window" then "Answer". Arrows: "split ahead of time", "match the question", "only these go in", "model reads and replies". Draw it after step 5.
- **Misconceptions:**
  - "Retrieval means the model searches the whole manual itself." Wrong. The program runs the search; the model only sees what comes back. If the right chunk is not in the top 3, the model cannot answer correctly, and may guess. Real case: search "acrylic speed" and get the wrong machine's chunk.
  - "Retrieval and notes are the same thing." Wrong. Notes are what the assistant writes about this student. Retrieval is reading a document the team wrote. Both end the same way: text placed in the window.

## Part 5. Worked example, then practice: deciding what goes where
- **Key sentence:** Every piece of information has to live somewhere: in the window now, in notes for later, or in a document to retrieve. So the last skill is sorting each item into the right place.
- **Words:** 280. The extra detail goes into the worked sorting table and the faded steps.
- **Worked example (fully shown).** Sort four items, giving a reason and a number for each:
  1. "Student's name and request" goes in the window now (small, needed this step).
  2. "Training status of each student" goes in notes (changes by student, must survive sessions).
  3. "40-page laser cutter manual" goes to retrieval (30,000 tokens, only about 900 needed per question).
  4. "Result of today's calendar check" goes in the window now, and can be cleared once the booking is made.
- **Practice (steps faded).** New items, different from the worked table: (a) "the student prefers morning slots, told in this chat"; (b) "the 3D printer's 25-page manual (about 18,000 tokens)"; (c) "the booking made 3 steps ago". Step 1 filled in as a hint ("Does it need to survive after this chat ends?"). Step 2 blank, step 3 blank. Hints appear before the solutions, then the solutions on demand. Expected: (a) notes, since it matters on later visits; (b) retrieval; (c) window now, then clear or summarise it once done.
- **Why this matters:** with a small model budget (MISSION.md), the choice sets cost per request: tokens in the window are paid for again every step. This is the decision Riley must defend in design review.

## Part 6. Summary and go further (90 words)
- Summary, 3 to 5 lines:
  1. The context window is everything the model reads and writes on one call, and it has a limit.
  2. The model keeps nothing between calls, so the program resends the history each step, which is why long loops cost more.
  3. Between sessions, only saved notes survive, and they matter only once read back into the window.
  4. Retrieval puts a few matching chunks in the window instead of the whole manual.
  5. Everything the model uses reaches it as text in the window.
- Prompt: "Explain in your own words why the assistant knows on Thursday that a student finished training on Monday."
- Go further: primary source plus two or three others (below), then the closing reminder that the learner can ask questions in chat and that a quiz is ready. Community suggestion: the Anthropic developer community or r/LocalLLaMA is optional. Check `NOTES.md` for any no-community wish (none noted) and choose a reputable forum after searching.

## Misconceptions not to assert (judge model checks)
- Do not say the model "remembers" across calls on its own, that training updates from chat, or that a larger window removes the need to curate context.
- Do not state exact context sizes or model names as fixed. If one is needed, cite the context-window doc: 1M tokens for current models, 200k for some older ones.

## Sources (primary marked)
1. **PRIMARY.** Anthropic Engineering, "Effective context engineering for AI agents": https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Opened this session. Supports: context is a finite resource; context rot; compaction; structured note-taking outside the window; just-in-time retrieval; the trade-off that retrieval is slower than loading up front.
2. Anthropic docs, "Memory tool": https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool. Opened. Supports: the memory tool is client-side and the app runs the file operations; `/memories` directory; view/create commands; memory persists across conversations; the model checks memory first; memory is paired with compaction.
3. Anthropic docs, "Context windows": https://platform.claude.com/docs/en/build-with-claude/context-windows. Opened. Supports: the window includes the system prompt, messages, tool results, tool definitions and the output; history accumulates turn by turn; context rot; window sizes.
4. Anthropic, "Introducing Contextual Retrieval": https://www.anthropic.com/news/contextual-retrieval. Opened. Supports: chunks of a few hundred tokens; retrieved chunks are added to the prompt; keyword plus meaning matching; the 200,000-token (about 500 pages) point where all of it can go in the prompt instead.

All four URLs were opened in this session, exactly as written. The numbers in the worked examples (300, 700, 2,000, 30,000 tokens and so on) are illustrative, and the lesson must say so.

## Figures (summary)
Four inline SVG figures (viewBox about 640 wide, labels 18 or larger, a title and a figcaption each, colors from the template variables): Fig 1 in part 1, Fig 2 in part 2, Fig 3 in part 3, Fig 4 in part 4. No figure in parts 5 and 6.

## Notes for the writer
- Open every part with its key sentence; the six key sentences, read in order, tell the lesson.
- Part titles use the course term, then a colon and a plain explanation. The title of Part 5 is the exception to review: "Context budgeting: deciding what goes where".
- Practice and quiz stay separate: the lesson's sorting items (a) to (c) must not appear in the quiz.
- Add entries to `GLOSSARY.md` and `RESOURCES.md`. A cheat sheet is optional: "Where does this information live? window / notes / retrieval".
