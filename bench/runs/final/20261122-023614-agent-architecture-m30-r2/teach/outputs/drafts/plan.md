# Plan: lesson 0001, objective O3

- Lesson file to be: `lessons/0001-context-and-memory-what-the-model-sees-and-what-it-keeps.html` (lessons/ is empty; confirmed by listing, no lessons exist).
- Meta tags: `p3-minutes` = 30, `p3-objective` = O3.
- Learner: Riley. Python-comfortable, never called a model from code. Knows: model is text in, text out (record 0001); the agent loop (record 0002). Does NOT know tokens, context window, cost link, memory, retrieval. Prefers: example first with real numbers/text, then the idea; examples from the topic itself (user says X, tool picked, what comes back, reply); short; casual; why it matters at the end of a part.
- Quiz 0001 not yet graded, so the warm-up recalls only what record 0002 established (the loop, not "who runs the tool").
- Not teaching: multi-agent (sub-agents are only a one-line pointer to a later lesson), fine-tuning, deployment, vector database products, company comparisons (out of scope in MISSION.md).

## Title

**Context and memory: what the model sees on each call and what the agent keeps**

## The win

Anyone who learns this can decide, for any piece of information an agent needs, whether it belongs in the context window, in a saved note, or in a searchable store that is looked up only when needed.

## Opening (no heading; about 300 words, counted in the total)

