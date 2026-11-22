# Lesson plan: O3, context and memory in an agent

Objective O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
Length: 30 minutes, 4,500 words (about 150 per minute). Meta tags: `p3-minutes` = 30, `p3-objective` = O3.

## Title

Context and memory: what an agent sees on each call and what it can carry between sessions

## The win

Anyone who learns this can decide, for any agent, what goes into the context window on each call, what is saved outside it for later, and how the agent finds the right piece of a long document.

(Mission tie-in for the opening, not the win: the makerspace assistant must answer from long machine manuals and remember each student's training status between visits, on a small budget.)

## Primary source

Anthropic Engineering, "Effective context engineering for AI agents": https://anthropic.com/engineering/effective-context-engineering-for-ai-agents
It covers context as a finite resource, context rot, just-in-time retrieval, compaction and note-taking in one place, and it links to the other sources below.

## Build-on and warm-up

- Learning record 0001: the model knows only its training plus the text it is given. Learning record 0002: the agent loop. Quiz 0001 is not yet graded, so the warm-up recalls loop ideas without quoting its items.
- Warm-up, 2 recall questions, answers on demand: (1) In the loop, who actually runs the tool, the model or the program? (2) Is each step one model call or one continuous thought? Both lead into part 1: if each step is a separate call, what does each call carry?
- No earlier lessons exist in `lessons/` and there is no GLOSSARY.md, RESOURCES.md or cheatsheets/ yet. The lesson should add a cheat sheet `cheatsheets/context-and-memory.html` (see end).
- "Token" was only mentioned in passing (record 0001), so part 1 must define it.

## Word budget overview (total 4,500)

| Part | Title | Words |
|---|---|---|
| 1 | Context window: what the model can see on one call | 800 (opening and warm-up about 300 of it) |
| 2 | Conversation history: what is kept between steps, and what each step costs | 700 |
| 3 | Context rot and compaction: why a full window is not a better window | 650 |
| 4 | Retrieval: finding the right page in a long manual | 750 |
| 5 | Notes: memory that survives between sessions | 750 |
| 6 | Putting it together: worked example, faded practice, summary | 850 |

Practice checks inside parts 1 to 5 (one short question each, with feedback on every option) come out of each part's budget. The 150 words per minute rule is met: 4,500 / 30 = 150.

---

## Part 1. Context window: what the model can see on one call (800 words)

**Key sentence:** The model can only use the text that is handed to it on each call, so the first design question is what gets handed over. This comes first because everything else, history, retrieval and notes, is a way of filling that one space.

**Word budget:** 800. Opening with win and mission tie 150; warm-up 150; token and window explanation 250; trace 150; practice check 100. Extra detail goes into the trace (one more line item in the window), not a new topic.

**Worked example (trace, numbers illustrative and labelled so):** One call from the makerspace assistant, "Is the laser cutter free Friday afternoon?"
What is in the window on call 1:
1. Instructions (system prompt): 400 tokens ("You are the makerspace assistant. Answer from the manuals...").
2. Tool descriptions (check_calendar, search_manual, book_slot): 800 tokens.
3. The student's question: 25 tokens.
4. Total sent: 1,225 tokens. The window is the limit on everything sent plus everything the model writes back.
Explain token as a small piece of text, roughly three quarters of a word in English, using this example: the question is about 25 tokens. Window size for the course's examples: say current Claude models have windows of up to 1M tokens ([context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)), and that the number is not the point, curation is.

**Figures:**
- Fig 1, "One call's window": a single horizontal stacked bar. Boxes left to right with plain labels and exact numbers: "Instructions 400", "Tool descriptions 800", "Student's question 25", then a dashed box "Room left for the model's reply". Caption: everything the model sees is in this one bar. Placed after the trace above. No arrows needed; a bracket labelled "1,225 tokens sent".

**Misconceptions:**
- M-a "The model remembers things from earlier calls on its own." Real case: send the call "Book it" alone on a fresh call and the model has no idea what "it" is, because the window held only those two words plus instructions. (This links to record 0001: only training plus the text given.)
- M-b "The context window is the same as the training data." Real case: the manual PDF the team uploaded last week is not in the model's training, so it is only usable if it is in the window.

**Sources:** context windows doc (primary for this part); primary source post for the definition "context refers to the set of tokens included when sampling".

---

## Part 2. Conversation history: what is kept between steps, and what each step costs (700 words)

**Key sentence:** Between steps the model remembers nothing, so the program sends the whole history again on every call. That makes every step a little more expensive than the one before, which is why it comes right after the window itself.

**Word budget:** 700. Explanation 200; the three-call trace with a table 300; cost explanation and why it matters for the sponsor's budget 100; practice check 100. Extra detail goes into the trace, one more column (running total), not a new topic.

**Worked example (full trace, numbers illustrative):** "Is the laser cutter free Friday, and what is the max cut speed for 3 mm acrylic?"
1. Call 1 input: 1,225 tokens (from part 1; two tools needed). Model writes a request for `check_calendar(laser, Friday)`, 60 tokens.
2. The program runs it (reminder from record 0002: the program runs the tool). Result: Friday 13:00 to 15:00 free, 350 tokens.
3. Call 2 input: 1,225 + 60 + 350 = 1,635. Model asks `search_manual("laser acrylic 3 mm speed")`, 70 tokens.
4. Result: one manual page, 1,800 tokens.
5. Call 3 input: 1,635 + 70 + 1,800 = 3,505. Model writes the final answer, 90 tokens.
6. Total input billed across the three calls: 1,225 + 1,635 + 3,505 = 6,365 tokens, though the window at the end holds only about 3,595.
Table columns: call, input sent, model wrote, tool result added.
Why it matters: the manual page alone is half of what call 3 costs, so a big tool result is the main thing to watch. Link to the doc that says everything in the request counts: system prompt, messages, tool results and tool definitions.

**Figures:**
- Fig 2, "Three calls, a growing window": three horizontal bars stacked vertically, one per call, same scale. Bar 1 = 1,225 (labels: "Instructions and tools 1,200" and "Question 25"); bar 2 = 1,635 (adds "Tool request 60" and "Calendar result 350"); bar 3 = 3,505 (adds "Tool request 70" and "Manual page 1,800"). Labels are plain-words. Arrow down between bars labelled "program sends everything again, plus the new lines". Placed after step 5 of the trace.

**Misconceptions:**
- M-a "You only pay for the new message each step." Real numbers above: 6,365 tokens billed for a conversation whose final window is about 3,600.
- M-b "Tool results are free, since the tool, not the model, did the work." The 1,800-token manual page is billed as input on every later call.

**Sources:** context windows doc ("Everything in the request counts..." and the progressive accumulation bullets); the primary source post (tool results should be token-efficient).

---

## Part 3. Context rot and compaction: why a full window is not a better window (650 words)

**Key sentence:** Fitting more into the window does not make the model use it better, so you choose what stays. When history grows, you trim it by clearing old tool results or by summarising, which is the next step after seeing what history costs.

**Word budget:** 650. Context rot explanation 150; two trimming options with the example 300; recap table (keep, clear, summarise) 100; practice check 100. Extra detail goes to a short recap, not a new topic.

**Worked example (numbers illustrative, continuing part 2):** After call 3, the student asks a follow-up and the window is 3,595 tokens, 1,800 of it the old manual page that is no longer needed.
1. Option A, clear the old tool result: replace the 1,800-token page with a 20-token placeholder ("manual page for laser, p. 14, cleared; search again if needed"). Window drops to about 1,815.
2. Option B, summarise: after a 40-message chat about a project, replace the first 35 messages by a 300-token summary: "Student wants to cut 3 mm acrylic on Friday 13:00 to 15:00, has finished laser training, not yet booked." Keep the last 5 messages word for word.
3. What can go wrong: a summary that drops "not yet booked" and the assistant tells the student they are already booked.
Call clearing old tool results the lightest form of compaction, per the primary source.

**Figures:**
- Fig 3, "Before and after trimming": two bars, same scale. Before: "Instructions and tools 1,200", "Old conversation 595", "Old manual page 1,800". After: "Instructions and tools 1,200", "Old conversation 595", "Placeholder 20". Arrow between with the reason "clear the page, keep a pointer". Placed after step 1.

**Misconceptions:**
- M-a "A bigger window means I can put everything in." Real case: the doc says accuracy and recall degrade as token count grows (context rot); give a makerspace case: a bar of 120,000 tokens holding 12 manuals while the student asks about one machine, the relevant paragraph is a needle in a haystack.
- M-b "A summary loses nothing." The "not yet booked" example above.

**Sources:** primary source post (context rot, attention budget, compaction, clearing tool results); context windows doc (context rot; compaction and context editing are named there).

---

## Part 4. Retrieval: finding the right page in a long manual (750 words)

**Key sentence:** When the material is too long to put in every call, keep it outside the window and fetch only the few pieces the question needs. That is retrieval, and it is how the assistant stays cheap while the manuals stay long.

**Word budget:** 750. Why not paste everything: 150; how retrieval works (split into chunks, search, add top pieces to the call) 200; the worked example 250; practice check 100; the "when you do not need it" rule 50. Extra detail goes into one more concrete case in the example (a chunk that loses its context), not a new topic.

**Worked example (numbers illustrative, stated as assumptions):** 12 machine manuals of 40 pages is 480 pages, about 190,000 tokens (using about 400 tokens per page, matching the source's "about 500 pages is 200,000 tokens").
1. Student: "What speed do I use for 3 mm acrylic on the laser?"
2. Pasting everything: 190,000 tokens sent on every call, and it would be resent on each step of the loop (part 2).
3. Retrieval: the manuals were split once, ahead of time, into chunks of about 300 tokens (about 1,600 chunks). The tool `search_manual` scores chunks against the question and returns the top 3: 900 tokens come back.
4. Model answers from those 3 chunks: "Speed 20 mm/s at 60 W (laser manual, p. 14)".
5. A chunk problem: chunk text "Keep the setting at 60 and do not exceed it" does not say which machine or setting. Fix: prepend one line of context to each chunk before indexing ("From the laser cutter manual, section 4, cutting acrylic") - this is the idea of contextual retrieval; report Anthropic's figures: the top-20 failure rate fell from 5.7% to 2.9% with contextual embeddings plus keyword search (BM25).
6. Name the two ways of searching: meaning (embeddings) finds "slow down for thick plastic" from "feed rate"; keyword (BM25) finds an exact error code such as "E-204". Say the real system uses both.
Rule of thumb: for a knowledge base under about 200,000 tokens, the source says you may just include it all, and use prompt caching to make that cheap. Tell Riley this assistant sits at the edge, so state the decision as one to defend at the design review.

**Figures:**
- Fig 4, "From question to answer, with retrieval": vertical flow of boxes. "Student's question" -> "Search the manuals (search_manual)" -> "Top 3 chunks, 900 tokens" -> "Model writes the answer". Arrow reasons: "ask for pieces about this", "only the best matches come back", "the answer cites the page". To the side, a box "Manuals, split ahead of time into about 1,600 chunks" with arrow "searched, never sent whole". Placed after step 3.

**Misconceptions:**
- M-a "Retrieval means the model memorised the manuals." Real case: the model gets 900 tokens per question and has seen nothing else; a different question gets different chunks.
- M-b "Retrieval always finds the right page." Real case: the "do not exceed 60" chunk above; and a query phrased "slow down for thick plastic" misses a chunk that says "reduce feed rate" if only keywords are used.

**Sources:** Anthropic "Introducing Contextual Retrieval" (https://www.anthropic.com/engineering/contextual-retrieval) for chunks, embeddings, BM25, the 200,000-token rule and the 5.7% to 2.9% numbers; the primary source post (just-in-time retrieval, lightweight references).

---

## Part 5. Notes: memory that survives between sessions (750 words)

**Key sentence:** When a chat ends, the window is gone, so anything the assistant should know next visit has to be written down outside it. The assistant writes short notes, then reads them back when a student returns.

**Word budget:** 750. Why the window does not survive 150; how a notes tool works 150; the two-session trace 250; what not to store and keep it fresh 100; practice check 100. Extra detail goes into the trace, one more line showing the second session, not a new topic.

**Worked example (illustrative):** Student Sam, ID s-4821.
Session 1 (Monday):
1. Sam: "I finished the laser safety training. Can you remember that?"
2. The model requests a notes action: create `/memories/students/s-4821.md` with "Laser: safety training done 2026-11-16. 3D printer: not started."
3. The program, not the model, saves the file on its own storage and replies "File created".
4. Model: "Done, you are marked as trained on the laser."
5. The chat ends; the window is thrown away. The file stays.
Session 2 (Thursday, a new window):
1. Sam: "Book the laser for Friday."
2. Call starts with 1,225 tokens and no knowledge of Sam. The model first views the notes, sees the line, and then calls `check_calendar`, then `book_slot`.
3. Final answer: "Booked laser Friday 13:00 to 15:00."
Key detail from the docs: the notes tool runs on your side: the model asks, your program saves, you control where and how, and you must stop paths escaping the notes folder. State this in one sentence and tell Riley the privacy angle is a design-review point.
What to keep fresh: the booking calendar is not memory. It changes constantly, so ask the calendar tool every time; a note "Friday free" would go stale. Keep notes for slowly changing facts (training status, preferred machine), and for training status consider that the official record should win over a note if they disagree, which the design review should decide.
Link back to part 3: a note is also a place to put what a summary might drop.

**Figures:**
- Fig 5, "Two sessions, one notes file": two columns, "Monday session" and "Thursday session", each with a box "Window (gone when chat ends)" and a shared box in the middle "Notes file s-4821 (stays)". Arrows: Monday window -> notes file, reason "write: laser training done"; notes file -> Thursday window, reason "read at the start of the visit". Placed after the Session 2 trace.

**Misconceptions:**
- M-a "The model remembers Sam because it chatted with Sam on Monday." Real case: Thursday starts at 1,225 tokens with nothing about Sam; if the notes file is not read, the assistant asks Sam to prove the training again.
- M-b "Notes are always right." Real case: a note says "Sam: laser trained", but the training record was revoked on Wednesday; the note is stale. Also "notes belong in the window forever": the whole file is viewed only when needed.

**Sources:** memory tool doc (https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool: client-side, the `/memories` folder, view-first protocol, security and size caps, path traversal); primary source post (structured note-taking, NOTES.md-style files); Anthropic "Managing context" announcement (https://www.anthropic.com/news/context-management) for memory as storage outside the window with context editing trimming inside it, and the reported gains (39% with both, 29% with editing alone, as reported there).

---

## Part 6. Putting it together: worked example, faded practice, summary (850 words)

**Key sentence:** Context, retrieval and notes each answer a different question, and a good design uses each for what it is best at. Now you use them together on one request.

**Word budget:** 850. Decision table of the three tools 100; full worked example 250; faded practice task 250 (hints first, solution on demand); summary 100; own-words prompt, why it matters, go further and closing 150. Extra detail goes into the worked trace (one more step), not a new topic.

**Worked example (full, all terms taught above):** Request: Sam says "Book the laser Friday afternoon, and which setting for 3 mm acrylic?"
1. Window starts: instructions and tools (1,200) plus the question.
2. Model views notes: "Laser: trained" (small read, about 40 tokens).
3. Model calls `check_calendar`: result 350 tokens: Friday 13:00 to 15:00 free. Not stored in notes, because it changes.
4. Model calls `search_manual`: 3 chunks, 900 tokens.
5. Model calls `book_slot`: confirmation, 30 tokens.
6. Model replies and, before it ends, writes one note line: "Sam usually books the laser on Fridays."
7. Window thrown away; only the note stays.
Decision table: three rows (what the assistant needs; where it should live; why): training status -> notes, slow-changing and per student; calendar -> live tool call, changes constantly; manual text -> retrieval, long and shared; the current chat -> the window.

**Faded practice task (steps faded):** "A student asks about the 3D printer: 'What temperature for PLA, and is the printer free Saturday morning? I did the printer training last week.'"
- Step 1 given: list what is in the window at the start.
- Step 2 given in part: "which of the three needs (training status, calendar, manual text) comes from notes, a live tool, retrieval?" Learner fills two of three.
- Step 3 blank: learner traces the calls with token numbers they invent and states the total input billed (a hint reminds them each call resends everything).
- Step 4 blank: what to write to notes at the end.
Hints before solutions: Hint 1, "which of these facts changes between visits?" Hint 2, "which is too long to send whole?" Then solution on demand.

**Summary (3 to 5 lines):**
1. The window is everything the model sees on one call, and it has to be rebuilt on every call.
2. Between steps the program resends the history, so each step costs more than the last, and a full window is not a better window.
3. Retrieval fetches a few chunks of a long manual instead of sending it whole.
4. Notes outside the window carry slow-changing facts between sessions; live things like the calendar stay tool calls.
Own-words prompt: "Explain to a teammate why the assistant needs notes and retrieval even though the model has a 1M-token window." Why it matters in the real world: the sponsor's small budget and the design review argument for what lives where.

**Go further:** primary source post; memory tool doc; contextual retrieval post. Community to test the skill: pick a real forum seen in search before the writer links one (not found in this session; the lesson writer should search for it, such as an Anthropic developers community, and use only a URL seen in results). Next lesson: workflows versus agents, so the learner can choose which makerspace steps are a fixed flow.

**Misconceptions to close:** "memory means the model learns" (it does not; training and fine-tuning are out of scope, no weights change, the program just saves and reloads text).

**Sources:** all above.

---

## Figures summary

Five figures: window bar (part 1), three growing bars (part 2), before and after trimming (part 3), retrieval flow (part 4), two-session notes (part 5). Every figure uses a plain-words label per box and the numbers from its part's example, inline SVG, with title and figcaption.

## Quiz-safety note

Practice questions use the numbers above (6,365 tokens, 900-token chunks, s-4821). The later quiz must use fresh numbers and a different machine and must not reuse these items.

## Cheat sheet to write after the lesson

`cheatsheets/context-and-memory.html`: the four places information can live (window, history, retrieval, notes), a one-line rule for each, and the 3-call cost formula.

## Sources and the claim each supports

1. PRIMARY. Anthropic Engineering, "Effective context engineering for AI agents", https://anthropic.com/engineering/effective-context-engineering-for-ai-agents: context is the tokens sampled; context rot and attention budget; just-in-time retrieval with lightweight references; compaction and clearing old tool results; structured note-taking.
2. Claude Platform docs, "Context windows", https://platform.claude.com/docs/en/build-with-claude/context-windows: window includes system prompt, messages, tool results, tool definitions and the output; history accumulates each turn; context rot; compaction and context editing; windows up to 1M tokens on current models.
3. Claude Platform docs, "Memory tool", https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool: client-side file operations in `/memories`; view before work; persists between sessions; security (path traversal, size caps, expiry); multisession progress-file pattern.
4. Anthropic Engineering, "Introducing Contextual Retrieval", https://www.anthropic.com/engineering/contextual-retrieval: chunks, embeddings, BM25; under about 200,000 tokens you may skip RAG; chunk-context example; failure rate 5.7% to 2.9%.
5. Anthropic, "Managing context on the Claude Developer Platform", https://www.anthropic.com/news/context-management: memory stores information outside the window, context editing trims inside it. Seen only in search results, not opened; the writer should open it before using its numbers or drop it.

All URLs were seen in this session's search results or opened. Sources 1 to 4 were opened and read; the token counts, names and students in the examples are invented for teaching and should be labelled "illustrative".
