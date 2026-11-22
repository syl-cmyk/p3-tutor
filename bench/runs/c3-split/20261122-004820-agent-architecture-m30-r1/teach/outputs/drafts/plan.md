# Plan: O3, context and memory in an agent (30 minutes, 4,500 words)

## Title and win

**Title:** Context window and agent memory: what the model sees now, what it keeps, and how it finds the rest

**Win:** Anyone who learns this can decide, for an agent, what belongs in the context window on each call, what should be saved as notes between sessions, and what should be fetched from a large document only when needed.

Note for the writer: the learner's makerspace assistant appears only inside examples. All token counts below are invented round numbers for teaching; say "say" or "for example" so they are not read as measured facts. Do not state a words-per-token ratio unless you cite a source for it.

## Shape and budget

| Item | Words |
|---|---|
| Opening (win, tie to mission, warm-up recall of the agent loop from record 0002, answers on demand) | 250 |
| Part 1 Context window | 700 |
| Part 2 Message history | 700 |
| Part 3 Context rot and clearing | 600 |
| Part 4 Memory | 750 |
| Part 5 Retrieval | 700 |
| Part 6 Worked example and faded practice | 500 |
| Summary, own-words prompt, go further, closing | 300 |
| **Total** | **4,500** |

Extra detail goes only into more steps of the worked traces, one more concrete case of the same idea, or a short recap. No new topics. Multisession checklists, sub-agents, embeddings internals and prompt caching are out; at most one sentence points to a later lesson (sub-agents belong to the multi-agent lesson).

Quiz 0001 is not graded yet, so the warm-up reuses its ground (the program runs the tool, each step is a separate model call) without quoting quiz items.

---

## Part 1. Context window: everything the model can see on one call

**Key sentence:** The model only knows what is written in the text it is handed on this call, so the first design question is what that text contains. Once you see what fills it, you can see why it costs money and why it has a limit.

**Word budget:** 700. Extra detail goes into a second short trace line showing the reply also counts.

