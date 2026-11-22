# Plan for lesson 0001 (objective O3, 30 minutes, 4,500 words)

**Lesson file to be written:** `lessons/0001-context-window-and-memory.html` (meta `p3-minutes` 30, `p3-objective` O3).

**Title:** Context and memory in an agent: what it sees now, what it keeps, and what it looks up

**Win (general form):** By the end, you can say what goes into a model's context window on each call, what is carried between steps and between sessions, and when to fetch text by retrieval or save notes as memory instead of keeping everything in context.

**Learner:** Riley (Python, no model-API experience). Prefers an example first and then the idea, real numbers, short paragraphs, casual voice, and "why it matters" at the end. Examples are always: what the user says, which tool, what comes back, what the assistant replies. The makerspace assistant appears only inside examples, never in the title or the win.

**Builds on:** learning record 0001 (a model only knows its training plus the text it is given) and 0002 (the agent loop). Quiz 0001 is not graded yet; do not reuse its items. There are no earlier lessons, no glossary and no cheat sheets, so this is lesson 0001 and has nothing to link back to.

**Numbers rule:** every token count in the examples is an illustrative number made up for the lesson, and the lesson says so once, in one line. The only real figures quoted are the ones from the sources below.

**Shared vocabulary, introduced in this order (one new term at a time):** token, context window, system prompt, tool definition, tool result, conversation history, context rot, compaction, retrieval, chunk, memory (notes saved outside the context).

**Budget:** 800 + 800 + 700 + 800 + 800 + 600 = 4,500 words. The opening, warm-up and "go further" are counted inside Parts 1, 6 and 6 respectively, so there are exactly six headed parts.

---

## Part 1. Context window: what the model can see on one call

**Budget: 800 words.** Split: opening with win and mission link and warm-up (about 200), the part's explanation with its trace and figure (about 400), misconceptions and practice check (about 200). The extra detail goes into a second concrete count, a tool definition costing tokens (the 403-token tool example), not into new ideas.

**Key sentence:** The model can only use the text it is handed on each call, and that text has a size limit. So before we talk about keeping anything, we need to know what that text is made of and how it is measured.

**Warm-up (in the opening, answers revealed on demand):** (1) In the agent loop, who actually runs the tool, the model or the program? (2) Why can a chatbot state an outdated fact with confidence? Both come from records 0002 and 0001.

**Content:**
- Token: the unit the model reads and writes, a word or a piece of a word. Cost and limits are counted in tokens. Source example: a request with the system prompt "You are a scientist" and the user message "Hello, Claude" counts as 14 input tokens, and adding one small tool definition and a question brings it to 403, so tool definitions cost tokens too.
- Context window: all the text the model can reference when generating a response, including the response itself. Everything in the request counts: system prompt, every message, tool results and tool definitions. Source: the context-windows page. Real sizes: up to 1M tokens on current models. The same page says it is like working memory, as opposed to what was learned in training (ties back to record 0001).
- Billing: input and output tokens are billed (the thinking docs say output tokens are billed once when generated; the history is billed as input). So context size is a cost lever, which is the budget constraint in MISSION.md.

**Worked example (makerspace):**
1. User says: "Is the laser cutter free on Friday?"
2. The program builds the request: system prompt (600 tokens, illustrative), tool definitions for `check_calendar`, `book_slot` and `search_manuals` (900 tokens), the user message (20 tokens). Input is 1,520 tokens.
3. The model replies with a tool request: `check_calendar(machine="laser cutter", date="Friday")` (40 tokens of output).
4. Everything the model "knows" about the makerspace on this call is in those 1,520 tokens; nothing else is visible.

**Figure 1 (shown after the trace): "One call, as a stack of blocks."** A vertical stack, labels in plain words: "Instructions for the assistant (system prompt): 600", "Descriptions of the tools it may use (tool definitions): 900", "The student's message: 20", total "Input: 1,520 tokens", and a separate block to the side "The model's answer: 40" with the arrow label "also counts toward the window". Arrows: stack to model, "the model reads all of this on every call".

