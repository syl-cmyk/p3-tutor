# Plan: O3, context and memory in an agent (30 minutes, about 4,500 words)

**Title:** Context and memory: what an agent sees now, and what it can look up later

**The win (general):** By the end, you can say what an agent has in front of it on each model call, what survives from one step and one session to the next, and when to keep something in the context, save it as a note, or retrieve it on demand.

**Links back:** the agent loop (learning record 0002: every step is a separate model call, and the program runs the tools). Learning record 0001: the model knows only its training plus the text it is given. This lesson makes that second point concrete, and it also covers what "token" and "context window" limit, which `NOTES.md` says Riley has not met.

**Voice (from PREFERENCES.md):** example first, then the idea. Casual, short paragraphs (three sentences at most). Real numbers and real text. Quiz-style questions get hints, not answers. End each part with "why this matters" in a line. Numbers for the makerspace are illustrative, and the lesson says so; the only sourced figure is about 400 tokens per page (200,000 tokens is about 500 pages, per the contextual retrieval post).

**Unheaded opening and warm-up (250 words):** the win, one line tying it to the mission ("decide what the assistant keeps in its context, what it saves between sessions, and how it finds the right page"), and two warm-up recall questions with answers on demand: (1) in the loop, who runs the tool, the model or the program? (2) why can a chatbot state an outdated fact? (0001 and 0002).

Word budgets: Opening 250, Part 1 700, Part 2 650, Part 3 700, Part 4 750, Part 5 750, Part 6 700. **Total 4,500.**

---

## Part 1. Context window: everything the model can see on one call (700 words)

**Key sentence:** The model only knows what is in the text you hand it on each call, and that text has a size limit. So before we talk about memory, we need to see what is in that text and how it grows.

**Where the extra detail goes:** more steps in the trace, plus a short note on tokens (a token is a chunk of text, roughly three-quarters of a word; defined in plain words, with the 400 tokens per page ratio).

**Worked example (a trace of one request, with illustrative token counts):** Student asks "Is the laser cutter free Friday, and what's the max material thickness?" Trace of the context on each call:
1. Call 1 sees: system prompt 800 tokens + tool descriptions 1,200 + the question 30 = 2,030 tokens. The model asks for `check_calendar`.
2. The program runs the tool. The result (400 tokens) is appended.
3. Call 2 sees everything from call 1 plus the model's request plus the result = about 2,500. The model asks for `search_manual`.
4. The result is 3 manual pages (1,200 tokens), appended. Call 3 sees about 3,750 and writes the final answer.
5. Point out that the model has no memory of call 1; the program re-sent the whole transcript each time (this is the "every step is a separate call" point that learning record 0002 flagged as unchecked).

**Figure 1:** "What call 3 sees". One horizontal stacked bar, left to right, total 3,750 tokens, with segments: "Instructions: 800", "Tool descriptions: 1,200", "Student's question: 30", "Calendar request and answer: 450", "Manual pages: 1,200", "Room left for the reply". Plain-words label on each box. A second thin bar above it, "Call 1: 2,030", to show growth, with an arrow labeled "each step adds to the pile". Placed after the trace.

**Misconceptions:**
- *"The model remembers earlier calls by itself."* Real case: if the program sent only the newest tool result on call 3, the model would not know the student asked about Friday. The model sees only what the program sends ([context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows): previous turns are carried in the input each time).
- *"The window only holds the student's chat."* Real case: the 1,200 tokens of tool descriptions and the 800 of instructions count too. The docs say everything in the request counts: system prompt, messages, tool results and tool definitions, plus the reply.

**Why it matters (one line):** you pay for and are limited by all of it, on every call.

---

## Part 2. Context rot: why a bigger window does not mean better answers (650 words)

**Key sentence:** A bigger window lets you fit more, but it does not mean the model uses all of it well. So the job is to choose what goes in, not to fill it up.

**Where the extra detail goes:** one more concrete case (cost, tied to the small sponsor budget), then a short recap.

