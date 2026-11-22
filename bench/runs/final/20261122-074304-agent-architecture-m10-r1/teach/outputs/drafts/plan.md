# Plan: lesson for O3 (10 minutes, about 1,500 words)

Objective O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
File to write: `lessons/0001-<slug>.html`, suggested slug `context-window-and-agent-memory`. Meta tags: `p3-minutes` = 10, `p3-objective` = O3.
No earlier lessons, no RESOURCES.md, GLOSSARY.md or cheatsheets exist. Build on learning records 0001 (the model sees only training plus the text it is given) and 0002 (the agent loop, every step a model call). Note: "token" and "context window" are not yet taught, so the lesson defines both in plain words where they first appear.

## Title
**Context and memory: what an agent can see now and what it can recall later**

## Win
Anyone who learns this can say what is inside a model's context on a given call, what carries over from one step and one session to the next, and when to use notes or retrieval to bring in what the window cannot hold.

## Learner-fit rules
- Example first, then the idea; real numbers; casual voice; short paragraphs (3 sentences max); each part gets a numbered trace.
- Examples come from the makerspace assistant's own traffic: what the user says, which tool is picked, what comes back, what it replies.
- Cost matters (small budget), so tokens tie to cost throughout.
- Practice questions need hints before answers. They must not become quiz items (quiz 0002 will use fresh questions).

## Shared running example and numbers (use the same ones in every part)
- Fixed text sent on every call (system prompt plus tool definitions): 1,200 tokens.
- Student message: "Is the laser cutter free Friday?" = 30 tokens.
- Model's tool request `check_calendar(machine="laser cutter", day="Friday")` = 60 tokens.
- Tool result (list of Friday slots) = 400 tokens.
- Final reply = 80 tokens.
- One manual page = 3,000 tokens; the laser cutter manual = 120 pages = 360,000 tokens.
- Do not call the numbers real model limits. They are illustration numbers.

## Opening (unheaded, about 100 words)
Title, 10 minutes, the win sentence, one line tying to the makerspace assistant. Warm-up recall question from record 0002: "In the agent loop, who runs the tool, the model or the program?" (answer on demand, covers the open gap in record 0002). Second warm-up: "Why can a chatbot state an outdated fact?" (record 0001).

---

## Part 1. Context window: what the model can see on one call (about 210 words)
**Key sentence:** The model only knows what is in the text it is handed on each call. That handed-over text is the context, and it has a size limit.
**Extra detail goes to:** one more line in the trace showing the token count of each piece.
**Worked example (trace of one call):**
1. Program sends: system prompt plus tool definitions (1,200 tokens) plus the student's message (30 tokens) = 1,230 tokens.
2. Model reads only that text. It knows nothing else about this student or the manual.
3. Model writes a tool request (60 tokens). The output counts toward the window too.
Define token in one plain sentence (a chunk of text, roughly three-quarters of a word; you pay per token in and out). Define context window as all the text the model can reference on a call, including its own reply; it works like the model's working memory, and it is not the training data ([Claude docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)).
**Figure 1 (after the definition of context window):** one stacked horizontal bar, "one call". Segments: "Fixed instructions and tool descriptions: 1,200", "Student's message: 30", "Room left for the model's reply", then a bracket "the context window". No arrows. Caption: everything the model uses is in this one bar.
**Misconception named:** "The model remembers me from last time." Case: a student asks "and what about Saturday?" in a brand new call with nothing else in it; the model has no idea which machine was meant, because nothing in the window says so.

## Part 2. Step-to-step state: the context grows with every step (about 240 words)
**Key sentence:** Between steps the model remembers nothing by itself. The program sends the whole history again each time, so the context grows and so does the cost.
**Extra detail goes to:** a fuller second call in the trace, plus a one-line cost remark.
**Worked example (the Friday laser cutter request, two calls):**
1. Call 1 input: 1,200 + 30 = 1,230 tokens. Output: tool request, 60.
2. Program runs `check_calendar` (links to the loop, record 0002) and gets slots back, 400 tokens.
3. Call 2 input: 1,200 + 30 + 60 + 400 = 1,690 tokens, a fresh call that contains all of call 1. Output: reply, 80.
4. Total input tokens paid across the two calls: 1,230 + 1,690 = 2,920, not 1,690.
**Figure 2 (after the trace):** two stacked bars, "Call 1: 1,230 tokens in" and "Call 2: 1,690 tokens in". Call 2's segments: "Same fixed text and question, sent again: 1,230", "Model's request: 60" (reason: its own output joins the history), "Calendar result: 400" (reason: the tool result goes back to the model). Caption: each call re-reads everything before it.
**Misconception named:** "The model keeps its place between steps, so earlier steps are free." Real case: ten tool calls of 400 tokens each; call 11 re-sends 4,000 tokens of results, and every earlier call paid for its own share of them too.