**Misconceptions:**
- "The model remembers the makerspace because it was told once." Real case: the 600-token system prompt is sent again on every call. If it were left out of call 2, the model would not know it is the makerspace assistant. (The window is working memory, not storage.)
- "Only my question counts." Real case: in the example the student's question is 20 of 1,520 tokens (about 1 percent); the rest is instructions and tool descriptions.

**Practice check (mcq, four options of equal length, correct option not first):** "A call sends a 600-token system prompt, 900 tokens of tool definitions and a 20-token question. How many input tokens is that?" Feedback explains each wrong option (20 only counts the question; 1,500 forgets one block; 620 forgets tool definitions).

---

## Part 2. Conversation history: what is kept between steps

**Budget: 800 words.** Split: opener and trace (about 350), the figure and the cost sum (about 200), the second user turn as an extra concrete case (about 150), misconception and check (about 100). Extra detail goes into a longer trace (more steps), not a new idea.

**Key sentence:** The model itself keeps nothing from one call to the next, so the program has to resend everything each time. That is why every step makes the next one bigger and costlier.

**Content:** Each agent step is a separate model call. The program holds the list of messages and appends to it: previous turns are preserved completely and each call's input is all earlier history plus the new message (context-windows page, "progressive token accumulation"). The tool result is appended as a message, then the whole list goes back. Billing counts the input each time, so two steps cost more than the sum of their new text.

**Worked example (makerspace), numbered trace with token counts:**
1. User: "Is the laser cutter free on Friday?" Call 1 input: 1,520 tokens.
2. Model output: tool request `check_calendar(machine="laser cutter", date="Friday")` (40 tokens).
3. The program runs the tool (the model does not) and gets back `{"free": ["10:00-12:00", "15:00-17:00"]}` (150 tokens).
4. Call 2 input: the 1,520 tokens + the 40-token request + the 150-token result = 1,710 tokens.
5. Model output: "Yes, it's free Friday 10 to 12 and 3 to 5. Want me to book one?" (30 tokens). Stop.
6. Total input billed across the two calls: 1,520 + 1,710 = 3,230 tokens, even though only 190 tokens of new text appeared. Output billed: 70 tokens.
7. Next turn, student says "Book 3 to 5, please" (10 tokens). Call 3 input: 1,710 + 30 + 10 = 1,750 tokens, because the earlier turn is still in the history.

**Figure 2: "The same history, resent on each call."** Three columns for call 1, call 2 and call 3, each a stack that grows: call 1 = [fixed instructions and tools 1,500, question 20] = 1,520; call 2 adds [model's tool request 40, calendar result 150] = 1,710; call 3 adds [model's reply 30, new question 10] = 1,750. Arrow label between columns: "everything so far is copied forward, then the new part is added". The part's text states the same reason. Comes after Figure 1.

**Misconceptions:**
- "The model remembers the calendar result from step 2 on its own." Real case: if the program forgets to append the 150-token result before call 3, the model sees no calendar data and may invent times. The program, not the model, keeps the history.
- "A step costs only its new text." Real case: step 2 costs 1,710 input tokens, not 190.

**Practice check (short, immediate feedback):** "Call 3 added a 25-token reply and a 15-token question to the 1,750-token history. What is the call 4 input?" (answer: 1,750 + 25 + 15 = 1,790; hints first, then the sum). Keep it clearly different from the worked example's numbers.

---

## Part 3. Context rot and compaction: why a fuller window is not a better one

**Budget: 700 words.** Split: opener and example trace (about 300), figure (about 100), the two fixes (clearing, compaction) in short (about 200), misconception and check (about 100). If the learner needs more, add a third lookup to the trace; do not add new techniques.

