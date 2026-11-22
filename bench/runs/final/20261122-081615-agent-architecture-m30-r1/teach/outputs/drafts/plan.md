# Plan: O3, context and memory in an agent

**Title:** Context and memory: what an agent sees now, and what it can look up later
(Alt in course terms: "Context engineering: deciding what the model sees on each call")

**The win (general):** Anyone who learns this can decide, for any agent, what goes into the context window on each call, what is carried between steps, what is saved between sessions, and what is fetched on demand.

**Length:** 30 minutes, 4,500 words (150/min). meta p3-minutes=30, p3-objective=O3.

**Learner fit (PREFERENCES, NOTES):** Riley wants an example first with real numbers, then the idea, then why it matters. Casual voice, short paragraphs, hints before answers. Riley knows the loop (record 0002) and that a model only knows training plus the text it is given (record 0001). Riley has NOT been taught tokens. Teach "token" in one plain sentence in Part 1 (a chunk of text, roughly a short word or part of a word; the model reads and writes in tokens, and the bill is per token). Link back to lessons/ 0001-style loop lesson if one exists in `lessons/` (none yet; the folder is empty, so no links).
Mission link: "decide what the assistant keeps in its context, what it saves between sessions, and how it finds the right page in a long manual"; budget matters, so cost per request recurs.

**Running example (all parts):** the makerspace assistant. Three sources of information: the machine manuals (long), the booking calendar (changes by the minute), and each student's training status (small, per person, must last between visits). Student: Dana. All numbers below are illustrative and labelled as such in the lesson, except where cited.

## Word budget

| Block | Words |
|---|---|
| Opening: win, mission tie, warm-up recall (2 questions on the loop, answers on demand) | 250 |
| Part 1 Context window | 650 |
| Part 2 Context rot | 600 |
| Part 3 State between steps | 600 |
| Part 4 Memory between sessions | 700 |
| Part 5 Retrieval | 750 |
| Part 6 Worked example, faded practice, summary | 700 |
| Go further (primary source, other sources, community), closing reminder | 250 |
| **Total** | **4,500** |

Extra detail goes only into more trace lines, one more concrete case of the same idea, or a short recap, never a new topic.

---

## Part 1. Context window: everything the model can see on one call (650 words)

**Key sentence:** The model has no memory of its own between calls; it only reads what the program hands it each time. So the first job is to know exactly what is in that handover and how fast it fills up.

**Content:** A token (one plain sentence, rough). The context window is all the text the model can reference when generating a response, including the response itself; it is the model's working memory, different from training data ([context windows doc]). Everything counts: system prompt, every message, tool results, tool definitions, and the output. Each turn the input is all prior history plus the new message, and the reply is added to the history for the next turn. So each call is a fresh, separate call (ties to record 0002: every step is a separate model call, the program runs the tools). Cost follows tokens in and out, so a longer history costs more on every later call.

**Worked example (trace, Dana asks "Is the laser cutter free Friday, and how do I change the lens?"):**
1. Call 1 input: system prompt (about 400 tokens), the 3 tool definitions (about 600), Dana's question (about 25). About 1,025 tokens in.
2. Model asks for `check_calendar`; the program runs it.
3. Call 2 input: everything from call 1 plus the model's tool request plus the calendar result (about 150). About 1,200 tokens in, because call 1 is sent again.
4. Model writes the answer (about 100 tokens). Call 3 would carry all of this again plus Dana's next message.
Extra-detail slot: a fourth trace line showing a 5-turn chat with running totals.

**Figures:**
- Fig 1 "What fills one call": a vertical stack of boxes with the numbers above: "Instructions (400)", "Tool descriptions (600)", "Dana's question (25)", "Calendar result (150)", "Model's reply (100)". Arrow from the stack down to "Model reads it all"; reason: "the model only sees this text". Comes after the definition of context window.
- Fig 2 "Same history sent again": three horizontal bars for calls 1, 2, 3 with lengths 1,025 / 1,200 / about 1,325, each bar extending the last. Label "everything before is sent again". Comes after the trace.

**Misconceptions:**
- "The model remembers my last message by itself." Real case: call 1 and call 2 above; if the program left out the earlier messages, the model would not know what "it" referred to in "book it". The program resends history.
- "The window only holds my question." Real case: 1,025 tokens in call 1 where the question is 25 (about 2%): the rest is instructions and tool descriptions.

## Part 2. Context rot: why a bigger window is not a better answer (600 words)

**Key sentence:** A window has a size limit, but a more important limit is that the model gets worse at using a long context. So the aim is the smallest set of useful text, not the most text.