## Part 3. Context rot and compaction: keeping the window small (about 210 words)
**Key sentence:** A bigger window does not mean you should fill it. Models get worse at using long contexts, so you decide what stays in and what gets shrunk.
**Extra detail goes to:** a three-item list of ways to shrink (clear old tool results, summarize, keep a pointer instead of the content).
**Worked example (the same assistant, after a long chat):** a student has asked about booking, three machines, and safety rules; the context is at 40,000 tokens, of which 30,000 are old calendar results already acted on.
1. Clear the old calendar results (they were only needed once): 40,000 to 10,000.
2. Summarize the remaining chat into "Student wants the laser cutter Friday 2pm, booked, confirmation #A12": 10,000 to 2,000, say.
3. Continue with the fixed text plus the summary.
Terms: context rot (accuracy and recall degrade as the token count grows), compaction (summarize a nearly full conversation and continue with the summary). Sources: Claude docs and Anthropic engineering post.
**Figure 3 (after step 3):** two bars, "Before: 40,000" split into "Old calendar results: 30,000" and "Everything else: 10,000", and "After: 2,000" labelled "Summary plus fixed text". Arrow between them labelled "clear and summarize". Caption: most of the space was stale tool output.
**Misconception named:** "A 1M-token window means I can paste in every manual." Case: ten manuals of 360,000 tokens each overfill it, and even a window that fits them degrades with length (context rot) and costs per token on every call.

