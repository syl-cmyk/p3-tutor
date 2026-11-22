# Plan: lesson for O3 (30 minutes, about 4,500 words)

**Objective O3:** Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.

**Lesson title:** Context and memory: what an agent sees on each call and what it keeps

**The win (one sentence):** By the end, you can say what goes into an agent's context window on each call, what must be saved outside it to survive between steps and sessions, and when to load information into the window by retrieval or by notes.

**Meta tags for the writer:** `p3-minutes` = 30, `p3-objective` = O3. Proposed file: `lessons/0001-context-and-memory.html` (next number in `lessons/`, which is empty at planning time; recheck).

**Learner facts that shape the plan** (from NOTES.md, PREFERENCES.md, records 0001 and 0002):
- Riley knows: a model turns text in into text out, one token at a time; the agent loop (model asks, program runs the tool, result goes back, repeat).
- Riley does NOT know yet: what a token is, what the context window limits, why either affects cost. Tokens must be introduced in Part 1, before anything else uses them.
- Not yet checked (record 0002): that every step is a separate model call and that the program, not the model, runs tools. Part 2 relies on "every step is a separate call", so it re-teaches that in one line and traces it.
- Prefers: example first, then the idea; real numbers and real text; short; casual; why-it-matters at the end of each part.
- Mission: makerspace assistant answers from long machine manuals, checks the booking calendar, books time, remembers each student's training status between visits; small model budget, so cost per request matters.

**Illustrative numbers rule:** the figures below for the makerspace (manual length, number of booking rows) are made up for teaching. The writer must label them "say" or "for example". Rates and ratios from sources are real and cited.

## Budget table

| Piece | Words |
|---|---|
| Opening (win, why it matters, time) and warm-up recall | 250 |
| Part 1: Token | 550 |
| Part 2: Context window | 700 |
| Part 3: Context accumulation and compaction | 700 |
| Part 4: Retrieval | 750 |
| Part 5: Persistent memory with notes | 700 |
| Part 6: Context budget design (worked example, faded practice) | 600 |
| Summary, own-words prompt, go further, closing | 250 |
| **Total** | **4,500** |

Where the extra detail goes (never a new topic): one more step in each trace, one more concrete case of the same idea (a second tool result, a second student), and a short recap line at the end of each part.

---

## Opening and warm-up (250 words)

- Open with the win, the 30-minute time, and two sentences tying it to the mission: the assistant must answer from long manuals and remember training status, on a small budget.
- Warm-up recall (answers on demand), from records 0001 and 0002: (1) "In the loop, who runs the tool, the model or your program?" (2) "Why can a chatbot state an outdated fact confidently?" Spacing only; not quiz items.
- Link: earlier lessons do not exist yet in `lessons/`, so no links; mention the loop and the model-as-text-in-text-out ideas in plain words.

---

## Part 1: Token: the unit a model reads, writes and bills by (550 words)

**Key sentence:** Everything an agent reads and writes is counted in small pieces of text, and those pieces are what you pay for. So before we talk about what the agent sees, we need the unit it is measured in.

**Word budget:** 550. Extra detail goes in a second counted example (the calendar result) and a short recap.