**Content:** Context rot: as token count grows, accuracy and recall degrade, so curating what is in context matters as much as how much room there is ([context windows doc]). Attention budget idea in plain words: each added token uses up some of the model's focus ([context engineering article]). Principle: the smallest possible set of high-signal tokens. Cost: every extra token is paid for on every later call (ties to the small budget). Name "context engineering" as the course term.

**Worked example:** Option A: paste the whole 80-page laser cutter manual (illustrative: about 40,000 tokens) into every call. Option B: put in only the 2 relevant pages (about 1,000 tokens). Compare over a 6-call conversation: A sends about 240,000 manual tokens in total, B about 6,000, a 40-fold difference, before any answer quality effect. And the lens-change step sits among 39,000 unrelated tokens in A. (Label that the numbers are made up for the arithmetic; the degradation is the cited claim.)
Extra-detail slot: a second pair with the 30-day booking calendar dump (about 8,000 tokens) versus only Friday's slots (about 200).

**Figures:** Fig 3 "Two ways to feed the manual": two columns, A "whole manual every call: 40,000 per call, 240,000 over 6 calls" and B "two pages: 1,000 per call, 6,000 over 6 calls". Arrow from each to "answer"; reason on A: "answer buried in noise", on B: "answer easy to find". Comes after the cost trace.

**Misconceptions:**
- "A 1M-token window means I can put everything in." Case: the docs say models with up to 1M-token windows still show recall degradation as context grows; and cost is per token, so A costs 40 times B.
- "Context rot only matters when the window is full." Case: it grows as tokens grow, not at the limit (the doc says "as token count grows"); A at 40,000 tokens is far from 1M and still worse than B.

## Part 3. Carrying state between steps: what to keep, shrink or drop as a run gets long (600 words)

**Key sentence:** Inside one long run, the history keeps growing, so you have to decide what stays word for word, what gets shortened and what gets dropped. This comes right after rot because it is the first thing you do about it.

**Content:** Three moves, each with a plain definition: (1) clear old tool results, the lightest form (a calendar lookup from 20 steps ago is stale and big); (2) compaction: summarize a conversation that nears the limit and continue in a new window with the summary, keeping decisions and open problems and dropping repeated output ([engineering article]; server-side compaction in [context windows doc]); (3) keep a pointer instead of the content (a file path or a booking id) and load it only when needed (just-in-time). Trade-off: a summary can lose a detail that later matters; cleared results cost a new call if needed again. Note that the booking calendar is the case where old results should be dropped because they go stale.

**Worked example (trace, a 12-step run where Dana asks about three machines):**
1. Steps 1 to 4: calendar for the laser cutter (150 tokens), manual pages (1,000), calendar for the 3D printer (150), its manual page (1,000). History about 2,300 tokens plus fixed 1,025.
2. Step 5: clear the two calendar results, keep short lines "laser: free Fri 2 pm; printer: busy Fri". Saves about 300 and removes stale text.
3. Step 9: compaction. Summary (about 200 tokens): "Dana wants Friday afternoon; laser free 2 pm; printer busy; Dana is trained on laser, not printer." Replaces 6,000 tokens of history.
4. Step 10 continues with 1,025 + 200 tokens.
Extra-detail slot: show what is lost if the summary leaves out "not trained on printer".

**Figures:** Fig 4 "History size over 12 steps": line chart, x = step 1..12, y = tokens; points: step 1 = 1,200; step 4 = 3,300; step 8 = 7,000; step 9 after compaction = 1,225; step 12 = 2,400 (all illustrative). Arrow annotation at step 9: "summary replaces the old turns"; arrow at step 5: "stale calendar results cleared". Comes after the three moves are defined.

**Misconceptions:**
- "Summarizing is free and safe." Case: if the summary drops "Dana is not trained on the printer", the assistant could book the printer in step 11.
- "Old tool results should always stay so nothing is lost." Case: Friday's calendar result from step 1 is wrong if Dana books at step 6; keeping it makes the model see two conflicting facts.

## Part 4. Persistent memory: notes that last between sessions (700 words)

**Key sentence:** Everything so far disappears when the session ends. To remember Dana next week, the assistant has to write things down outside the window and read them back later.