**Worked example (trace), built from record 0001 and 0002 terms only:** One call from the makerspace assistant. Define token as a chunk of text the model reads and writes, then show what one call contains (numbers invented):
1. System prompt (the assistant's instructions): 400 tokens.
2. Tool definitions (calendar lookup, booking): 600 tokens.
3. Student message "Is the laser cutter free Friday?": 20 tokens.
4. Input total: 1,020 tokens. The model writes a 60-token reply (a request to call the calendar tool). That output counts toward the window too.
5. Cost link: you pay per token in and out, so what you put in is what you pay for.

Define "context window" as the maximum tokens in one call, input plus output, and say current Claude models have windows up to 1M tokens (docs), so the limit is rarely the first problem; cost and quality are.

**Figure 1 (after the definition of context window, before the trace):** A single stacked horizontal bar titled "One model call". Boxes left to right with plain labels and numbers: "Instructions (system prompt): 400", "Tool descriptions: 600", "Student's message: 20", "Model's reply: 60 (counts too)". A bracket over the first three labeled "Input: 1,020 tokens". Arrow from the three input boxes to the reply box labeled "model reads this, then writes". Caption: the window holds the instructions and tool descriptions too, not only the chat.

**Common misconceptions:**
- "The context window is the model's whole knowledge." Example: the model can state the Friday laser cutter slot only if the calendar result is in the window; with no result in the window it can only guess, as in record 0001's outdated-fact case. Training knowledge is separate from the window.
- "Only my message counts toward the limit and the bill." Example: the 20-token question rode along with 1,000 tokens of instructions and tool descriptions, so 98% of the input was not the question.

---

## Part 2. Message history: what is kept between steps of one task

**Key sentence:** The model keeps nothing from one call to the next, so the program has to send the whole story again on every step. That is why a long task costs more than the sum of its parts looks like.

**Word budget:** 700. Extra detail goes into one more trace step (a failed booking retry) rather than new ideas.

**Worked example (trace), using only Part 1's terms and the agent loop:** Student says "Book the laser cutter Friday at 2." Three model calls:
1. Call 1 input: 1,020 (instructions, tools, question). Model asks for calendar lookup (60 tokens out).
2. The program runs the calendar lookup and gets a 300-token result back.
3. Call 2 input: 1,020 + 60 + 300 = 1,380. Model asks to book (70 out).
4. Program runs the booking; result is 40 tokens.
5. Call 3 input: 1,380 + 70 + 40 = 1,490. Model writes the final reply (90 out): "Booked, Friday 2 pm."
6. Total input tokens billed across the three calls: 1,020 + 1,380 + 1,490 = 3,890, even though only about 450 tokens of new text appeared. The history is what the program carries in a list and re-sends (this is "kept between steps").

Tie to the docs: previous turns are preserved completely and each output becomes input for the next turn; everything (system prompt, messages including tool results, tool definitions) counts.

**Figure 2 (after step 6):** Three vertical bars side by side, labeled "Call 1: 1,020", "Call 2: 1,380", "Call 3: 1,490". Each bar is stacked: the bottom segment "Instructions and tools: 1,000" same height in all three, then segments "Question 20", "Model's request 60", "Calendar result 300", "Model's request 70", "Booking result 40" appearing in the order they were added. Arrows between bars labeled "everything re-sent, plus the new step". Caption: the bars only grow, and the bottom segment is paid again every call. Text must say why each arrow exists (the model remembers nothing between calls).

**Common misconceptions:**
- "The model remembers the earlier step on its own." Example: if the program sent call 3 with only the booking result (40 tokens), the model would not know which machine or time was asked; it needs the 1,380 tokens before it. Each call is a separate model call, with the program holding the history (links to the open point from record 0002).
- "A longer task costs a bit more, in a straight line." Example: three calls of 1,020, 1,380 and 1,490 add to 3,890, but a ten-step task whose history grows 300 tokens a step has its last call far bigger than the first, so cost grows faster than step count.

---

## Part 3. Context rot and clearing: keep the window small and useful

**Key sentence:** A bigger window is not a reason to fill it, because the model gets worse at using a crowded context and every token costs. So the agent should drop what it no longer needs.

**Word budget:** 600. Extra detail goes into a short recap table of the three options.

**Worked example (trace):** The assistant has done many steps, now 40,000 tokens of history. Six old calendar-lookup results of 2,000 tokens each (12,000 total) are no longer needed for the current question.
1. Spot the old tool results that the model already acted on.
2. Replace each with a 20-token placeholder ("calendar result for Tuesday, cleared"): 12,000 becomes 120.
3. History drops from 40,000 to 28,120.
4. Next call is cheaper and the model has less clutter to wade through.
5. If the history is still near the limit: compaction, where the model writes a summary of the conversation and a new window starts from that summary.

Name three tools in a small table: clearing old tool results (light), compaction (summarize and restart), and keeping a pointer instead of the full thing (set up for Part 5). Context rot: as token count grows, accuracy and recall degrade, a gradual decline, not a cliff (Context windows doc and Anthropic engineering post). Guiding principle: the smallest set of high-signal tokens that makes the result likely.

**Figure:** none (a table is enough here).

**Common misconceptions:**
- "A 1M-token window means I can paste everything in." Example: pasting a 90,000-token manual on every call of a three-call task bills about 270,000 input tokens for what a 900-token excerpt does (from Part 5's numbers; keep consistent), and the model must find one line in 90,000 tokens.
- "Summarizing loses nothing." Example: a summary that drops "student is not trained on the laser cutter" makes the assistant book them anyway; compaction should keep decisions and unresolved items and drop repeated tool output, and anything that must survive should also be saved as a note (Part 4).

---

## Part 4. Memory: notes the agent saves for the next session

**Key sentence:** When a session ends, the window is gone, so anything that must last has to be written somewhere outside it. A notes file the agent reads at the start and updates as it goes is the simplest way.

**Word budget:** 750. Extra detail goes into the second session's trace (the second student visit), not a new topic.

**Worked example (trace), makerspace training status:**
1. Session 1, student Riley: "I finished the laser cutter safety training today." The assistant is given a memory tool that works on files under /memories.
2. Model asks to view /memories; the program (not the model) runs it and returns the listing: empty.
3. Model asks to create /memories/students/riley.md with the text "Laser cutter: trained 2026-11-21. 3D printer: not trained." The program writes the file and returns "File created successfully".
4. Session ends. The window, history and all, is thrown away. The file stays on the program's disk.
5. Session 2, a week later: "Book the laser cutter Friday." New window, empty history.
6. Model views /memories, then views riley.md; the 15-token file comes back as a tool result and is now in the window.
7. Model sees the training is recorded, calls the calendar tool, books, replies.
8. Cost: a few tokens of notes instead of re-asking or re-reading a whole conversation.

Explain: memory here is not magic inside the model; it is a file the program stores and the model reads through a tool call, so it travels into the window as ordinary text. In the memory tool the model only asks for file operations and the application runs them against storage it controls (client-side), so the team decides where it lives and how long it is kept. Also say the model is told to assume interruption and record progress as it goes (from the docs' system prompt text).

**Figure 3 (after step 8):** Two boxes side by side, "Session 1 window" and "Session 2 window", with a cylinder between them labeled "Notes file: riley.md (15 tokens)". Arrow from Session 1 box to the file: "write: trained 2026-11-21". Arrow from the file to Session 2 box: "read at the start". Cross symbol on a dashed arrow directly from Session 1 to Session 2 labeled "history is not carried over". Caption: the only thing that crosses is what was written down.

**Common misconceptions:**
- "The assistant will remember Riley next week because it talked to Riley." Example: with no notes file, session 2 starts with an empty window and the assistant must ask whether Riley is trained, or wrongly book.
- "Save everything the student says." Example: saving a 3,000-token transcript means session 2 loads 3,000 tokens to learn one fact; a 15-token line holds it. Notes are small, organized, and updated, not a dump (docs advise keeping the directory organized and capping size). Also: do not store sensitive data without checking; the docs recommend validation and expiry.

---

## Part 5. Retrieval: finding the right page in a long manual

**Key sentence:** Some knowledge is too long to carry in the window every call, so the agent keeps the manual outside and pulls in only the few pieces that answer the question. This is the third place information can live, next to the window and the notes.

**Word budget:** 700. Extra detail goes into a second search case in the trace (an exact error code), not into how embeddings work.

**Worked example (trace), laser cutter manual (numbers invented):** manual is 120 pages, about 90,000 tokens.
1. Prepare once: split the manual into chunks of about 300 tokens, giving 300 chunks. Build a search index over them.
2. Student asks: "Can I cut PVC on the laser cutter?"
3. Model calls a search-manual tool with the query "laser cutter PVC".
4. The program searches the index and returns the top 3 chunks, 900 tokens total, including the chunk that says PVC releases toxic fumes and must never be cut.
5. Model answers with a warning and cites the page.
6. Compare: 900 tokens in the window instead of 90,000, a 100-fold cut in input for that call.
7. Second case: student asks about "error E-42". Searching by meaning can miss an exact code; a keyword search (BM25) finds it exactly; real systems combine both (Anthropic contextual retrieval post). Contextual retrieval adds a short note about where the chunk comes from to each chunk, and reports that combining it with keyword search cut failed retrievals from 5.7% to 2.9%.
8. Just-in-time version: keep only a lightweight pointer (a page index with titles) in the window and let the model load the page it picks (engineering post). Trade-off: slower and needs good guidance.

Honest rule from the contextual retrieval post: if the knowledge is under about 200,000 tokens (roughly 500 pages) you can put it all in the prompt, and prompt caching makes that cheaper; beyond that, retrieve. Say prompt caching exists in one clause only and link, do not teach it. For the learner: decide per manual by size and by cost per request.

**Figure 4 (after step 6):** Left to right pipeline. Box "Laser cutter manual: 120 pages, about 90,000 tokens" -> arrow "split into pieces" -> box "300 chunks of about 300 tokens, in a search index" -> arrow "search with the student's question" -> box "Top 3 chunks: 900 tokens" -> arrow "added to the window" -> box "Model's answer". A small side label under the manual box: "never all sent". Caption: only 1% of the manual reaches the window, because 900 / 90,000 is 1%. Vertical layout acceptable for phones.

**Common misconceptions:**
- "Retrieval always finds the right page." Example: the student types "E-42"; a meaning-based search returns general error-handling chunks while the one chunk with E-42 is missed; the top-20 failure rate was still 5.7% before improvements in the post, so retrieval can miss and the assistant must say when nothing relevant came back.
- "If the window is big enough, retrieval is pointless." Example: a 90,000-token manual fits in a 1M window, but sent on every one of the three calls in Part 2 it costs 270,000 input tokens against 2,700 with retrieval, and the model reads a crowded context (Part 3).

---

## Part 6. Choosing what goes where: window, notes or retrieval

**Key sentence:** Now you have three places for information, and each fact belongs in one of them depending on how often it is needed and how long it must last. Deciding this is the design skill the mission asks for.

**Word budget:** 500. Worked example about 200, faded practice about 300. Extra detail goes into one extra hint per step.

**Worked example (full, step by step):** Request "Book the laser cutter Friday at 2." Put each item in its place:
1. Assistant's instructions and tool descriptions: always in the window (needed on every call).
2. This student's training status: a note, loaded at the start of the session (needed every visit, tiny, must outlast the session).
3. Laser cutter manual: retrieval (large, only a little is needed).
4. Friday calendar: tool result, kept in history until used, then cleared (needed now, stale soon).
5. Final check: roughly 1,500 tokens in the window on the last call instead of about 91,500.

**Faded practice task (3D printer version):** A student asks "My print keeps coming off the bed, and book me the printer for Saturday." The learner assigns six items to window, notes or retrieval. Steps faded: (a) item 1 done for them, (b) item 2 half done, (c) the rest blank. Items: tool descriptions, the printer's troubleshooting manual (60,000 tokens), the student's printer training status, last week's calendar lookup result, the student's preferred email, the instruction text. Hints come first (one question per item: "how often needed? how long must it last? how big?"), then the solution on demand with the reason for each placement. Use only the three places taught above.

**Common misconceptions (one only, to keep to budget):**
- "Memory and retrieval are the same thing." Example: the training-status note is written by the assistant about one student; the manual chunks are written by the manufacturer and never edited by the assistant. Memory is written and updated by the agent; retrieval reads a fixed collection.

---

## Practice, checks and summary

- A one-question check after each of Parts 1 to 5 (about 40 words each, already counted in the part budgets), with feedback explaining the right option and each tempting wrong option. Multiple choice options equal length, right answer position varied. These must not be the quiz items; the quiz will use fresh cases (for example, a different machine and different token counts).
- Warm-up (in the opening): "In the agent loop, who runs the tool, and is each step a separate model call?" Answers revealed on demand (record 0002, quiz 0001 area).
- **Summary (3 to 5 lines):**
  1. The model sees only the window: instructions, tools, history, results, and its own reply.
  2. Between steps, the program re-sends the whole history, so cost and clutter grow; clear or summarize what is no longer needed.
  3. Between sessions, only what was written to notes survives; the model reads it back as ordinary text.
  4. For long documents, retrieve a few relevant pieces instead of loading everything; expect misses and plan for them.
  5. Place each fact by how often it is needed, how long it must last and how big it is.
- Prompt: "In two sentences, tell a teammate why the assistant needs a notes file to remember a student's training."
- Why it matters (the learner likes a real-world tie-in): the sponsor's budget is spent per token, so these choices decide cost per request.
- Next lesson pointer: workflows versus agents and when to split the work across agents (not taught here).
- Community for testing skill: the Anthropic developer Discord or a similar forum; the writer should look for one via search and only link a URL it has seen.

## Sources and the claims they support

1. **PRIMARY.** Effective context engineering for AI agents (Anthropic Engineering), https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Supports: context as the set of tokens given to the model, context rot, finite attention budget and the smallest set of high-signal tokens, compaction, structured note-taking to memory outside the window, just-in-time retrieval with lightweight identifiers, trade-offs.
2. Context windows (Claude API docs), https://platform.claude.com/docs/en/build-with-claude/context-windows. Supports: the window is all text referenced including the response; turns accumulate and prior turns are preserved; system prompt, messages, tool results and tool definitions all count; context rot; window sizes up to 1M tokens; compaction and tool result clearing as options.
3. Memory tool (Claude API docs), https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool. Supports: a /memories directory, client-side operation (the model requests, the application runs and returns tool_result), the view-then-read flow, the system-prompt instruction to check memory and assume interruption, size caps, expiry, sensitive-data and path-safety warnings, pairing with compaction.
4. Introducing Contextual Retrieval (Anthropic), https://www.anthropic.com/news/contextual-retrieval. Supports: chunking, embeddings versus BM25 and exact matches such as error codes, failure rate 5.7% to 2.9% with contextual embeddings plus BM25, the roughly 200,000-token note on small knowledge bases.

Verification status: all four pages were opened in this session (the first and fourth through summaries, the second and third in full text). Every claim about numbers in the plan's examples (tokens in the makerspace traces, 120 pages, 300 chunks) is invented for teaching and must be framed as such; the only real numbers are the 1M window, the 5.7% and 2.9% failure rates, and the 200,000-token guidance.
