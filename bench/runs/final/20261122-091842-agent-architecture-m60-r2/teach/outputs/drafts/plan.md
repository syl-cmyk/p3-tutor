# Lesson plan: O3, context and memory in an agent

**Objective (O3):** Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
**Length:** 60 minutes, 9,000 words (150 per minute; floor 120 per minute = 7,200). Planned total: 9,000.
**Learner:** Riley. Example first, then idea. Casual, short paragraphs (max three sentences). Real traces from the makerspace assistant (manuals Q&A, booking calendar, per-student training status). If a part is too long, make it shorter and simpler, never longer.

## Title

**Context engineering: what an agent sees, what it keeps, and what it looks up**

## The win (one sentence, general)

By the end, you can take any agent, list what is in its context window on each model call, and decide what to keep there, what to clear, what to fetch only when needed, and what to save as notes for later sessions.

(Riley's makerspace assistant appears only inside examples, never in the title or the win.)

## Build-on and warm-up

- Builds on learning record 0001 (the model sees only what it was trained on plus the text it is given) and 0002 (the agent loop: model asks, program runs the tool, result goes back, repeat).
- Warm-up (inside Part 1, answers on demand): (1) "In the loop, who actually runs the tool, the model or your program?" (2) "Where does a chatbot's knowledge stop?" These also close the open item from record 0002.
- No lessons or cheatsheets exist yet in `lessons/` or `cheatsheets/`, and no GLOSSARY.md or RESOURCES.md: there is nothing to link back to except the learning records. The lesson must add RESOURCES.md entries and could add a cheat sheet ("What goes in the window: keep, clear, fetch, save").
- New terms, one at a time, each defined where it first appears: token, context window, context rot, tool result clearing, compaction, chunk, embedding, retrieval (RAG), memory file, session.

## Cost numbers used throughout (illustrative, labelled as such in the lesson)

- A made-up round price of $3 per million input tokens, only so arithmetic is easy. The lesson says to look up the real price before the design review. Do not present it as a quote.
- Token sizes in examples are invented but consistent across parts (see each part). Say so once: "these numbers are made up but realistic; the real counts come from the token counting tool".

---

## Part 1. Context window: what the model can see on one call (1,500 words)

**Key sentence:** The model only knows what is in the text it is handed on this one call, so everything it could use has to fit in there. That limit, and what counts toward it, is where context and memory both start.

**Budget:** 1,500 words = opening and win (200), warm-up (150), the example and its trace (450), the idea: token and context window (350), figure caption and text (100), one practice check with feedback (250). Extra detail goes into more lines in the worked trace (list every block in the request) and one more short case of "what counts", not a new topic.

**Worked example (example first):** The real first request to the assistant: "Is the laser cutter free on Friday?" Show the full request the program sends, as a block list with made-up token counts:
1. System prompt (rules, tone): 800 tokens
2. Tool definitions (`check_calendar`, `search_manual`, `book_slot`): 600 tokens
3. The student's question: 20 tokens
4. Total sent in: 1,420 tokens. The model's reply (a `check_calendar` request, 40 tokens) also counts toward the window.
Then say what a token is (a small chunk of text, often a word or part of a word; a word is not one token) and define the context window: everything the model can reference on one call, including its own reply.

**Figure 1 (after the example and the definition of context window):** A single horizontal bar "One call's context window" split into four labelled boxes: "Rules we gave it (system prompt): 800", "Descriptions of its tools: 600", "The student's question: 20", "Room left for its reply and more: the rest". Numbers plotted: 800, 600, 20; total used 1,420. Arrow from "tool descriptions" to the bar is not needed; one bracket labelled "Everything here counts, even what you never typed". Comes after the definition of token and context window.

**Misconceptions to name:**
- "A token is a word." Real case: the docs say the same text counts as roughly 30 percent more tokens on newer models than older ones (the newer tokenizer), so a 1,000-token prompt on an old model is about 1,300 on a new one. Token counts are estimates and must be re-measured on the model you pick ([token counting docs](https://platform.claude.com/docs/en/build-with-claude/token-counting)). This is why a cost estimate from one model does not carry over.
- "Only my message counts toward the window." Real case: the 800 + 600 token rules and tool descriptions above are sent and counted every call, before the student types a word.
- "The window is the model's training data." Real case: the docs say the window is "working memory", different from the training corpus; record 0001's chatbot with the outdated fact is the contrast.

**Practice check (multiple choice, equal-length options, correct option not first):** Which of these count toward the window on Riley's call? Options built from the example above; feedback says why each wrong one is tempting.

---

## Part 2. Conversation history: what is kept between steps (1,500 words)

**Key sentence:** The model does not remember the last step; your program hands it the whole story again each time. So the window grows with every step, and so does the bill.

**Budget:** 1,500 words = example trace (550), the idea and the cost arithmetic (400), figure text (100), misconception cases (200), practice check (250). Extra detail goes in more steps of the trace (a third call for a booking) and a second line of arithmetic, not new concepts.

**Worked example:** Same request, now two calls, from the loop in record 0002.
1. Call 1 input: 1,420 tokens (from Part 1). Model output: a request to run `check_calendar` for Friday (40 tokens).
2. The program runs the tool. Result: Friday's laser cutter slots, 300 tokens.
3. Call 2 input: the whole thing again: 1,420 + 40 + 300 = 1,760 tokens. Output: the final answer, "Free 2 to 4 pm", 60 tokens.
4. Input tokens billed over the request: 1,420 + 1,760 = 3,180, not 1,760 and not 300.
5. Add a third call (student says "book 2 pm"): call 3 input = 1,760 + 60 + the new message 10 + ... (the plan uses: 1,760 + 60 + 10 = 1,830 for the next user turn, then a tool request 40 and tool result 50 gives call 4 input 1,920). Keep the lesson's sums on one line each so Riley can check them. Total input across calls 1 to 4 = 1,420 + 1,760 + 1,830 + 1,920 = 6,930. Cost at the made-up price: 6,930 / 1,000,000 x $3 = about $0.021 per conversation.

Idea after the trace: the model is stateless per call; the "memory" within a conversation is just the message list your program keeps and resends. The docs say each turn's input is "all previous conversation history plus the current user message" and that previous turns are preserved completely ([context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)). Between steps = the list in your program. Anything not in the list is gone.

**Figure 2 (after the trace):** Stacked vertical bars, one per call (Call 1, Call 2, Call 3, Call 4), heights 1,420; 1,760; 1,830; 1,920. Stack segments: "Rules and tool descriptions (1,400, same every call)", "Question", "Model's earlier replies", "Tool results". Label on the arrows between bars: "everything from before is sent again, plus the new part". The caption says what to notice: the bottom block is paid for every call.

**Misconceptions to name:**
- "The model remembers the earlier steps by itself." Case: if the program forgot to append the `check_calendar` result, call 2 would contain 1,420 + 40 tokens and the model could not answer; it would either ask again or guess.
- "Cost is just the length of my latest message." Case: 6,930 input tokens billed for a conversation whose newest message is 10 tokens.
- "The window just stops when full." Case: if the input alone is over the limit the API returns an error ("prompt is too long", a 400); if the input fits but generation hits the limit, the reply is cut off with a stop reason. Either way the agent fails in the middle of a job, so budget before it happens.

**Practice check:** A fill-in arithmetic task: given a similar two-call trace with new numbers (system and tools 1,000; question 30; first output 50; tool result 200; final answer 70), compute the input tokens billed in total (answer 1,080 + 1,330 = 2,410; the lesson must not reuse this in the quiz). Feedback on the common slip of counting only the last call or forgetting the model's own tool request.

---

## Part 3. Context rot and context editing: why a fuller window is not a better one (1,300 words)

**Key sentence:** A bigger window does not mean the model uses all of it well, and old results you no longer need still cost money every call. So you choose what stays, and clear or summarise the rest.

**Budget:** 1,300 words = example trace (450), the idea and the three tools (clear, summarise, fetch later) (400), figure text (100), misconceptions (150), practice check (200). Extra detail goes in a before/after line count of the same trace, not in more techniques.

**Worked example:** The student asks: "How do I change the lens on the laser cutter, and is it free Friday?"
1. Call 1: input 1,420. Output: `search_manual("laser cutter lens change")`.
2. The tool returns a whole manual chapter: 5,000 tokens. The model needs only a few lines of it.
3. Call 2: input 1,420 + 40 + 5,000 = 6,460. Output: `check_calendar` request, 60 tokens.
4. Call 3: input 6,460 + 60 + 300 (calendar result) = 6,820. Output: final answer.
5. With the chapter cleared once it has been used (leave a short stub saying a search ran, say 20 tokens): call 3 input = 6,820 - 5,000 + 20 = 1,840 tokens. Saves 4,980 tokens on that call, and on every later call in the conversation.
6. Another way: summarise. When the history nears the limit, the program (or the platform) replaces old messages with a short summary and carries on (this is compaction; defined here in plain words).

Idea: Context rot: as the token count grows, the model's accuracy and recall at finding things in the window get worse ([context windows docs](https://platform.claude.com/docs/en/build-with-claude/context-windows), [Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)). So the aim is "the smallest set of high-signal tokens", not the biggest window. The three tools: clear old tool results (the lightest), summarise the old history (compaction), and do not load it at all until needed (leads to Part 4).

**Figure 3 (after the trace):** Two horizontal bars for call 3, same scale. Top: "Before clearing: 6,820" split into "Rules and tools 1,400", "Chapter 5,000", "The rest 420". Bottom: "After clearing: 1,840" split into "Rules and tools 1,400", "Stub saying a search ran 20", "The rest 420". Arrow between them labelled "chapter removed after the model used it". Comes after the clearing step.

**Misconceptions to name:**
- "A bigger window means I can stop thinking about what goes in." Real case: the docs state that many current models have a 1M-token window and still warn that more context is not automatically better because of context rot. A 1M window does not make a 5,000-token chapter free: it is still resent and billed every call.
- "Clearing a result means the agent forgets it did the search." Case: the stub, or a short note, keeps the record that the call happened, and the tool can be called again if the full text is needed (the docs describe clearing as removing re-fetchable results while keeping a record).
- "Summarising loses nothing." Case: a summary that drops "booked for 2 pm on Friday" makes the agent offer the slot again; anything that must survive a summary should be written to notes (Part 5).

**Practice check:** Given a short trace with one large result, pick which token block to clear and compute the new input. Feedback on why clearing the system prompt or the student's question would be wrong (the model still needs it).

---

## Part 4. Retrieval-augmented generation (RAG): finding the right page in a long manual (1,600 words)

**Key sentence:** A long manual cannot sit in the window on every call, so the assistant looks up only the few pieces that match the question. This is how it finds the right page without paying to read the whole manual each time.

**Budget:** 1,600 words = example trace (550), the idea in four steps (chunk, embed, search, top few) (450), figure text (100), when not to use it (150), misconceptions (150), practice check (200). Extra detail goes into a second query in the trace (an exact error code) to show why exact matching matters, not a new technique.

**Worked example:** The laser cutter manual is 120 pages, about 60,000 tokens (made-up, 500 tokens a page). Prepared once, offline:
1. Split the manual into chunks of about 300 tokens: 200 chunks.
2. Turn each chunk into a list of numbers (an embedding) that is close to the lists of chunks with a similar meaning, and store them.
At question time:
3. Student: "What's the thickest acrylic I can cut?" The program turns the question into numbers the same way and finds the 3 nearest chunks (about 900 tokens). Retrieved: the "Materials and thickness limits" chunk, and two neighbours.
4. Only those 3 chunks go into the window as the tool result. Compare: whole manual = 60,000 tokens = $0.18 per call at the made-up price; 3 chunks = 900 tokens = $0.0027 per call (about 67 times cheaper: 60,000 / 900).
5. Second query: "What does error E-42 mean?" Meaning-based search may return chunks about errors in general; a plain word-match search (the Anthropic post names BM25) finds the exact string "E-42". Real systems combine both and keep the top few ([Contextual Retrieval](https://www.anthropic.com/engineering/contextual-retrieval)).

Idea: retrieval is memory for knowledge that is large and mostly unchanging: look it up when needed rather than carry it. In the agent loop it is just another tool (`search_manual`) whose result lands in the window like any other, so Parts 2 and 3 apply to it. Honest trade-off: the same source says that if the whole knowledge base is under about 200,000 tokens, you can skip retrieval and put it all in the prompt (with prompt caching making that cheaper). So the choice is a cost and accuracy trade-off for the design review, not a rule. Also mention the "just-in-time" idea: keep lightweight pointers (a file path, a page number) and load the content when needed ([Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)).

**Figure 4 (after the idea in four steps):** Left-to-right flow with boxes: "Manual (120 pages, 60,000 tokens)" -> "Cut into pieces (200 chunks of about 300 tokens)" -> "Each piece stored as a list of numbers (search index)"; below, a second row at question time: "Student's question" -> "Question turned into numbers and matched against the pieces" -> "3 best pieces (900 tokens)" -> "Into the window as a tool result". Arrow reasons in a few words: "split so each piece is small enough to fetch alone", "so similar meaning means nearby numbers", "only the closest are worth paying for", "the model answers from them". Appears after the four steps are explained.

**Misconceptions to name:**
- "Retrieval makes the model know the manual." Case: the model reads the 3 chunks fresh each call; if the answer is in a chunk that was not retrieved, it answers from guesswork (record 0001's confident wrong fact). The Anthropic post's baseline missed relevant chunks 5.7 percent of the time in the top 20, and the best pipeline there (context added to chunks, both search types, reranking) still missed 1.9 percent.
- "Meaning-based search is always enough." Case: the E-42 query above; exact identifiers need word matching.
- "RAG is always the right answer for documents." Case: a 30-page quick-start guide of 15,000 tokens may be cheaper and simpler to include whole, especially when cached.

**Practice check:** Choose the better design for three documents (the 60,000-token laser manual, a 4,000-token safety card, a 300-page vendor handbook), and give a reason using token counts. Feedback explains each.

---

## Part 5. Persistent memory: notes that survive between sessions (1,500 words)

**Key sentence:** When a conversation ends, the window is gone, so anything the assistant should know next visit has to be written down somewhere outside it. Notes are how it remembers a student, and loading them is just another step in the loop.

**Budget:** 1,500 words = example: two visits, as a trace (600), the idea and who does what (300), figure text (100), misconceptions (200), one design note (privacy, size, staleness) (100), practice check (200). Extra detail goes in more lines in the second-visit trace (an update at the end of the visit), not in new storage types.

**Worked example (the mission's own case):** Student Dana, two visits.
Visit 1:
1. Dana: "Can I use the laser cutter?" The assistant checks the notes folder first: no file for Dana.
2. It calls `check_training` (tool from the booking system), which says Dana finished the safety orientation only.
3. It tells Dana she needs the laser training. Before ending, it writes `/memories/students/dana.md` (about 40 tokens): "Dana: orientation done 2026-09-14. Laser training not done. Asked about laser."
Visit 2 (new session, empty window; the old messages are gone):
4. Dana: "Ok I did the laser class, can I book Friday?"
5. The assistant lists the notes folder, reads `dana.md` (40 tokens into the window), sees laser training was pending, calls `check_training` to confirm (the system of record, not the note), then books.
6. It updates the note: "Laser training done 2026-11-18. Booked laser Fri 2 pm."
Cost of remembering: 40 tokens per visit, not a whole old conversation of thousands.

Idea: between steps = message list; between sessions = something stored outside the window, and that you fetch. In Anthropic's memory tool, the model asks for file operations (view, create, edit, rename, delete) under a `/memories` folder and your program carries them out against storage you control, such as a per-user folder or database ([memory tool docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool)). When the tool is on, the model is told to check the folder at the start of a task and to assume its context may be reset at any time. The same pattern is called structured note-taking in the context-engineering post ([Effective context engineering](https://anthropic.com/engineering/effective-context-engineering-for-ai-agents)). Notes can be something else than files: a database row keyed by student id works for the same job; the requirement is that the program stores it and loads it.

**Figure 5 (after the idea):** Two columns, "Visit 1" and "Visit 2", each with a short window box (grey) labelled "Window: gone when the visit ends", and one shared box in the middle labelled "Notes folder: kept by our program". Arrows: "write a note at the end" (visit 1 to notes), "read the note at the start" (notes to visit 2), each with the 40-token size. Comes after the idea. Caption: the notes survive; the window does not.

**Misconceptions to name:**
- "The model learned about Dana, so it will remember her." Case: nothing in the model changes (record 0001: the model is the same text predictor); visit 2's window is empty, and the only reason it knows Dana is the 40-token file it read.
- "The model's memory is stored by the vendor." Case: the memory tool is client-side: the model only requests operations and your application stores the files, so what to keep, for how long and who can read it is your design decision (and your risk). The docs warn to validate paths (a request for `/memories/../../secrets.env` must be rejected), to cap file size and to expire old notes.
- "A note is always true." Case: Dana's note says laser training not done; she did it a week later. That is why step 5 re-checks with `check_training`. Notes are hints with dates, and the booking system stays the source of truth.

**Practice check:** Which of four facts should go in notes, which be re-fetched from a tool, and which stay only in the current window? (e.g. "Dana prefers afternoons", "Friday's calendar", "the manual's lens-change steps", "Dana's training status"). Feedback per item.

---

## Part 6. Context design: deciding what to keep, fetch and save (1,600 words)

**Key sentence:** Now put the three kinds of memory together and decide, for each thing the assistant needs, where it should live. This is the call you will defend at the design review, and the cost per request is the reason it matters.

**Budget:** 1,600 words = worked example done in full (500), faded practice task (350), hints then solutions on demand (200), why it matters for the design review and budget (150), summary of 3 to 5 lines (150), prompt to explain it back in own words (50), go further: sources and a community (100), closing reminder about asking questions and a ready quiz (50). Extra detail goes into the worked example (one more line item in the table), not a new idea.

**Worked example (fully done):** A table for the assistant, one row per thing it needs, with the where-it-lives decision, a reason in a few words, and a rough token cost:
| Need | Where it lives | Why | Tokens per call |
|---|---|---|---|
| Rules and tone | In the window every call (system prompt) | Needed every step; small | 800 |
| Tool descriptions | In the window every call | The model cannot use tools it cannot see | 600 |
| Messages and results of this visit | Message list, with old big results cleared | Needed between steps; cleared when used (Part 3) | grows |
| Manual content | Retrieved, top 3 pieces | Large and rarely needed whole (Part 4) | about 900 only when asked |
| Calendar | Fetched by a tool each time | Changes constantly; stale if saved | 300 |
| Student's training status | Notes, plus re-check with the booking tool before booking | Must survive between visits, but can go stale (Part 5) | 40 |
Then total a typical request: 1,400 + 20 + 40 (notes) + 900 (retrieval) + 300 (calendar) + replies about 100 = about 2,760 tokens in on the busiest call, versus the 60,000+ of the "paste the manual in" design. Say what would change the decision (a small manual, a long visit).

**Faded practice task:** Same table method for a second case with a different mix: the assistant also needs "which machines are down for maintenance this week" (changes daily, short), "the 3D-printer manual (25 pages, 12,500 tokens)", and "a student's saved preference for afternoon slots". Step 1 given in full (rules and tool descriptions); step 2 half given (where the maintenance list lives, reason left blank); steps 3 and 4 left to Riley. Hints first (a hint per row: "Does it change between visits? Is it big? Must it survive the end of the visit?"), then solutions on demand, with a sentence on each reason.

**Why it matters (real world):** What goes into the window each call decides the cost per request and how well the assistant answers; the memory design decides whether a student has to re-explain their situation at every visit, and what student data you store. The three decisions in the mission (what to keep in context, what to save between sessions, how to find the right page) are exactly this table.

**Summary (3 to 5 lines to write):**
1. The model sees only the window on each call; everything counts, including rules, tool descriptions and its own replies.
2. Between steps, the program resends the whole message list, so the window and the bill grow with every step; clear or summarise what is done.
3. Big knowledge (manuals) is retrieved a few pieces at a time instead of carried.
4. Between sessions, only what is written outside the window survives: notes that the program stores and loads, checked against the real source before acting.
5. More room is not better; the aim is the smallest set of tokens that does the job.

**Next lesson pointer:** workflows versus agents (what to fix in code and what to leave to the model), which uses this table to decide which steps need the model at all.

**Go further (primary source plus two to four others, see Sources) and a community:** point to the Anthropic Discord or the r/ClaudeAI subreddit or the r/LocalLLaMA community for practice (the lesson writer should confirm the exact link by search before linking; do not link from memory). Reminder to ask follow-up questions in chat; a short quiz is ready.

---

## Word budget check

| Part | Words |
|---|---|
| 1. Context window: what the model can see on one call | 1,500 |
| 2. Conversation history: what is kept between steps | 1,500 |
| 3. Context rot and context editing: why a fuller window is not a better one | 1,300 |
| 4. Retrieval-augmented generation (RAG): finding the right page in a long manual | 1,600 |
| 5. Persistent memory: notes that survive between sessions | 1,500 |
| 6. Context design: deciding what to keep, fetch and save | 1,600 |
| **Total** | **9,000** |

(1,500 + 1,500 + 1,300 + 1,600 + 1,500 + 1,600 = 9,000, which equals 150 per minute and is above the 120 per minute floor.)

## Practice and quiz hygiene

- Each part's practice check is new; the quiz must use fresh questions and different numbers. Faded task: worked example then practice with the steps faded and hints before solutions (Part 6). Multiple-choice options all the same length; right answer positions varied (not always first, not always last).
- Misconception ids: none exist in the workspace yet (keys/0001.json is for quiz 0001 only). The writer should check `keys/0001.json` and `quizzes/0001.json` for existing ids before naming new ones, and never invent an id for something that already has one.

## Sources

| Source | URL | Supports |
|---|---|---|
| **PRIMARY.** Anthropic Engineering, "Effective context engineering for AI agents" | https://anthropic.com/engineering/effective-context-engineering-for-ai-agents | Context as a limited resource ("attention budget"), context rot, smallest set of high-signal tokens, just-in-time retrieval with lightweight pointers, compaction, clearing old tool results, structured note-taking outside the window. Read in full this session. Covers all three parts of O3 in one place, which is why it is primary. |
| Claude Platform docs, "Context windows" | https://platform.claude.com/docs/en/build-with-claude/context-windows | Definition ("all the text a language model can reference when generating a response, including the response itself"; "working memory", not training data); each turn's input is the whole history plus the new message; everything counts (system prompt, messages, tool results, tool definitions, output); context rot; overflow error behavior; compaction and tool result clearing; 1M-token windows on current models. |
| Claude Platform docs, "Memory tool" | https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | Memory is client-side files under `/memories`; commands (view, create, str_replace, insert, delete, rename); model checks memory first and assumes interruption; path traversal protection, size caps, expiry; multi-session pattern (read at start, update at end). |
| Anthropic Engineering, "Introducing Contextual Retrieval" | https://www.anthropic.com/engineering/contextual-retrieval | RAG steps (chunk, embed, search by similarity, BM25 for exact terms, top-K into prompt); skip RAG under about 200,000 tokens (about 500 pages); failure-rate numbers 5.7%, 3.7%, 2.9%, 1.9%. |
| Claude Platform docs, "Token counting" | https://platform.claude.com/docs/en/build-with-claude/token-counting | Token counts are estimates; the free count endpoint; newer tokenizer gives roughly 30 percent more tokens for the same text, so recount per model. |
| Anthropic, "Managing context on the Claude Developer Platform" (seen in search results, not opened) | https://www.anthropic.com/news/context-management | Optional "go further": memory tool plus context editing; do not cite its performance percentages without opening it first. |

Notes for the lesson writer: all URLs above were seen in search results or fetched this session. Anthropic documents are about Claude; the mission puts comparisons of companies out of scope, so frame them as one concrete implementation of ideas that apply to any model. Dollar figures and most token counts in the examples are invented for the arithmetic and must be labelled as made up.