**Worked example (makerspace, built from nothing earlier than the opening):**
Show a short real student message and break it into pieces on screen, for example "Is the laser cutter free on Friday?" shown as pieces such as `Is | the | laser | cutter | free | on | Friday | ?` (label as a simplified split; real splits vary by model). Then size it with real ratios: a typical 10 kB web page is about 2,500 tokens, so about 4 characters of English per token ([pricing page: web fetch example](https://platform.claude.com/docs/en/about-claude/pricing)). A 120-page laser-cutter manual, say, at about 400 tokens a page (the contextual retrieval article puts 500 pages at 200,000 tokens, which is 400 per page) is about 48,000 tokens. Cost trace with real prices, labelled as one example model: at $2 per million input tokens and $10 per million output tokens (the listed price of Claude Sonnet 5.5), 48,000 input tokens cost 48,000 x 2 / 1,000,000 = $0.096 for one call. Output tokens cost 5 times as much per token ($10 vs $2).

**Figure 1 (optional, small):** a horizontal strip of boxes, one per piece of the sentence "Is the laser cutter free on Friday?" (8 boxes), with a bracket under it "8 tokens (simplified)". Label: "one box = one token". Comes after the definition of token. Alt text/title required.

**Common misconceptions:**
- "A token is a word." Counter: "Friday" may be one piece, but a long part number such as a model code or a word with an unusual spelling splits into several pieces; the same text gives different counts on different models (the pricing FAQ says Claude 4.7 and later models produce about 30% more tokens for the same text than earlier ones). Real case: count with the provider's token-counting tool rather than guess.
- "Only what I type costs money." Counter: input tokens (everything sent) and output tokens (everything the model writes) are both billed, at different rates ($2 vs $10 per million in the example).

**Why it matters (end of part):** budget is spent in tokens, so every later choice in the lesson is a choice about tokens.

---

## Part 2: Context window: what the model can see on one call (700 words)

**Key sentence:** The model only sees what is sent to it on each call, and that has a size limit. So at every step, someone is choosing what goes in.

**Word budget:** 700. Extra detail goes in a fuller trace of one call (four labelled parts listed with token counts) and the "limit" paragraph.

**Worked example (makerspace):** Trace the first call of the assistant for "Can I use the laser cutter Friday at 2?" Show the actual list of what is sent, with token counts (illustrative):
1. System instructions (who the assistant is, rules): 400 tokens.
2. Tool descriptions (`search_manual`, `check_calendar`, `book_slot`): 600 tokens (the provider counts tool definitions as input; see the pricing page's tool-use section and the context-windows page: "Everything in the request counts ... the system prompt, every message ... and your tool definitions").
3. The student's message: 15 tokens.
4. Total sent on this call: 1,015 tokens. The model writes its reply (say 40 tokens), which also counts toward the window.
Then the point: the model has no other source. It does not "look up" a manual unless text from it is in the window (links back to record 0001: it knows only training plus what it is given).
State the real limit: windows are large now (up to 1M tokens on current models per the context-windows doc) but "more context isn't automatically better": accuracy and recall degrade as the token count grows, called context rot.

**Figure 2:** One tall rectangle labelled "Context window (one call)" containing four stacked boxes: "System instructions: 400", "Tool descriptions: 600", "Student message: 15", "Room for the reply". Arrow from the stack to a box "Model" labelled "everything here is read on this call"; arrow from "Model" to a box "Reply" labelled "reply tokens also count". Numbers: 400, 600, 15. Comes after the trace.

**Common misconceptions:**
- "The model remembers the manual because I showed it last week." Counter: nothing persists inside the model between calls; show a call with an empty window where the student asks "What did I ask yesterday?" and the model has nothing to answer from.
- "A bigger window means I can paste everything." Counter: real case, 48,000-token manual on every call costs $0.096 each call at $2/MTok; and context rot ([Anthropic context engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): recall falls as the window fills).

**Why it matters:** the window is both the thing that limits what the assistant knows and the thing that sets the cost of each call.

---

## Part 3: Context accumulation and compaction: what is kept between steps (700 words)

**Key sentence:** In the loop, every step is a new call, and the window grows as results pile up. So you decide what stays, what gets cleared, and what gets summarized.

**Word budget:** 700. Extra detail: a fifth step in the trace showing the cost growing, and one more clearing example.

**Worked example (makerspace):** A four-step trace of one request "Book me the laser cutter for Friday afternoon, and tell me the kerf setting for 3 mm acrylic". Each step is a separate call, and the whole history is sent again (context-windows doc: "each user message and assistant response accumulates ... previous turns are preserved completely"). Illustrative sizes: base 1,015 tokens.
1. Call 1 sends 1,015; model asks `check_calendar(laser, Friday)`.
2. Program runs the tool; result is 40 booking rows, say 1,200 tokens.
3. Call 2 sends 1,015 + 40 (its tool request) + 1,200 = about 2,255; model asks `search_manual("3 mm acrylic kerf")`; result 1,500 tokens.
4. Call 3 sends about 3,800; model asks `book_slot`; result 30 tokens.
5. Call 4 sends about 3,850; final answer.
Total input tokens billed across the four calls: 1,015 + 2,255 + 3,795 + 3,850 = 10,915, about 10 times the original. At $2/MTok that is about $0.022 for the request. Then show the fix: clear the old calendar rows after the booking is made (the lightest compaction; clearing old tool results), so call 4 sends about 2,650. Mention summarizing: when the window nears its limit, summarize and start a new window from the summary ([context engineering article](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents); [context windows doc](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Mention prompt caching in one line: repeated prefixes can be read at a fraction of the price (cache read 0.1x on most models; 0.05x on the Sonnet 5.5 example) but they still occupy the window.
(Writer: recompute every sum before publishing; the numbers above must add up exactly.)

**Figure 3:** A vertical bar chart with 4 bars for the four calls: 1,015; 2,255; 3,795; 3,850 tokens sent. Each bar stacked: base (1,015, same in every bar), calendar rows (1,200 from call 2 on), manual chunks (1,500 from call 3 on), small extras. Label for each segment in plain words. Axis: "tokens sent on this call". A dashed fifth line: "call 4 after clearing the calendar rows: about 2,650". Reason for the arrow from call to call: "the whole history is sent again". Comes after the trace.

**Common misconceptions:**
- "The model remembers earlier steps by itself." Counter: the program resends the history on every call; if your code drops the calendar result from the list, the next call has no idea what the calendar said.
- "Cost is the size of the question." Counter: the trace above, 10,915 billed input tokens for a 15-token question.

**Why it matters:** per-request cost in a loop is dominated by what you keep resending, which is the lever the sponsor budget gives you.

---

## Part 4: Retrieval: loading only the page you need (750 words)

**Key sentence:** A long manual should not ride along on every call. Keep it outside the window, search it, and put in only the few passages that answer the question.

**Word budget:** 750. Extra detail: a second query to show the exact-match case (error code) and the semantic case.

**Worked example (makerspace):** The manual is split ahead of time into chunks of a few hundred tokens each (real: "usually no more than a few hundred tokens", [Anthropic contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval)); each chunk is stored with its page number. Trace the request "What does error E-214 on the laser cutter mean?":
1. Student message arrives; window has instructions and tools (1,000 tokens).
2. Model calls `search_manual("laser cutter error E-214")`.
3. Program searches the stored chunks and returns the top 3 chunks, say 3 x 300 = 900 tokens, each with manual name and page.
4. Model reads them and answers "E-214 means the exhaust fan is not detected; check the cable at the back panel (laser manual, p. 62)".
Cost: about 1,900 input tokens at $2/MTok is $0.0038, versus $0.096 with the whole manual: about 25 times cheaper (0.096 / 0.0038 = 25.3). Two ways to search, in plain words: by meaning (embeddings) and by exact words (BM25, "works well for unique identifiers such as an error code"); show that "E-214" is the exact-words case and "why does my cut look burnt" is the meaning case; real systems combine both ([contextual retrieval](https://www.anthropic.com/engineering/contextual-retrieval)). State the failure: a chunk like "Check the cable at the back" loses which machine it is about; the fix is to attach a note saying which manual and section it belongs to. Small-collection shortcut: under about 200,000 tokens (about 500 pages) you could include it all and cache it; say when that is sensible and when the budget says no. Name the trade-off: retrieval can miss the right page, so the assistant must show the page it used.
Tie it to the idea that agents can keep light references and load on demand ("just-in-time"; [context engineering article](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

**Figure 4:** Left-to-right flow of four boxes: "Manual (120 pages, split into chunks, stored outside the window)" -> "Search: finds the 3 best chunks" -> "Context window: 900 tokens of chunks added" -> "Model answers with a page number". Arrow reasons: "the question is turned into a search", "only the best chunks come back", "the model reads only these". Numbers: 120 pages, 3 chunks, 900 tokens. Comes after the trace.

**Common misconceptions:**
- "Retrieval means the model searches the manual itself." Counter: the program runs the search and returns text; the model only sees the returned chunks (same rule as in the loop).
- "Retrieval always finds the right page." Counter: real number: in the contextual retrieval article's tests, a baseline setup missed the right chunk in the top 20 about 5.7% of the time; so keep the page numbers in the answer and test with real student questions.

**Why it matters:** this is how the assistant answers from a long manual within a small budget.

---

## Part 5: Memory: notes the agent saves outside the window (700 words)

**Key sentence:** When a session ends, the window is gone. Anything the assistant must know next visit has to be written down somewhere outside it, and read back in.

**Word budget:** 700. Extra detail: a second student's visit showing that memory is per student, and a short "what not to save" list.

**Worked example (makerspace: student training status):** Two-visit trace for one student.
Visit 1 (Monday):
1. Student: "I just finished the laser cutter safety training."
2. Model calls the memory tool: `create /memories/students/riley.md` with "Laser cutter: trained 2026-11-23. Prefers mornings."
3. Program writes the file and returns "File created successfully at: /memories/students/riley.md".
4. Reply: "Got it, you're cleared for the laser cutter." Session ends; the window is discarded.
Visit 2 (Thursday, new empty window):
1. Student: "Can I book the laser cutter tomorrow at 9?"
2. Model calls `view /memories/students/riley.md`; the program returns the file text.
3. Model sees trained status, calls `check_calendar`, then `book_slot`.
4. Reply confirms the booking.
Explain that the memory tool is client-side: the model only asks for file operations; your program runs them against storage you control ([memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)), and the docs' protocol line "assume interruption: your context window might be reset at any moment" (the API adds it automatically). Say what to save (training status, preferences) and what not (the manual, which belongs to retrieval; live booking data, which belongs to the calendar tool because notes go stale: a stale note saying "slot free" is the same failure as the outdated chatbot fact in record 0001). Safety in two lines: restrict paths to the memory folder, and do not store sensitive data (docs' security section). Also name the pattern for long jobs: progress notes at the end of a session, read at the start of the next ([context engineering article](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents): "structured note-taking").
Distinguish three kinds of "memory" in a small table: within one call (the window), between steps of one request (the history resent), between sessions (notes/files, a database). One row each with "what holds it", "who writes it", "what happens at session end".

**Figure 5:** Timeline with two columns, "Monday session" and "Thursday session", each with a window box. A cylinder box "Memory file: riley.md" between them, arrow from Monday window to file labelled "model asks to save, program writes it", arrow from file to Thursday window labelled "model asks to read, program returns it". Monday window crossed out at the end labelled "window discarded". Comes after the trace.

**Common misconceptions:**
- "The model learned my training status, so it will remember." Counter: the Thursday window is empty; without the file read, the assistant would ask for training again (or worse, book without checking). Real case: the trace's step 1.
- "Save everything, just in case." Counter: every note read back costs tokens each visit; a 5,000-token notes file read on every call at $2/MTok costs $0.01 per call and adds noise; keep short, organized files (docs advise keeping the directory organized and expiring old files).

**Why it matters:** it is the difference between an assistant that treats each student as a stranger and one that does not.

---

## Part 6: Context budget: deciding what goes where (600 words)

**Key sentence:** Now you can place every piece of information in the right spot: in the window, retrieved, or saved. Here is one worked decision, then one for you.

**Word budget:** 600 (worked example about 280, faded practice about 260, hints and solutions about 60 of the overlapping text; the writer keeps solutions in on-demand reveals, which still count as visible words).

**Worked example (makerspace), then faded practice:**
Worked: a placement table for the assistant, filled step by step with reasons:
| Information | Where | Why |
|---|---|---|
| Role and rules (200 to 400 tokens) | always in the window | needed on every call, small |
| Tool descriptions | always in the window | the model can only call what it can see |
| Machine manuals (48,000 tokens each) | retrieval | too big and mostly irrelevant on any call |
| Booking calendar | tool call, then clear after use | changes constantly; stale if saved |
| Student training status | notes file, read at start of a session | must survive the session; small |
Then a one-line cost check: with retrieval and clearing, a typical request sends about 3,000 tokens per call instead of about 50,000.

Practice with the steps faded (hints before solutions, answers revealed on demand): three new items the lesson has not used: (a) the makerspace's safety rules for the 3D printer (a 2-page document the assistant needs on nearly every printer question); (b) "last week the student said they prefer afternoon slots"; (c) the current list of broken machines this week. Step 1 given as a full example row; step 2: learner places each item with a reason, with a hint ("how often is it needed? does it change? must it survive the session?"); step 3: learner estimates tokens sent per call for their plan, with the hint "add the always-present parts, then one retrieved chunk set". Solutions on demand.
Expected solutions: (a) in the window or retrieval (short and needed often: window; tell the learner both can be defended if they give a reason about size); (b) notes file; (c) a tool call to a status source (changes weekly, so not a saved note unless refreshed).
Practice questions must not match the quiz items; the quiz writer should use different cases (e.g. a different machine and a different kind of change).

**Figure 6 (optional, only if the word budget allows):** the placement table as a three-lane diagram "In the window / Retrieved on demand / Saved between sessions" with the five items from the worked table placed in lanes; arrows are not needed.

**Common misconceptions:**
- "One mechanism should cover everything (just a huge window, or just notes)." Counter: show the table: the manual in notes would mean the model writes and rereads 48,000 tokens; the calendar in notes would go stale; the training status in the window alone would vanish at session end.

---

## Summary, own-words prompt, go further, closing (250 words)

**Summary (three to five lines):**
1. Tokens are the unit of reading, writing and cost.
2. The window is everything the model sees on one call, and bigger is not better.
3. Between steps, the program resends the history, so clear or summarize what is no longer needed.
4. Retrieval loads only the passages that answer the question.
5. Notes are files outside the window that carry facts between sessions.
**Prompt:** "In your own words, say where the assistant should keep the manual, the calendar and a student's training status, and why."
**Go further:** the primary source (below), plus two or three of the other sources. Wisdom/community: point to a real forum only if found in a search; none was searched here, so the writer may omit or search once more before naming one.
**Closing:** reminder that they can ask follow-up questions in the chat and that a short quiz on this lesson is ready when they are. Next lesson hint: writing a tool description (mission success item 2), and when to split work across agents (sub-agents get clean windows; mention only as a teaser).
**Cheat sheet:** write `cheatsheets/context-and-memory.html` with the three kinds of memory table (window / history / notes), the token cost formula and the placement table. Also add every source to RESOURCES.md and the new terms (token, context window, context rot, compaction, retrieval, chunk, memory file) to GLOSSARY.md.

---

## Sources

All opened in this session. Primary source is marked.

1. **PRIMARY.** Anthropic Engineering, "Effective context engineering for AI agents": https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents . Supports: context is a finite resource and recall falls as it fills (context rot); keep light references and load on demand (just-in-time retrieval); compaction (summarize, clear old tool results); structured note-taking outside the window; sub-agents return short summaries (teaser only).
2. Claude API docs, "Context windows": https://platform.claude.com/docs/en/build-with-claude/context-windows . Supports: the window is all text the model can reference including its reply; previous turns accumulate; system prompt, messages, tool results and tool definitions all count; up to 1M tokens on current models; context rot; compaction and tool-result clearing.
3. Claude API docs, "Memory tool": https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool . Supports: client-side memory, the model requests file operations and the app runs them; files under /memories persist between sessions; the view-first protocol and "assume interruption"; security (path restriction, sensitive information, size caps, expiry); multisession progress-log pattern; pairing with compaction.
4. Anthropic Engineering, "Introducing Contextual Retrieval": https://www.anthropic.com/engineering/contextual-retrieval . Supports: chunks of a few hundred tokens; embeddings vs BM25 (BM25 good for unique identifiers like error codes); top-K chunks added to the prompt; chunks lose context; under about 200,000 tokens (about 500 pages) you can include everything and cache it; baseline failure rate of 5.7% in top 20.
5. Claude API docs, "Pricing": https://platform.claude.com/docs/en/about-claude/pricing . Supports: price per million input and output tokens (Claude Sonnet 5.5: $2 and $10), output costs more per token, tools and tool results count as input tokens, cache reads at a fraction of input price, average 10 kB web page is about 2,500 tokens, newer tokenizers produce about 30% more tokens for the same text.

Not yet verified, so do not cite: a community URL for the "Wisdom" section; a standalone page defining "token" (the pricing FAQ gives a one-line definition: "Tokens are pieces of text that models process").

## Notes for the writer

- Introduce tokens before the context window; never use "token" in an opener before Part 1 defines it. Part openers contain no numbers and no new terms.
- All traces are numbered, one line per step: student message, what the system decides, what comes back, the reply.
- Every example number must be recomputed and consistent across parts (48,000-token manual; 1,015-token base; 10,915 total; $0.096 vs $0.0038).
- Do not compare AI companies; use one named model's price only as "one example price".
- Use "Riley" only if the lesson addresses the learner by name; the makerspace appears only in examples, never in the lesson title or the win.