**Key sentence:** A big window does not mean the model uses everything in it equally well, and old tool results mostly sit there doing nothing. So the assistant should keep only what the next step needs and drop or shrink the rest.

**Content:**
- Context rot: as the token count grows, accuracy and recall degrade, across models, some more gently than others. Curating what is in context matters as much as how much room there is (context-windows page; Anthropic's context-engineering post says the goal is "the smallest set of high-signal tokens" that gets the outcome).
- Fix 1, clear old tool results: the lightest form (context-engineering post; context editing is named on the context-windows page).
- Fix 2, compaction: when the conversation nears the limit, summarize it and continue from the summary (both sources).
- Cost link: a 3,000-token manual page left in history is resent on every later call.

**Worked example (makerspace):** a long chat with a student who asks five questions about the 3D printer.
1. Each answer needs a manual page: `search_manuals` returns about 3,000 tokens per lookup.
2. After five lookups the history holds 1,520 + 5 x 3,000 = 16,520 tokens (illustrative, ignoring replies).
3. Only the last page matters for the next question ("what temperature for PETG?").
4. The program replaces the four older results with a one-line placeholder such as "[page 41 read, removed]". New size: 1,520 + 3,000 = 4,520 tokens.
5. The next call is about 12,000 tokens smaller, and the model has less to be distracted by.
6. If the student keeps going for an hour, the program asks the model for a short summary of the chat and starts a new window with that summary (compaction).

**Figure 3: "Before and after clearing old results."** Two horizontal bars. Bar A "Before: 16,520 tokens" = instructions and tools 1,520 + five blocks of 3,000 each, labeled "manual page 1" to "manual page 5". Bar B "After: 4,520 tokens" = instructions and tools 1,520 + one 3,000 block "manual page 5" + four tiny blocks labeled "placeholder". Arrow label: "old pages removed because the next step does not need them". Comes after the trace.

**Misconceptions:**
- "A 1M-token window means I can leave everything in." Real case: current models have windows up to 1M tokens, yet the docs say accuracy and recall degrade as tokens grow; also, 16,520 tokens are billed on every call while only 3,000 matter.
- "Clearing results loses the answer." Real case: the student's earlier questions and the model's earlier replies stay; only the raw page text goes, and the program can fetch the page again if needed.

**Practice check (mcq):** which of three histories to trim first (an old 3,000-token manual page, the 600-token system prompt, the student's current question). Correct is the old page; the system prompt is needed on every call and the question is what to answer now.

---

## Part 4. Retrieval: finding the right page in a long manual

**Budget: 800 words.** Split: opener and trace (about 300), figure (about 100), keyword-versus-meaning and lost-context cases (about 250), misconception and check (about 150). Extra detail goes into the second concrete case (an error code), not a new idea.

**Key sentence:** The manuals are far too long to keep in the window, so the assistant looks up only the few pieces it needs when a question comes in. That leaves the window small and the answer grounded in the real page.

**Content:**
- Retrieval: search a body of text for the pieces that match the question and put only those in the context (contextual-retrieval post).
- Chunks: the text is split ahead of time into small pieces, a few hundred tokens or fewer. Each chunk is indexed two ways: by meaning (embeddings: each chunk becomes a list of numbers that captures its meaning, searchable by similarity) and by exact words (BM25, which helps with identifiers and technical terms that meaning-search can miss, for example an error code such as "TS-999").
- Chunks lose context: a chunk saying "revenue grew 3%" does not say which company or period. For the makerspace, a chunk saying "Set power to 60%" does not say which machine or material. Fix: add a one-line label of machine and section to each chunk before indexing.
- Just-in-time: keep a lightweight pointer (file path, page id) and load the full text only when needed (context-engineering post).
- When you do not need it: a knowledge base under about 200,000 tokens (about 500 pages) can sit in the prompt, and prompt caching makes that cheaper (contextual-retrieval post). Say what this means for the team: count the manuals' tokens first; if they fit, start without retrieval, and add it when they do not or when cost per request is too high. Flag this as the lesson's advice, not the source's.
- Cost: the contextual-retrieval post's numbers (top-20 failures down from 5.7% to 1.9% with contextual embeddings, contextual BM25 and reranking) are shown as a single line to say retrieval quality is measurable, not as something to build now.

**Worked example (makerspace):**
1. User: "What power and speed for 3 mm acrylic on the laser cutter?"
2. The model calls `search_manuals(query="laser cutter acrylic 3 mm power speed", top_k=3)`.
3. The program searches the index and returns three chunks (about 300 tokens each, 900 in all), each with its label: "Laser cutter manual, p. 52, cutting acrylic: 3 mm, 60% power, 12 mm/s" and two others.
4. The model reads the three chunks, which are now in the history (Part 2).
5. Reply: "For 3 mm acrylic on the laser cutter, use 60% power at 12 mm/s (manual page 52). Wear the eye protection listed on page 8."
6. Second case, error code: the user types "Printer shows E-47". Meaning-search returns general error-handling pages; the exact-word index finds the chunk containing "E-47". The program combines both.

**Figure 4: "From long manual to three useful chunks."** Left to right boxes: "All the manuals, split into small chunks (done once, ahead of time)" -> "Index: find by meaning and by exact words" -> "Student's question turned into a search" -> "Top three chunks, 900 tokens" -> "Context window". Arrow reasons: "split so each piece is small enough to return", "so a search is fast", "the model writes the query through the search tool", "only the best matches are sent". Comes after the trace and builds on Figure 1's idea that the window is a stack of blocks.

**Misconceptions:**
- "Retrieval means the model has learned the manual." Real case: the model only sees the 900 tokens returned for this question; ask the next question about a different machine and it must search again.
- "A chunk is self-explanatory." Real case: "Set power to 60%" appears for both the laser cutter and the engraver, with different material settings; without a machine label, the search may return the wrong one.
- "Always build retrieval." Real case: a 150-page set of manuals is well under the 200,000-token threshold; retrieval adds work, and the real reason to add it is cost per request.

**Practice check (mcq):** which index finds "E-47" reliably (exact-word, meaning-only, neither, can't tell). Correct: exact-word index.

---

## Part 5. Persistent memory: notes that last between sessions

**Budget: 800 words.** Split: opener and two-session trace (about 350), figure (about 100), the memory tool's shape and safety (about 200), misconception and check (about 150). Extra detail goes into the trace's second session; no new topic.

**Key sentence:** When a conversation ends, everything in the window is gone, so anything the assistant should know next time has to be written down outside it. The assistant can then read those notes at the start of the next session.

**Content:**
- Between steps, the program holds the history (Part 2). Between sessions, nothing is kept unless the program saves it.
- Memory as notes: the agent writes what it learns to files and reads them back on demand, keeping the window focused (memory-tool docs; "structured note-taking" in the context-engineering post).
- How the memory tool works: the model asks for a file operation (`view`, `create`, `str_replace`, `insert`, `delete`, `rename`) under a `/memories` folder; the program runs it against storage the team controls and returns the result, the same loop as any tool. It is client-side, so the data lives in the team's own storage. When the memory tool is enabled the model is told to view its memory directory first.
- Safety, kept short: validate every path so it stays inside `/memories`, cap file sizes, expire old files, and do not store sensitive data (memory-tool docs).
- Design judgment (flag as the lesson's advice, not the source's): a fact that decides whether a student may use a machine, such as training status, should live in the makerspace's own record that the program looks up through a tool; the notes file holds soft things such as "prefers morning slots". Notes can be stale or wrong, and a model-written note is not a safety record.
- Retrieval versus notes: retrieval reads a fixed body of text someone else wrote; notes are written by the assistant for its future self.

**Worked example (makerspace), two sessions:**
Session on Monday:
1. User: "I just finished the laser cutter safety training. Also, I always book mornings."
2. The model calls `memory(command="create", path="/memories/students/maya.md", file_text="Prefers morning slots. Mentioned finishing laser cutter training on 2026-11-17 (unverified, check the training record).")`.
3. The program writes the file and returns "File created successfully at: /memories/students/maya.md".
4. Reply: "Nice, noted. I'll suggest mornings when you book."
Session on Thursday (new window, empty history):
5. User: "Book the laser cutter Saturday."
6. The model calls `memory(command="view", path="/memories/students/maya.md")`; the program returns the file text.
7. The model calls `check_calendar(machine="laser cutter", date="Saturday")` and gets `{"free": ["09:00-11:00", "14:00-16:00"]}`.
8. Reply: "Saturday morning is free, 9 to 11. Want me to book it? I'll check your training record first."
Point: the first line of the Thursday window held nothing from Monday; step 6 put the notes back in.

**Figure 5: "Two sessions, one notes file."** A timeline with two boxes (Monday window, Thursday window) separated by a gap labeled "window is thrown away". Between and below, a box "Notes file: /memories/students/maya.md" with an arrow from Monday labeled "the assistant writes what is worth keeping" and an arrow to Thursday labeled "the assistant reads it back at the start". Comes after Figure 4 and echoes Figure 2's "resend" idea: notes are resent only when read.

**Misconceptions:**
- "The model remembers me between chats." Real case: Thursday's window starts empty; without step 6 the model has no idea the student likes mornings.
- "Memory means the provider stores my data." Real case: the memory tool is client-side; the team's program writes and reads the files, so the team decides where they live and how long.
- "Whatever is in memory is true." Real case: Monday's note says training finished, but the student only said so; the Thursday reply checks the record.

**Practice check (mcq):** for four facts (the laser cutter's cutting settings, whether a student passed training, "likes mornings", today's calendar), which belong in retrieval, a record the program looks up, notes, or a tool result. Immediate feedback per option.

---

## Part 6. Context design: deciding where each piece of information lives

**Budget: 600 words.** Split: a worked example (about 220), a faded practice task (about 200), summary and prompt to explain in own words (about 80), go further, sources, and closing (about 100). If short on time, trim the practice, not the summary. Extra detail goes into the worked example's steps.

**Key sentence:** Every fact an agent needs has one best home: always in context, looked up when needed, or saved between sessions. Choosing the home for each fact is the design decision you will defend in review.

**Worked example (a full request, every piece placed):** Maya writes: "Can I use the CNC router tomorrow afternoon? I'm a new user."
1. System prompt (always in context): the assistant's role and the rule "check the training record before booking". 600 tokens.
2. Tool definitions (always in context): `check_calendar`, `book_slot`, `search_manuals`, `get_training_status`, `memory`.
3. Notes (read at the start of the session): "prefers mornings".
4. Retrieval (looked up when needed): `search_manuals("CNC router new user rules")` returns 2 chunks (600 tokens).
5. Tool result (kept for a few steps, then cleared): `get_training_status("maya")` returns `{"cnc_router": "not completed"}`.
6. Reply: "Not yet. The CNC router needs the intro session first (manual p. 4). Want me to find one?" and the program writes "asked about CNC router; needs intro session" to the notes.
Show a table with columns Fact, Home, Why. The table is the one table of the lesson.

**Faded practice task (hints before the solution):** the same pattern with a 3D printer request, where the first row is filled in, the second half-filled, and the rest blank. Task: "A student asks, 'Is the 3D printer free tomorrow, and what nozzle size do I need for the flexible filament?'" Learner places: the printer rules (system prompt), the calendar answer (tool result), the nozzle size (retrieval), "wants flexible filament again next time" (notes). Hint 1: which of these changes by the minute? Hint 2: which of these exists in a manual already? Solution revealed on demand.

**Summary (three to five lines):**
1. The model sees only the context window, and everything in it is counted in tokens and billed.
2. The program keeps the history between steps and resends it, so each step costs more than its own text.
3. A fuller window is not a better one: trim old results and compact long chats.
4. Retrieval fetches the few matching chunks from long manuals; notes carry facts between sessions.
5. Place each fact where it belongs: always in context, looked up, or saved.
Prompt: "In your own words, tell a teammate why the assistant doesn't paste all the manuals into every call." Next lesson: cost and decision-making are left for later lessons, tool descriptions come next in the mission.

**Why it matters (real world):** the sponsor's budget is paid in tokens, so context choices are cost choices, and each of the three homes is a line you can defend at the design review.

**Go further (primary source plus others):** see Sources. Add a community pointer for testing the skill: the lesson-writer should search for a high-reputation forum or class for building agents with the Claude API and cite only a page seen in search. Closing: reminder to ask follow-up questions in chat and that a short quiz on this lesson is ready (fresh items, not the practice checks above).

---

## Figures summary (for the figure designer)

| # | After which idea | Shows | Exact numbers |
|---|---|---|---|
| 1 | Part 1 trace | stack of blocks for one call | 600, 900, 20, total 1,520; reply 40 |
| 2 | Part 2 trace | three calls with growing history | 1,520; 1,710; 1,750 |
| 3 | Part 3 trace | before and after clearing | 16,520 to 4,520; five blocks of 3,000 |
| 4 | Part 4 trace | manual to chunks to context | three chunks, 900 tokens |
| 5 | Part 5 trace | two sessions and a notes file | file `/memories/students/maya.md` |

Every figure is inline SVG with a `<title>`, labels of 18 units or more in a viewBox about 640 wide, colors from the template, and a `<figcaption>` saying what to notice.

---

## Sources (each URL was opened in this session)

1. **PRIMARY.** Anthropic, "Effective context engineering for AI agents" (Sep 29, 2025). https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
   Supports: context engineering as curating the tokens in the window; context rot and the finite attention budget; "smallest set of high-signal tokens"; just-in-time retrieval with lightweight pointers; compaction; clearing old tool results as the lightest form; structured note-taking outside the window; hybrid of up-front and on-demand loading.
2. Claude API docs, "Context windows". https://platform.claude.com/docs/en/build-with-claude/context-windows
   Supports: the window is all text the model can reference, including its own response, and acts like working memory; each turn's input is all earlier history plus the new message; system prompt, messages, tool results and tool definitions all count; windows up to 1M tokens; accuracy and recall degrade as tokens grow (context rot); compaction and tool-result clearing; prompt caching changes the price, not whether tokens count.
3. Claude API docs, "Memory tool". https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool
   Supports: memory persists across conversations as files under `/memories`; client-side, the application runs each operation; the six commands; the tool_use and tool_result flow; the instruction to view memory first; path traversal, size, expiry and sensitive-data safeguards; compaction plus memory together.
4. Claude API docs, "Token counting". https://platform.claude.com/docs/en/build-with-claude/token-counting
   Supports: tokens as the unit that rate limits and costs are counted in; the example counts of 14 and 403 input tokens (tool definitions count); counts are estimates; newer models' tokenizer gives about 30 percent more tokens for the same text, so recount for the model you pick.
5. Anthropic, "Introducing Contextual Retrieval". https://www.anthropic.com/news/contextual-retrieval
   Supports: retrieval, chunking, embeddings, BM25 and the "TS-999" exact-term case; chunks losing context; the 200,000-token (about 500 pages) threshold for skipping retrieval; failure rates of 5.7% falling to 1.9% in the best combination.

**Checks for the lesson-writer:** do not claim a specific model's price; do not state a tokens-per-word ratio, since no opened source gives one; say that all makerspace token counts are illustrative; mention that Claude Sonnet 5.5 and similar models have 1M windows only if needed, citing source 2.