## Part 4. Session memory: notes kept outside the window (about 230 words)
**Key sentence:** When a session ends, the window is gone. Anything the assistant should know next visit has to be written down somewhere outside it and read back in.
**Extra detail goes to:** one more note example (booking preference) in the same file.
**Worked example (Riley's makerspace need: training status between visits):**
1. Session 1: the student passes the laser cutter safety training. The assistant calls `save_note("student 4471: laser cutter training passed, 2026-11-20")`. The program writes it to a file or database.
2. Session ends. The window is discarded; the model keeps nothing.
3. Session 2, a week later: the program loads that student's notes into the start of the context (about 40 tokens).
4. Student asks "Can I book the laser cutter?" The assistant sees the note and books, without asking again.
Term: structured note-taking (the agent writes notes to storage outside the window and reads them back later; Anthropic's examples are a to-do list or a NOTES.md file). Contrast "short-term" (the window, within a session) and "long-term" (stored, across sessions). The model does not remember; the program stores and reloads.
**Figure 4 (after step 4):** two boxes "Session 1 window" and "Session 2 window" with a box between them below, "Notes file: 'training passed'". Arrow down from session 1, "assistant saves a note"; arrow up into session 2, "program loads it at the start". Caption: only the notes cross the gap.
**Misconception named:** "The model learned the student's status, so it knows it next time." Case: no weights change; delete the notes file and session 2 starts blank, so the assistant would ask for training proof again.

## Part 5. Retrieval: loading only the right page of a long manual (about 230 words)
**Key sentence:** The assistant cannot fit a whole manual in its window, and it does not need to. It keeps a way to find the right page and loads only that.
**Extra detail goes to:** a second question showing a different page comes back.
**Worked example (long laser cutter manual):** manual is 120 pages (360,000 tokens), so pasting costs 360,000 tokens on every call.
1. Student: "What material can't I put in the laser cutter?"
2. Assistant calls `search_manual(machine="laser cutter", query="prohibited materials")`.
3. The program searches an index of the manual and returns the top 2 pages, 3,000 tokens each, 6,000 total, with page numbers.
4. Model reads those pages, replies "No PVC or vinyl, it releases chlorine gas (manual p. 14)."
5. Cost of that call about 6,000 + fixed text, about 1.7% of pasting everything (6,000 / 360,000).
Terms: retrieval (look up the relevant piece and load it into the context just in time), and the idea of a lightweight pointer (a page number or file path) loaded only on need, per Anthropic. Mention a hybrid: the small, always-needed facts load up front (e.g. makerspace hours); the manual is looked up. Mention that retrieval can miss: if the search returns the wrong pages, the model answers from the wrong text, so tool description and search quality matter (leads to the next lesson on tool descriptions).
**Figure 5 (after step 4):** left box "Manual, 120 pages (360,000 tokens), stored outside the window", arrow "search returns the 2 best pages" to a small box "Window: 2 pages, 6,000 tokens". Caption: the window gets only the pages that were fetched.
**Misconception named:** "Retrieval is memory the model has, like recall." Case: a search for "prohibited materials" returns the wiring page instead; the model has nothing correct to read, and may still write a confident answer.

## Part 6. Practice and summary (about 210 words)
**Key sentence:** Now you can decide, for each piece of information the assistant needs, whether it belongs in the window, in notes, or in a retrievable store.
**Worked example (all steps shown):** "The assistant needs (a) the system's rules, (b) a student's training status, (c) page 14 of the laser cutter manual." Answer table: (a) always in the window, fixed text, small and needed every call; (b) notes, needed across sessions and small; (c) retrieval, large and needed rarely.
**Practice task (steps faded):** "Sort these into window, notes, or retrieval: (1) what the student asked two messages ago; (2) which printer the student prefers; (3) the 80-page 3D printer manual; (4) the booking calendar for next week." Step 1 given as a hint (ask: is it needed after this session? how big?); step 2 student does; hints first, then the solutions on demand:
1. window (it is in the conversation now); 2. notes; 3. retrieval; 4. fetch with a calendar tool call when asked, not stored in the window beforehand (retrieval-like, just in time).
Include a one-line cost check: why pasting the 80-page manual (240,000 tokens at 3,000 per page) into every call is costly.
**Summary (4 lines):**
1. The window is everything the model sees on one call, and the output counts too.
2. Each step re-sends the history, so the context and the cost grow; shrink it by clearing and summarizing.
3. Between sessions, only what you save in notes survives; the program reloads it.
4. For big sources, retrieve just the pages you need, just in time.
Add a prompt: "Explain in your own words why the assistant forgets a student between visits and how notes fix that."
**Why it matters (one sentence):** this is how the makerspace assistant stays inside a small model budget while still answering from long manuals.

## Closing and go further (unheaded, about 70 words)
Primary source link, 2 to 3 other sources, a reminder that the learner can ask questions in chat and a quiz is ready. Community pointer: the learner could test design decisions by posting a context plan to a forum such as the Anthropic Discord or r/LocalLLaMA; verify any URL by search before linking, and drop it if not found (none was verified in this session).
Next lesson suggestion: tool descriptions (how the model chooses a tool, since retrieval depends on it).

## Budget table
| Part | Words |
|---|---|
| Opening and warm-up | 100 |
| 1 Context window | 210 |
| 2 Step-to-step state | 240 |
| 3 Context rot and compaction | 210 |
| 4 Session memory | 230 |
| 5 Retrieval | 230 |
| 6 Practice and summary | 210 |
| Closing and sources | 70 |
| Total | 1,500 |

Where extra detail goes if the draft runs short: more steps in each trace, a second case of the same idea. Never a new topic.

## Sources
1. **Primary:** Anthropic Engineering, "Effective context engineering for AI agents", https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened this session). Supports: context as the set of tokens given to the model; context rot and the attention budget; just-in-time retrieval with lightweight pointers such as file paths; compaction; structured note-taking (NOTES.md, to-do lists) as memory outside the window; hybrid approach; "do the simplest thing that works".
2. Claude Platform Docs, "Context windows", https://platform.claude.com/docs/en/build-with-claude/context-windows (opened this session). Supports: the context window as the model's working memory, distinct from training data; each turn re-sends all prior history plus the new message and the output becomes part of the next input; tool results and tool definitions count toward the window; more context is not automatically better (context rot); compaction and tool result clearing as management; token counting API for estimating.
3. Not used: the Oracle agent memory page (https://docs.oracle.com/en-us/iaas/Content/generative-ai/memory.htm) returned 404 when opened, so do not cite it. Search snippets only (not opened) from Elastic, Sanity and others support the short-term versus long-term split; do not cite these unless the writer opens them.

## Accuracy notes for the writer
- Do not state real window sizes as fact without citing the Claude docs (they list 1M tokens for many current models and 200k for others); the lesson's numbers are illustrations.
- Say "the program" resends history, not "the model remembers"; this reinforces the open question from record 0002 that each step is a separate model call.
- Do not claim retrieval always uses vector search; keep it as "an index the program searches".
- Keep the Anthropic Discord and r/LocalLLaMA community suggestion only if the writer confirms a URL from a search; otherwise name the design review itself.