**Content:** Between sessions the window starts empty. Memory = the program stores information in files or a database, and the model reads it back by calling a tool ([memory tool doc]). Structured note-taking: the agent writes notes to storage outside the context and pulls them back later ([engineering article]). The memory tool: client-side, the model asks for file operations under `/memories` (commands include view, create, str_replace, insert, delete, rename) and your program runs them against storage you control and returns the result as a tool result. It is the same loop as in record 0002: the model asks, the program acts. At session start the model views its memory directory first. Contrast: parametric memory (what is in the model's weights; fixed at training) versus external memory ([RAG paper] terms, one line only). Design choices for the mission: what to save (training status, preferences like "Dana prefers afternoon slots"), what NOT to save (calendar availability, which goes stale; and the manual, which is already a source), who can read it, size caps and expiry (security notes in doc: restrict to `/memories`, cap file size, expire old files, avoid sensitive data). Note the official training status record should come from the university system, not the model's note, because a note can be stale or wrong (judgment point, flagged as design opinion).

**Worked example (trace across two sessions):**
1. Session 1, Dana: "I finished the laser cutter safety training today." Model calls `memory` `view /memories`: empty.
2. Model calls `create /memories/students/dana.md` with "Trained: laser cutter (Nov 20). Prefers afternoons." Program writes it and returns "File created successfully".
3. Session ends; the window is discarded.
4. Session 2, a week later, Dana: "Book the laser cutter Friday." Window starts with only instructions and tools (about 1,025 tokens). Model first calls `view /memories`, sees `students/dana.md`, views it (about 30 tokens).
5. Model sees "Trained: laser cutter", calls `check_calendar`, books an afternoon slot.
Extra-detail slot: a third trace line where Dana later passes 3D printer training and the model uses `str_replace` to update the line instead of creating a duplicate.

**Figures:** Fig 5 "Two sessions, one notebook": left box "Session 1 window" and right box "Session 2 window", both with a dotted end ("discarded"); in the middle a box "Notes store (files the program keeps)" with arrows: from session 1 "writes: Dana trained on laser" (reason: so it outlasts the session) and to session 2 "reads at start" (reason: restores what the assistant knew). Comes after the memory tool definition.

**Misconceptions:**
- "Memory means the model learned Dana." Case: nothing in the weights changes; delete `dana.md` and session 3 knows nothing about her.
- "Memory saves itself." Case: in the doc the program must implement the handler and the storage; the model only requests operations. If the handler is not built, "Trained: laser" is never written.
- "Save everything." Case: a note "Laser free Fri 2 pm" saved on Monday is wrong by Friday; save facts that change slowly, look up the fast ones.

## Part 5. Retrieval: finding the right page in a long manual (750 words)

**Key sentence:** Some information is too big to keep in the window or in notes, like the manuals, so the assistant looks up only the part it needs for each question. This is retrieval, and it is how Part 2's "smallest useful text" is done in practice.

**Content:** Retrieval-augmented generation: combine what the model already holds in its weights with an external source it can search; it was proposed to reduce the limits of knowledge stored only in parameters, such as outdated facts and no way to show where an answer came from ([RAG paper]). Steps: (1) before anything, split the manual into chunks (a section or page); (2) at question time, search the chunks, scored by keyword match or by meaning similarity (one line each; do not teach embeddings math: out of scope); (3) put the top few chunks in the context with their page names; (4) the model answers from them and cites the page. Two ways to wire it: fixed (the program always searches first, a workflow) or as a tool the model calls when it decides to (just-in-time; [engineering article]); a hybrid is often best (some always loaded, rest on demand). Retrieval can miss: the right page may not come back (then the model may answer from general knowledge, so tell it to say "not found in the manual"). Retrieval versus memory: retrieval looks up shared documents; memory holds this one student's facts. Same tool-call shape in both.

**Worked example (trace):**
1. Dana: "What's the max material thickness for the laser cutter?"
2. Model calls `search_manuals(query="laser cutter max material thickness")`.
3. Program searches 400 chunks (illustrative: 4 manuals, about 100 chunks each) and returns the top 3, each about 300 tokens: "LC-40 manual p.12, Specs: cuts acrylic up to 10 mm"; "p.14, Materials not allowed: PVC"; "p.9, Focus the lens".
4. Context grows by about 900 tokens instead of 40,000.
5. Model replies: "Up to 10 mm acrylic (LC-40 manual, p.12). PVC is not allowed (p.14)."
Extra-detail slot: a miss case, the question uses "burn through" and the manual says "kerf": keyword search returns the wrong chunks and the model should reply "I could not find that in the manual".

**Figures:** Fig 6 "Look-up path": vertical boxes: "Question" -> (arrow, "turn into a search") "Search the chunks (400)" -> (arrow, "keep the best 3") "3 chunks (900 tokens)" -> (arrow, "added to the window") "Model answers with page numbers". Side box "Manuals cut into chunks once, ahead of time". Comes after the steps are defined.

**Misconceptions:**
- "Retrieval makes the model learn the manual." Case: delete the chunk and the next answer changes; nothing in the weights changed (non-parametric memory in RAG paper).
- "Retrieval always returns the right page." Case: the burn-through / kerf miss above, so the program must handle "nothing good found".
- "Retrieval and memory are the same." Case: the max thickness (shared manual, search) versus Dana's training (one person, notes).

## Part 6. Putting it together: a worked design, then your turn (700 words)

**Key sentence:** For every piece of information the assistant uses, you answer one question: where does it live, and when does it enter the window? Here is that done once, step by step, then you do a similar one.

**Content:** A three-column decision table: item / where it lives / when it enters the window. Rows for the worked example: instructions and tool descriptions (always in window), Dana's training status (notes, loaded at session start), manual pages (retrieval, only when asked), calendar (live tool call, never saved, cleared after use), the chat so far (in window, compacted when long). Then practice with the steps faded.

**Worked example (full, 5 steps, all numbers shown):** Design the assistant for "Can I use the 3D printer Saturday? I'm Sam." Steps: (1) identify the pieces; (2) decide each one's home; (3) estimate tokens in window (instructions 1,000 + notes 30 + 2 manual chunks 600 + calendar 150 = about 1,800) versus all-in (1,000 + 30 + 35,000 manual + 8,000 calendar = about 44,000); (4) say what is saved at the end (training status unchanged; nothing else); (5) name one risk (retrieval miss or stale note) and its guard.

**Practice (faded, hints before solutions):**
- Task A (steps 1 to 3 given, learner does 4 to 5): "Dana asks: 'Which settings for 3 mm plywood on the laser cutter, and book me Thursday 3 pm.'" Fill in the table's home for each item, and estimate the tokens in the window.
- Task B (only the case given): "A student says: 'I got my mill training today; also, I hate mornings.'" What gets saved, where, and what should not be saved?
- Task C, one multiple-choice item (all options same word count, correct answer not in position A): "By session 3 a note says 'Printer free Saturday'. What is the problem?" (Do NOT reuse in quiz; quiz needs fresh items.)
- Hint ladder per task: hint 1 which of the three homes (window, notes, retrieval); hint 2 how often does it change; solution on demand, with why each wrong option is wrong.

**Summary (3 to 5 lines):** (1) The model sees only the context window, resent each call. (2) More is not better: context rot plus cost, so curate. (3) In a run, clear, summarize, or point instead of pasting. (4) Between sessions, only what is written to notes survives. (5) Look up big documents by retrieval; keep per-person facts in notes. Then a prompt to explain in their own words: "Where does Dana's training status live, and when does it enter the window?" Why it matters in the real world: cost per request and trustworthy answers. Next lesson teaser: workflows versus agents.

**Figure:** Fig 7 (optional, only if budget allows) the decision table as an HTML table, not an image.

---

## Go further and closing (250 words)

Primary source (to recommend in "Go further"): Anthropic Engineering, "Effective context engineering for AI agents". Other sources cited: context windows doc, memory tool doc, RAG paper. Community: suggest a high-reputation community where Riley can test it (for example a developer forum or subreddit about LLM agents; the writer should confirm the exact URL by search before linking). Closing reminder: ask follow-ups in chat; quiz ready.

## Common thread for the quiz writer (do not put answers in the lesson)

Practice items in the lesson must differ from quiz items. Misconceptions to carry into the quiz (ids to be assigned later; none exist yet): model remembers by itself; bigger window means better; memory means weights changed; retrieval always finds the right page; save everything.

## Sources (all opened in this session)

1. PRIMARY: Anthropic Engineering, "Effective context engineering for AI agents". https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   Supports: context engineering definition; attention budget and context rot; "smallest possible set of high-signal tokens"; just-in-time retrieval with lightweight identifiers; hybrid approach; compaction and tool result clearing; structured note-taking outside the window; choosing between techniques. (Parts 2, 3, 4, 5.)
2. Claude Docs, "Context windows". https://platform.claude.com/docs/en/build-with-claude/context-windows
   Supports: context window as working memory including the response; everything counts (system prompt, messages, tool results, tool definitions, output); history accumulates each turn; context rot; up to 1M tokens depending on the model; compaction and context editing (tool result clearing). (Parts 1, 2, 3.)
3. Claude Docs, "Memory tool". https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
   Supports: client-side memory under `/memories`; commands view, create, str_replace, insert, delete, rename; the program runs operations and returns tool results; check memory first; pairing with compaction; security (path traversal, size caps, expiry, sensitive data); multisession progress-log pattern. (Part 4.)
4. Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (NeurIPS 2020). https://arxiv.org/abs/2005.11401
   Supports: parametric memory (weights) versus non-parametric memory (external index searched by a retriever); motivation (limits of parametric-only knowledge, provenance, updating knowledge). (Parts 4, 5.)

Facts to keep out of the lesson because I did not verify them: any rule of thumb on characters per token, specific accuracy-drop numbers, pricing figures. All token counts in worked examples are illustrative and must be labelled "made-up numbers" in the lesson.