**Worked example:** The team is tempted to paste all ten machine manuals into every call. 10 manuals x 120 pages x 400 tokens = 480,000 tokens per call, versus the 3 relevant pages (1,200 tokens). Trace the student's question "what's the laser cutter's max thickness for acrylic?" with the answer buried among 1,200 pages, and the model grabbing the 3D printer's limit instead of the laser cutter's. Then the cost line: a 5-step loop re-sends the pile each step, so 5 x 480,000 = 2.4 million input tokens for one question, against 5 x about 3,000 for the focused version. State that prices vary, so compare token counts, not dollars.

**Figure 2 (optional, small):** two bars on one scale, "All manuals pasted in: 480,000 tokens per call" and "Only the right pages: 1,200 tokens per call", with the 5-step total in a caption. Placed after the cost trace. (The bar for 1,200 will be a sliver; label it with its number and say so in the caption.)

**Misconceptions:**
- *"A bigger window means the model reads everything equally well."* Context rot: recall gets worse as the context grows, a gradient rather than a cliff ([Effective context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Real case: the laser cutter vs 3D printer thickness mix-up above.
- *"If it fits, it is free."* Real case: the 2.4 million versus 15,000 input tokens comparison above.

**Why it matters:** keeps the assistant accurate and keeps the sponsor's budget alive. The goal is the smallest set of facts that makes the right answer likely.

---

## Part 3. Within-session state: what is kept between steps, and how to trim it (700 words)

**Key sentence:** Inside one conversation, the program keeps the transcript and re-sends it, so the pile only grows. When it gets too big, you have to shrink it on purpose.

**Where the extra detail goes:** one extra step in the trace showing three ways to shrink it side by side (clear old tool results, summarize, start fresh), with a short recap table.

**Worked example:** A long booking chat. The student checks 6 calendars on different days; each calendar result is 2,000 tokens, so 12,000 tokens of results pile up after the student has already chosen Friday 2pm. Trace:
1. Turn 12: the context is 25,000 tokens, and 12,000 of them are old calendar listings nobody needs.
2. Option A, clear old tool results: drop the 6 listings, keep "student chose Friday 2pm" and the booking confirmation. Context goes to about 13,000.
3. Option B, compaction: the model (or the program) writes a 300-token summary of the whole chat and the next window starts from that summary (compaction, per the docs and the engineering post).
4. The cost of each: clearing loses the listings (fine, they can be re-fetched); a summary can drop a detail, such as "student is allergic to the resin", so tell it what must survive.
5. After either option, the model sees only the shrunken version; whatever was dropped is gone from its view.

**Figure 3:** "Before and after trimming": two stacked columns with the numbers above (25,000 before; about 13,000 after clearing; about 300 plus recent turns after summarizing). Label: "old calendar results: 12,000", "chat so far", "summary: 300". Arrow reasons: "clear old results" and "summarize". Placed after the trace.

**Misconceptions:**
- *"Trimming is safe because the model will remember the important bits."* Real case: after a summary, the model knows only what the summary says; if "needs the 40 W laser" was left out, it is gone.
- *"The transcript is saved somewhere the model can reach."* The program holds it, and the model sees it only when it is sent.

**Why it matters:** this is the loop of 0002 with its cost made visible: each step is another call that carries the whole pile.

---

## Part 4. Memory across sessions: notes the agent writes and reads back (750 words)

**Key sentence:** When the conversation ends, the window is gone, so anything the assistant should know next week has to be saved outside it. The usual way is to give the agent a tool to write and read notes.

**Where the extra detail goes:** a second trace for the next visit, and a short list of what to save and what not to (sensitive data, stale notes).

**Worked example (student training status):** Riley's mission says the assistant must remember each student's training status between visits. Trace, session 1 (Monday):
1. Student: "I just finished the laser cutter safety training."
2. The model calls the memory tool: `create /memories/students/s4821.md` with "Laser cutter safety training: done 11/17. Needs: 3D printer training."
3. The program (not the model) runs the file write against its own storage and returns "File created successfully".
4. Session ends. The window is thrown away.
Session 2 (a week later, a brand new window):
5. Student: "Can I book the laser cutter Friday?"
6. First the model views `/memories/students/s4821.md` (the memory tool's instructions tell it to check memory first).
7. The note comes back and the model sees training is done. It then calls `check_calendar` and books.
Say plainly: the memory tool is client-side, so the model only asks and your program stores the data wherever you decide (a folder or a database), and you control retention ([memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)). Also name the alternative for facts that must be exact: a training status could live in a real database the tool reads, with the model's notes for softer things, such as "prefers morning slots".

**Figure 4:** "Two sessions, one notebook". Left box "Session 1 window (thrown away)" and right box "Session 2 window (new)", and a middle box "Notes the program stores: s4821.md". Arrow from session 1 to notes: "model asks to write; program saves". Arrow from notes to session 2: "model asks to read; the program sends the text back". Placed after the trace.

**Misconceptions:**
- *"The model remembers the student because it was told."* Real case: session 2 starts with an empty window; without the `view` call, the assistant would ask for the training status again.
- *"Notes are automatically in the context."* They count only once read: a note read costs tokens on that call, so keep notes short and organized (the engineering post says note-taking works because the agent reloads notes later).
- *"The model's memory lives inside the model or at the vendor."* With the memory tool it lives in your application.

**Why it matters:** a student's status is the main reason this assistant needs memory at all, and it gives the design review a clear answer on where that data lives.

---

## Part 5. Retrieval: finding the right page in a long manual (750 words)

**Key sentence:** Memory is for what the assistant has learned about a student, and retrieval is for finding facts in material that already exists, like manuals. Instead of loading the whole manual, you search it and load only the best few pages.

**Where the extra detail goes:** one more concrete case of the same idea (the chunk that lost its context, such as "Max thickness is 6 mm" with no machine name), then a recap.

**Worked example (the manuals):** Question: "How thick can I cut acrylic on the laser cutter?" Trace:
1. Before any questions, the program splits each manual into chunks of a few hundred tokens and stores a searchable index of them (embeddings turn each chunk into numbers that capture its meaning, so similar meanings are found; described plainly, with no maths).
2. The question arrives; it goes through the same process.
3. The index returns the 3 closest chunks, say "Laser cutter, materials table" (p. 14), "Acrylic settings" (p. 22), "Safety: ventilation" (p. 9).
4. Those chunks, about 1,200 tokens, are placed in the context (the "augmented" part); the model answers and cites page 14.
5. Two ways to connect it to the loop: the program always retrieves first, or `search_manual` is a tool the model chooses to call (this links back to the loop in 0002 and previews the later workflow-versus-agent lesson, so mention it in one line only).
Extra case: the chunk "Maximum thickness is 6 mm." does not say which machine, so it can match the wrong question. The fix is to add context to each chunk before indexing, for example "Laser cutter manual, materials table: Maximum thickness is 6 mm." ([Contextual Retrieval](https://www.anthropic.com/news/contextual-retrieval) reports fewer failed retrievals: 5.7% down to 3.7% with contextual embeddings, 1.9% with the full combination). Also mention the exact-term case: a model number or error code such as "E-17" is better found by keyword search.
Also the small-knowledge-base shortcut: if the material is under about 200,000 tokens (about 500 pages), you can skip retrieval and put it all in, perhaps with caching; here 10 manuals is about 480,000, so retrieval is needed.

**Figure 5:** "From question to the right pages". Boxes left to right: "Manuals split into small chunks (about 300 tokens each)" -> "Index: a searchable list of chunks" -> "Question comes in" -> "Top 3 chunks: 1,200 tokens" -> "Context for the model's answer". Arrow reasons: "split once, ahead of time"; "find the closest matches"; "only these go in the window". Placed after the trace.

**Misconceptions:**
- *"Retrieval means the model has learned the manuals."* Real case: replace the manual and the very next question uses the new page, with no training; the model only reads what was retrieved.
- *"Retrieval always finds the right page."* Real case: the "6 mm" chunk with no machine name, and the 5.7% failure rate on the top-20 chunks in the source's own test, which is lower when chunks carry context but never zero.
- *"Retrieval and memory are the same."* Retrieval searches material someone wrote ahead of time; memory is what the agent wrote down itself. Both end in the same place: text added to the window.

**Why it matters:** this is the "how it finds the right page in a long manual" success criterion in `MISSION.md`, and the cost fix from Part 2.

---

## Part 6. Choosing what to keep: worked example, practice, summary (700 words)

**Key sentence:** Now put the three tools together: for each piece of information, decide whether it stays in the window, goes in a note, or is retrieved when needed. A simple rule helps you decide.

**Rule to teach (one line):** will it be needed on the next call (keep in window), in a later session (note), or only now and then from a big pile (retrieve)?

**Worked example (done in full, about 200 words):** "Student asks to book the 3D printer for Tuesday; the assistant needs: (a) the printer's filament limits, (b) whether the student passed 3D printer training, (c) the Tuesday calendar, (d) the student's name, typed in this chat." Table with each item, the decision and the reason: (a) retrieve from the manual, because it is in a long document; (b) note or database, because it must persist and be exact; (c) tool result, kept in the window for this chat and cleared later; (d) window, only needed now.

**Practice with faded steps (about 250 words):** Same shape, new items, with the steps faded. Version 1 is nearly complete (one blank to fill). Version 2 has only the items: "(a) the student's preferred time of day, mentioned in 3 sessions; (b) the safety rules for the band saw, in a 40-page manual; (c) a booking conflict message from the calendar that the student has since resolved; (d) the student's name." The learner decides each and says why. Hints first (a hint per item: "Will it be needed after this chat ends?" and "How long is the pile it sits in?"), solutions on demand (hidden, with the reason each wrong place fails). Do not reuse these items in the quiz.

**Summary (3 to 5 lines, about 100 words):**
1. The model sees only the window: instructions, tool descriptions, history and results, sized in tokens.
2. More in the window is not better: accuracy can drop and cost grows with every call.
3. Within a session the program re-sends and can trim the pile; across sessions the agent needs notes.
4. Retrieval finds the right chunks in big material, and the model only reads what comes back.
5. Everything ends up as text in the next call's window.
Then a prompt: "In your own words, explain how the assistant knows Maya passed laser cutter training a week ago", and "why this matters in the real world": it is the answer to cost and accuracy questions at the design review.

**Go further, and sources block:** the primary source plus the others below, a community pointer (the Claude developer community or the r/LocalLLaMA / r/LLMDevs forum; the planner has not verified a URL, so the writer must find and open one before linking or skip it), the reminder to ask questions in the chat, and that a quiz is ready. Say in one line what the next lesson covers (workflows versus agents).

---

## Practice and summary checklist

- Worked example then practice with faded steps, hints before solutions: Part 6 (plus a one-question recall check at the end of each of Parts 1 to 5, each with feedback on why each wrong option fails; options all the same length, position of the right answer varied).
- Summary: five lines, in Part 6.
- Quiz items are to be fresh (not the checks or the practice here).

## Sources (all opened this session)

1. **PRIMARY:** Anthropic Engineering, "Effective context engineering for AI agents": https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents. Supports: the definition of context; context rot and the finite attention budget (Part 2); compaction, clearing old tool results, structured note-taking and just-in-time retrieval (Parts 3 to 5); sub-agents (only to point to a later lesson).
2. Claude Docs, "Context windows": https://platform.claude.com/docs/en/build-with-claude/context-windows. Supports: the window is everything the model can reference, including the reply; every turn's history is carried forward as input; system prompt, messages, tool results and tool definitions all count; context rot; compaction and tool result clearing (Parts 1 to 3).
3. Claude Docs, "Memory tool": https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool. Supports: file-based memory in `/memories` that persists between sessions; it is client-side (the model asks and the application runs the operation); the model checks memory first; the multisession pattern; pairing with compaction (Part 4).
4. Anthropic, "Introducing Contextual Retrieval": https://www.anthropic.com/news/contextual-retrieval. Supports: what retrieval-augmented generation is, chunking and embeddings, chunks losing context, the failure-rate figures (5.7%, 3.7%, 2.9%, 1.9%), keyword matching for exact terms, and the 200,000-token (about 500 pages) shortcut (Part 5; also the 400 tokens per page ratio).

**Notes for the writer:**
- Docs list context window sizes by model (up to 1M tokens for current models, including Sonnet 5.5). Do not quote a single "the" window size without naming the model; the lesson's point holds at any size.
- All token counts in the traces are illustrative; label them so, and keep the arithmetic consistent between the trace, the figure and the text.
- Vocabulary introduced in order: token, context window (Part 1); context rot (2); compaction, clearing (3); memory tool, notes (4); chunk, embedding, retrieval (5). No example may use a term before its part.