- The title, 30 minutes, the win sentence, one sentence tying it to the makerspace assistant (answer from long manuals, remember each student's training status, small budget).
- Warm-up, two recall questions with answers revealed on demand, from record 0002 only: (1) "Name the four things that happen in one trip around the agent loop." (2) "In 'Is the laser cutter free on Friday?', which tool gets called and what comes back?" Answers: model asks for an action, action carried out, result goes back, repeat until final answer; calendar tool, list of free slots.
- Opening example (example-first): show a failure. Student Priya says on Monday "I passed the laser cutter safety training", and on Wednesday asks "Can I book the laser cutter?" The assistant says "I don't see any training on record, please complete it first." Two lines of text, then: "Why did it forget? That is today's lesson."
- No figure.

---

## Part 1: Context window: everything the model can see on one call (about 700 words)

**Key sentence:** The model knows only what is in the text it is handed on each call, and that text has a size limit. So before anything about memory, you need to know what counts as "handed over" and how it is measured.

**Word budget:** 700. Extra detail goes in the trace (more lines in the one worked trace), not in new ideas.

**Worked example (one):** a single call, laid out as the actual pieces of text for the makerspace assistant, with illustrative token counts, labelled "illustrative numbers":
1. System prompt: "You are the makerspace assistant. Be brief. Never book without checking the calendar." about 40 tokens (we'll say 800 for a realistic full prompt; pick one and keep it the same in Part 2: use 800).
2. Tool definitions: `check_calendar`, `book_slot` (600 tokens together).
3. The user message: "Is the laser cutter free on Friday?" (about 9 tokens).
4. The reply the model writes (counts too): tool request, about 40 tokens.
Total on this call: 800 + 600 + 9 = 1,409 tokens going in, plus 40 coming out. This shows the window holds input and output together ([Context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows): the system prompt, every message including tool results, tool definitions, and the output all count).

**Terms defined here, one at a time:** token (a chunk of text, roughly three-quarters of an English word on average; hedge as a rule of thumb, say "about"); context window (all the text the model can reference when writing a response, including the response; its "working memory", not what it learned in training); context (the text actually in the window on this call).

**Figure 1 (after the term "context window" is defined and the trace is shown):** "One call, packed into the window." A single wide horizontal bar split into four labelled segments, widths proportional to tokens: "Instructions (system prompt): 800", "Tool descriptions: 600", "Student's message: 9", "Model's reply: 40". Label for the whole bar: "Context window = the limit for all four together". No arrows. Caption: notice that before the student says anything, 1,400 tokens are already used.

**Common misconception to name:** M-window-is-memory, "the model remembers the earlier chat because it was trained on it / has it stored somewhere". Real case: call the model twice with just "My name is Priya" in the first call and "What is my name?" alone in the second; the second call has no name in it, so the model cannot know it. It only "remembers" if the program sends the first message again. (This builds on record 0001: knowledge = training plus the text given.)

**Why it matters (one line for the end of the part):** everything you want the assistant to know on a call has to be written into this window by your program.

**Source:** primary Anthropic context-windows doc.

---

## Part 2: Context accumulation: what is kept between steps, and what it costs (about 700 words)

**Key sentence:** Inside one request, the agent loop keeps adding to the window, because every step is a new call that gets sent the whole history again. That growth is what you pay for and what makes the model worse, which is why what stays in the window is a design choice.

**Word budget:** 700. Extra detail goes in more rows of the step table (one more tool call), not new concepts.

**Worked example (one):** the "Is the laser cutter free Friday, and book 2 pm if so" request as a 3-call trace with running totals (illustrative numbers; builds directly on the Part 1 base of 1,409):
1. Call 1 input: instructions 800 + tools 600 + student message 25 = 1,425. Model replies with a request for `check_calendar` (40). Window use so far 1,465.
2. Program runs the tool; result is Friday's slot list for the laser cutter, 300 tokens (a full day's list of slots as JSON).
3. Call 2 input: everything from call 1 (1,465) + tool result (300) = 1,765. Model replies `book_slot` request (45). Total 1,810.
4. Program runs `book_slot`; result "Booked, Fri 2 pm" 15 tokens.
5. Call 3 input: 1,810 + 15 = 1,825. Model writes final answer (35). Total 1,860.
Input tokens billed across the three calls: 1,425 + 1,765 + 1,825 = 5,015, even though the window at the end holds only 1,860. Say clearly: the same text is sent again each call (the docs describe each turn's input as all previous history plus the new message), so cost grows faster than the window does. (Billing detail: input and output tokens are priced separately; prompt caching can lower the price of repeated text; mention in one sentence and link the context windows doc; do not teach caching.)

**Terms defined here:** "kept between steps" = the message history the program re-sends; context rot (as the window fills, the model's recall and accuracy get worse, so more context is not automatically better; [Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Three ways to shrink what is kept, one line each: clear old tool results, summarise earlier steps (compaction), or keep a pointer and not the whole thing.

**Figure 2 (after the trace):** "The window grows at every step." A simple stepped bar chart (vertical bars, three bars) with exact values 1,465 (after call 1), 1,810 (after call 2), 1,860 (after call 3). Each bar split into a base block "Instructions and tools: 1,400" and a growing block labelled "Conversation so far". Label of a thin dashed line at the top: "Limit of the window". Arrow between bars: "Next call re-sends everything so far" (reason for each arrow). The text of the part must also say why the arrow exists. Comes after the trace.

**Common misconceptions:**
1. "A bigger window means I can stop caring what goes in." Real case: a 300-token slot list is fine, but if the assistant pastes a whole 40-page laser cutter manual (about 20,000 tokens) on every call, then in the 3-call example input cost goes from 5,015 to about 65,000 tokens (5,015 + 3 x 20,000), and the answer can get worse, not better (context rot).
2. "You pay for each token once." Real case: the 5,015 versus 1,860 numbers above.

**Why it matters:** our budget is per token, so cost per request is set by what we keep in the window and how many steps the loop takes.

**Sources:** context-windows doc (primary for the mechanics), Effective context engineering (context rot, finite attention budget, clearing old tool results as lightest compaction).

---

## Part 3: Persistent memory: what is kept between sessions (about 750 words)

**Key sentence:** When a session ends, the window is gone, so anything the assistant should know next visit has to be written down outside it and read back in. That is all "memory" means for an agent: notes that live outside the window.

**Word budget:** 750. Extra detail goes in a second trace (the next-visit trace), and a short recap of the difference between window and notes.

**Worked example (one):** Priya's training status across two visits (this resolves the opening failure). Illustrative store: one small file per student, `students/priya.json`.
Visit 1 (Monday), trace:
1. Student: "I passed the laser cutter safety training."
2. Model asks to call `save_note(student="priya", text="laser cutter safety training: passed Mon 17 Nov")` (the instructors' sign-off is the source of truth; see misconception below).
3. Program writes it to the file and returns "saved".
4. Reply: "Got it, I've noted that."
Session ends; the window is thrown away.
Visit 2 (Wednesday), new session, empty window:
5. Program starts by reading `students/priya.json` and putting its 40 tokens into the window (or the model calls `read_notes`).
6. Student: "Can I book the laser cutter Friday at 2?"
7. Model sees the note, calls `check_calendar`, then `book_slot`; reply confirms.
Cost note: the note is about 40 tokens, versus replaying all of Monday's chat (say 1,800 tokens) every visit.

**Terms defined here:** session (one conversation from start to end, one window); memory (information saved outside the window and loaded back when needed); client-side memory: the model only asks for a read or write, and the program does it, exactly like any tool from record 0002 ([Memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)); structured note-taking (the agent writes notes outside the window and reads them back later; [Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)). One short mention: the memory tool in the API stores files under `/memories`, the model views the directory first, and the program decides where it really lives and must reject paths outside it (path traversal), which matters for per-student privacy; one sentence, link.

**Figure 3 (after the two-visit trace):** "Two sessions, one notes file." Two columns "Monday session" and "Wednesday session" each a box with the label "Window (gone when the session ends)". Between them, a central box "Notes file for Priya (stays)". Arrow Monday window to notes file labelled "model asks to save a note; program writes it". Arrow notes file to Wednesday window labelled "program reads it at the start of the visit". Caption: only the arrows cross the gap between sessions.

**Common misconceptions:**
1. "The model learns from our chats, so it will remember next time." Real case: nothing in the model changes between Monday and Wednesday; with an empty Wednesday window it answers "no training on record", exactly the opening failure.
2. "Memory means storing the whole conversation." Real case: 1,800 tokens of chat versus a 40-token note; storing and replaying everything pays for every old token each visit and also fills the window (Part 2).
3. (Brief) "The model's note is the truth." Real case: if a student says "I'm certified on the laser cutter" with no instructor record, writing it down makes a wrong note; for a safety gate the assistant should read the instructors' records with a tool, not trust a self-reported note. Keep to two sentences; this is the one design judgement for Riley's review.

**Why it matters:** this is the "remember each student's training status between visits" requirement, solved with a few lines of Python and a file or database row.

**Sources:** Memory tool docs (primary for this part), Effective context engineering (note-taking, Claude playing Pokemon keeps tallies across thousands of steps; optional one-sentence aside in a margin note), Context windows doc tip on multi-session state.

---

## Part 4: Retrieval: finding the right page in a long manual (about 800 words)

**Key sentence:** The manuals are far too long to put in the window on every call, so the assistant looks up only the few passages that match the question. This is the third place information can live: a store you search, not one you carry.

**Word budget:** 800. Extra detail goes in a second concrete case (an exact-code lookup), not another technique.

**Worked example (one):** question "What's the max material thickness for the laser cutter?" against the laser cutter manual.
Setup (done once, before any student asks): split the manual into chunks of a few hundred tokens (about 60 chunks for a 20,000-token manual, assuming about 330 tokens each; illustrative); keep each chunk with its page number.
Trace:
1. Student asks the question.
2. Program (or a `search_manuals` tool the model calls) turns the question into a search query and scores every chunk against it.
3. The 3 best-matching chunks come back, about 330 tokens each = about 1,000 tokens, each labelled "laser_cutter_manual p.14", etc.
4. The model reads those 3 chunks in the window and answers "Up to 6 mm acrylic, 3 mm plywood (manual p. 14)", and cites the page.
Compare the numbers with Part 2: 1,000 tokens per lookup versus 20,000 for the whole manual, about 20 times fewer input tokens each call.
Second concrete case in the same part: the student types "Error E-214". Meaning-based search might return general error-code pages, while an exact-word search finds the string "E-214"; combining both works better ([Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval?utm_source=tldrai): embeddings capture meaning, BM25 matches exact words, Anthropic's example is "Error code TS-999"). Use a makerspace code for our example (invented, flagged "made-up code").

**Terms defined here:** retrieval (searching a store and putting only the best matches into the window); chunk; "search by meaning" (embedding) vs "search by exact words" (keyword/BM25), each in one plain sentence, no maths; just-in-time retrieval (keep a light reference and load the content only when needed; [Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Retrieval's weak spot: a chunk can lose what it refers to (Anthropic's example "The company's revenue grew by 3% over the previous quarter." names no company), so keep the machine name and section title with each chunk.

**Figure 4 (after the trace):** "Looking up a passage." Left to right: box "Manual, split into chunks (about 60)" then arrow "search: score each chunk against the question" to box "3 best chunks (about 1,000 tokens)" then arrow "put only these in the window" to box "Context window" then arrow "model writes the answer, quoting the page" to box "Reply to the student". Above, a dashed side box "Student's question" with an arrow into the first arrow, labelled "the question is what we search with". Numbers shown: 60 chunks, 3 chunks, about 1,000 tokens.

**Common misconceptions:**
1. "Retrieval means the model has learned the manual." Real case: a manual updated last week is found correctly the same day with no retraining, because the store is changed, not the model; this is also the fix for Riley's noted "outdated fact" problem (record 0001).
2. "Retrieval always returns the right page." Real case: the search returns the 3 nearest chunks even when none is relevant; ask about a machine that is not in the manuals and it still returns 3 chunks, so the assistant needs an instruction to say "not found" when the passages do not answer the question.
3. "We must build retrieval." Real case: Anthropic notes that if the whole knowledge base is under about 200,000 tokens (roughly 500 pages), you can put it all in the prompt, with prompt caching to make it cheaper ([Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval?utm_source=tldrai)); with 20,000 tokens per manual this is a real option, but given our budget the cost line in Part 2 still applies. State this as a trade-off, not an instruction; the learner decides.

**Why it matters:** this is "how it finds the right page in a long manual".

**Sources:** Contextual Retrieval (primary for this part), Effective context engineering (just-in-time retrieval, trade-off that runtime lookup is slower and needs good tool guidance).

---

## Part 5: Placement: deciding what goes in the window, in notes, or in a search store (about 900 words, includes the worked example and faded practice)

**Key sentence:** Now you have three places information can live, and each trades cost for convenience. The skill is picking one for each thing the assistant needs.

**Word budget:** 900 (about 250 for the rule and worked example, about 450 for the practice with hints and solutions, about 200 for the extra practice check and its feedback). Extra detail goes in one more row of the worked table, not new theory.

**The rule (4 lines, no new terms):** In the window: what is needed on almost every call and is small (instructions, tool descriptions, today's request). In notes: small facts about one person or one task that must survive the session (a student's training status). In a search store: large reference material where each question needs a little of it (the manuals).

**Worked example (one):** a decision table for the makerspace assistant, three rows done step by step with the reason and the token cost per call:
| Thing | Size | Needed when | Place | Reason |
| Rules ("never book without checking the calendar") | 800 | every call | window | small, needed on every call |
| Priya's training status | 40 | at visit start | notes, loaded at session start | per-person, must survive; small enough to load |
| Laser cutter manual | 20,000 | one question in twenty | search store | big; about 1,000 per lookup |
Then the per-request cost story: window base 1,400 + note 40 + 1,000 for one lookup, about 2,440 tokens, versus 21,400 if the manual were always included (a 9-times reduction; show the arithmetic: 1,400 + 20,000 + 40 = 21,440 vs 1,400 + 40 + 1,000 = 2,440).

**Faded practice (steps faded, hints before solutions):** Riley places three new items: (a) the booking calendar for the next 14 days for all machines (about 4,000 tokens, changes hourly), (b) a student's note "prefers morning slots" (10 tokens), (c) the 3D-printer troubleshooting guide (8,000 tokens). Step 1 given complete for (a) as a model: "Calendar changes hourly, so a saved copy would be stale: call `check_calendar` when needed, put only the answer in the window" (this ties to Part 2 clear/keep pointers and shows a fourth situation: live data comes from a tool, not memory). Step 2 half-given for (b): the "where" is asked, reasoning frame given. Step 3 blank for (c). Hints: "How big is it? How often is it needed? Does it differ per student?" Solutions revealed on demand after hints. Feedback on every option, including why the wrong places fail.
One extra multiple-choice check (equal-length options, correct answer not in first position): "A student asks the same manual question twice in one chat. What is true about the second call?" options about window re-sending, to check Part 2. Not to be reused in quiz 0002; the quiz will use new items.

**Figure 5 (after the table):** none, the table does the work (the lesson-level guidance says use tables for comparisons).

**Common misconception:** "Pick one memory method for everything." Real case: using notes for the manual (a 20,000-token note read every visit) or the window for the calendar (a stale 4,000-token copy that is wrong an hour later); each wrong placement has a visible cost in the tables above.

**Why it matters:** this is the design-review argument Riley will have to defend: "what the assistant keeps in context, what it saves, and how it finds the right page" (MISSION.md success criterion).

**Sources:** Effective context engineering (when to use which method: compaction for long back-and-forth, note-taking for milestones, hybrid of upfront and just-in-time), Memory tool docs, Contextual Retrieval.

---

## Part 6: Summary and where this leads (about 350 words)

**Key sentence:** There are three places information can live, and the window is the only one the model sees directly. So the job is choosing, call by call, what to put in it.

**Word budget:** 350 (summary 120, explain-it-yourself prompt 60, why it matters in the real world 80, go further 90). Extra goes to the recap of the opening failure resolved.

**Summary (3 to 5 lines):**
1. The model sees only the window, on every call, and everything in it costs tokens.
2. Within a request, the loop re-sends the history each step, so cost and clutter grow; keep only what the next step needs.
3. Between sessions, only what you save outside the window survives; keep notes small and per person.
4. For big reference material, retrieve a few passages per question instead of carrying the whole thing.
5. Choose the place by size, how often it is needed, and whether it is per person.

**Prompt:** "In your own words, explain to a teammate why the assistant forgot Priya's training on Wednesday, and which of the three places you would use to fix it." (No answer given in the lesson.)

**Real-world why:** the per-request cost and the memory design are what Riley will defend at the design review in five weeks.

**Next lesson pointer:** workflows versus agents (O4, if the course order holds) and when splitting into sub-agents pays off; one sentence only, since sub-agents are named in Effective context engineering as another context tactic (a sub-agent works in its own clean window and returns a short summary of about 1,000 to 2,000 tokens) but are not taught here.

**Go further:** primary source (below); two to four other sources; community: for testing the skill in the real world, a developer community such as the Anthropic Discord or r/LocalLLaMA/r/LLMDevs (not yet verified by a search in this session; the lesson writer must find and verify one by search before linking it, or leave it as plain text).

**Closing:** reminder to ask follow-ups in chat; quiz ready on request.

---

## Budget table

| Part | Words |
|---|---|
| Opening and warm-up | 300 |
| 1. Context window | 700 |
| 2. Context accumulation | 700 |
| 3. Persistent memory | 750 |
| 4. Retrieval | 800 |
| 5. Placement (worked example and faded practice) | 900 |
| 6. Summary and go further | 350 |
| Total | 4,500 |

(4,500 words is 150 per minute for 30 minutes; the range that fits the bench's estimate is 2,700 to 6,750.)

## Misconceptions tracked for later quiz distractors (propose new ids; none exist yet in the workspace)

- M-a: the model remembers earlier calls by itself (Part 1, Part 3).
- M-b: a bigger window means no need to curate; each token is paid once (Part 2).
- M-c: memory means storing the whole conversation / the model learns from chats (Part 3).
- M-d: retrieval means the model has learned the manual / always returns the right page (Part 4).
- M-e: one placement for everything (Part 5).
The learner's files have no misconception ids yet; the teach step should assign `M1` onward in order, since keys/0001.json is the only place that might already use ids (the planner did not open keys/0001.json to check; check it before assigning).

## Sources and the claim each supports

1. **PRIMARY.** Anthropic Engineering, "Effective context engineering for AI agents", https://anthropic.com/engineering/effective-context-engineering-for-ai-agents (opened). Supports: context is the set of tokens the model sees; context rot and attention budget; smallest set of high-signal tokens; just-in-time retrieval with lightweight references; compaction and clearing old tool results; structured note-taking as memory; sub-agents return condensed 1,000 to 2,000 token summaries; guidance on when to use which method. It is the one source that covers all five parts, by the model's own maker.
2. Claude API docs, "Context windows", https://platform.claude.com/docs/en/build-with-claude/context-windows (opened). Supports: the window is the model's working memory, not training data; everything counts (system prompt, messages, tool results, tool definitions, output); each turn's input is all earlier history plus the new message; context rot; compaction and tool-result clearing; window size up to 1M tokens depending on the model (state size only generally; the docs list varies by model and changes, so the lesson says "up to about a million tokens on current models" and links the page rather than naming models).
3. Claude API docs, "Memory tool", https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool (opened). Supports: memory is a directory of files that persist between sessions; client-side (the model requests, the application runs it); `/memories` check at the start of a task; view, create, str_replace, insert, delete, rename commands; path traversal and sensitive-information safeguards; size caps and expiry.
4. Anthropic Engineering, "Introducing Contextual Retrieval", https://www.anthropic.com/engineering/contextual-retrieval?utm_source=tldrai (opened; the search result URL included a tracking parameter, so use it exactly as seen, or the clean form https://anthropic.com/news/contextual-retrieval, also seen in search results). Supports: RAG steps (chunk, embed, store, retrieve top matches); chunks losing context (the "revenue grew by 3%" example); BM25 versus embeddings with the "Error code TS-999" example; under about 200,000 tokens you can put the whole knowledge base in the prompt, with prompt caching.

Not used: the Medium, eWeek, GitHub-mirror and translated pages seen in search results (secondary).
Figures quoted from the docs that I did not verify elsewhere: none beyond those above; every token count in the examples is made up for the lesson and must be labelled "illustrative numbers" in the lesson.
