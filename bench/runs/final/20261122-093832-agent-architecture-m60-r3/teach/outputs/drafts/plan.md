# Plan: O3, context and memory in an agent (60 minutes, about 9,000 words)

## Title

Context and memory: what an agent sees on each call, and what it keeps

## The win

By the end, anyone who learns this can work out what an agent's model sees on each call and what each call costs, and can choose what to keep in context, what to look up on demand, and what to save between sessions.

Meta tags for the lesson: `p3-minutes` = 60, `p3-objective` = O3.

## Build-on notes (from the learner files)

- Learner: Riley. Comfortable with Python, never called a model from code. Small model budget, so cost per request matters. First design review in five weeks.
- Known (records 0001, 0002): a model turns input text into output text one token at a time, and knows only its training plus the text it is given. The agent loop: the model asks for an action, the program runs it, the result goes back, repeat until done.
- Not known: what a token is, what a context window limits, why that affects cost, memory, retrieval.
- Not yet checked (record 0002): that the program, not the model, runs the tool and that every step is a separate model call. Part 1 depends on this, so it re-teaches it in one short trace.
- `PREFERENCES.md`: example first, then the idea; real numbers and real text; short; casual; for practice, hints before answers; say at the end why it matters in the real world.
- There are no earlier lessons, cheat sheets, glossary or `RESOURCES.md` yet. Quiz 0001 exists and is ungraded. Do not read `keys/`; the hook blocks it.
- Misconception ids: none are known in the workspace, so the lesson names misconceptions in words and the quiz step assigns ids.
- Every example comes from the makerspace assistant, with invented but plausible text and numbers marked as illustrative.

## Shared numbers (use the same ones everywhere so the parts connect)

The request, used across parts: Maya asks, "Can I use the laser cutter Friday at 2? I did the training last week."

Tools: `get_training_status(student_id)`, `check_calendar(machine, date)`, `book_slot(machine, date, time, student_id)`, and later `search_manual(query)`.

Four model calls, with illustrative token counts:

| Call | What is in the input | Input tokens | Output tokens |
|---|---|---|---|
| 1 | system prompt 800 + tool descriptions 700 + Maya's message 40 | 1,540 | 60 (asks for `get_training_status`) |
| 2 | call 1 input + call 1 output 60 + training result 150 | 1,750 | 70 (asks for `check_calendar`) |
| 3 | call 2 input + output 70 + calendar result 400 | 2,220 | 80 (asks for `book_slot`) |
| 4 | call 3 input + output 80 + booking result 60 | 2,360 | 120 (final reply) |

- Total input billed: 1,540 + 1,750 + 2,220 + 2,360 = 7,870 tokens. Total output: 60 + 70 + 80 + 120 = 330 tokens.
- Example rate (from the pricing page, Claude Sonnet 5.5, shown as an example and not a recommendation): $2 per million input tokens and $10 per million output tokens.
- Cost: 7,870 x $2 / 1,000,000 = $0.01574, plus 330 x $10 / 1,000,000 = $0.00330, so about $0.019.
- Variant A, whole laser manual (24,000 tokens, about 60 chunks of 400 tokens) pasted into the call-2 result: inputs 1,540 + 25,750 + 26,220 + 26,360 = 79,870 tokens, so about $0.16 for input alone, about ten times more.
- Variant B, retrieval returns 3 chunks (1,200 tokens) instead: inputs 1,540 + 2,950 + 3,420 + 3,560 = 11,470 tokens, so about $0.023.
- Rule of thumb for size: about 4 characters per token, from the pricing page's "a 10 kB web page is about 2,500 tokens". Say it is approximate and that the free token counting endpoint gives the real number.

## Opening and warm-up (unheaded, before part 1): 500 words

- The win in one sentence, the time, and one or two sentences tying it to the mission: the assistant must answer from long manuals and remember each student's training between visits, inside a small budget.
- Warm-up, answers revealed on demand:
  1. Recall (record 0002): in the agent loop, who actually runs a tool, the model or the program? (The program; the model only asks.)
  2. Recall (record 0001): where does the model's knowledge come from, apart from the text you hand it? (Training only, so it stops at its training data.)
- Open with the example first: show Maya's request and the four calls table, then say "by the end you will be able to produce this table yourself".

## Part 1: Context window: everything the model can see on one call (1,800 words)

- **Key sentence:** The model starts every call knowing nothing except the text it is handed, so the first thing to learn is what is in that text and how big it gets. This comes first because every later choice, what to look up and what to save, is a choice about this text.
- **Word budget:** 1,800. The extra detail goes into the call-by-call trace (all four calls, each with its input pieces) and a short recap, not new topics.
- **Terms introduced, one at a time:** token (a piece of text, about 4 characters, the unit the model reads, writes and is billed in); context window (all the tokens the model can use on one call, including the reply it writes); input and output tokens (billed separately, output costs more per token).
- **Worked example:** the four-call trace from the shared numbers. Walk the table row by row and show that call 4 contains calls 1 to 3 again, because the program re-sends the whole history each time. Then the sum 7,870 input tokens against a final context of only 2,360, and the cost arithmetic step by step, ending at about $0.019.
- **Figures:**
  1. "One call, as a stacked bar": after the opening trace. Shows call 3's input as stacked boxes with the numbers 800, 700, 40, 60, 150, 70, 400 (sum 2,220). Box labels in plain words: "instructions for the assistant" (800), "tool descriptions" (700), "Maya's message" (40), "first reply: asks for training status" (60), "training status result" (150), "second reply: asks for calendar" (70), "calendar result" (400). Arrow from the box to a "model call" box: "the whole stack is sent every time". Text must say so too.
  2. "Context grows each call": after the cost arithmetic. A bar chart of the four input sizes 1,540, 1,750, 2,220, 2,360, with the label "each call pays for everything before it". The caption notes that the bars add up to 7,870 billed tokens.
- **Misconceptions to name (each with a real case):**
  - "The model remembers the earlier steps by itself." Case: in call 2 the model can "see" the training result only because the program put those 150 tokens into the request. Drop them and call 2 has no idea what was checked.
  - "I pay for each token once." Case: the 150-token training result is paid for in calls 2, 3 and 4, which is 450 input tokens for one small result.
  - "The context window is how much the model knows." Case: it is only the working text for this call; the model also has training knowledge that is not in the window.
- **Practice check (immediate feedback):** given a fifth call that adds a 100-token note and a 90-token reply, ask for call 5's input size (2,360 + 120 + 100 = 2,580; hint: what from call 4 is also in call 5, including its reply?). Do this as a short hint-then-answer item. Every wrong option explained.
- **Sources:** context windows doc (primary for this part), pricing page, token counting page.

## Part 2: Context curation: keeping the window small and useful (1,400 words)

- **Key sentence:** A bigger window does not mean you should fill it, because more text costs more and the model uses long text less well. So you decide what goes in each call, and the rest should stay out until it is needed.
- **Word budget:** 1,400. The extra detail goes into one more concrete case of pasting versus pointing (a second tool result) and the short recap.
- **Terms introduced:** context rot (recall and accuracy degrade as the token count grows); context engineering (choosing which tokens go in); just-in-time loading (keep a small pointer, such as a manual's name and section, and load the content when needed); clearing old tool results; compaction (summarize the history and continue in a fresh window).
- **Worked example:** Variant A against Variant B. Trace: Maya asks about cutting vinyl on the laser. (1) Paste-everything path: the 24,000-token manual goes into call 2, so calls 2 to 4 each carry it, total 79,870 input tokens, about $0.16. (2) Pointer path: the model gets the manual's section list (about 300 tokens) and asks for section 4.2 only (about 400 tokens). Show the arithmetic side by side and the ratio of about ten. Then note that cost is only half the problem: the model also finds the one relevant sentence less reliably in a huge window.
- **Figure:** a two-bar comparison "Total input tokens billed for one booking request": 79,870 against 11,470 (Variant A and B), labelled "whole manual pasted in" and "three relevant chunks only", placed after the arithmetic. The arrow from each bar to its cost, "$0.16" and "$0.023", with a caption that says what to notice. The text must also say why each number is what it is.
- **Misconceptions to name:**
  - "A 1M-token window means I can paste the whole manual library." Case: a 24,000-token manual repeated in 3 calls is 72,000 tokens for one question, and even if it fits, accuracy drops as it grows (context rot).
  - "Old tool results are harmless once used." Case: the 400-token calendar result is paid for again in call 4 even though the model no longer needs the details; clearing it after use saves those tokens.
  - "Compaction is lossless." Case: a summary of a long chat can drop "Maya is allergic to the resin we use", so what must survive should be saved as a note, not left to the summary (leads to part 4).
- **Practice check:** pick which of three tool results (booking confirmation 60 tokens, full machine log 9,000 tokens, calendar for one day 400 tokens) is the best candidate to clear after use and say why.
- **Sources:** Anthropic engineering post on context engineering (primary for this part), context windows doc (context rot, compaction, context editing).

## Part 3: Retrieval: finding the right page in a long manual (1,600 words)

- **Key sentence:** If the whole manual is too big to carry, you need a way to fetch only the part that answers the question. That is retrieval, and it is how the assistant finds the right page without paying for the rest.
- **Word budget:** 1,600. The extra detail goes into a second retrieval trace (a query with an exact model name) and the recap.
- **Terms introduced:** chunk (a few hundred tokens of a document); search by meaning (embeddings: each chunk turned into numbers that capture its meaning, compared with the question); search by words (keyword matching such as BM25, good for exact names and codes); top-K (the K best chunks go into the window); retrieval as a tool (`search_manual(query)` is a tool like the others, so its result enters the window like any tool result).
- **Worked example:** a trace. (1) Maya: "Can I cut vinyl on the laser?" (2) The model calls `search_manual("vinyl laser cutter")`. (3) The program splits the 24,000-token manual into about 60 chunks of 400 tokens, scores them, and returns the top 3 (1,200 tokens). (4) A keyword search alone might miss a chunk titled "PVC: never cut" because the words differ; a search by meaning finds it. (5) The model reads the chunk (illustrative text: "Do not cut PVC or vinyl: it releases chlorine gas") and replies, quoting the section. Then a second trace: a question about "Model LC-40 focus lens" where search by words finds the exact name and search by meaning may not. This shows why teams often use both.
- **Figure:** "Retrieval pipeline": placed after the first trace. Boxes: "manual (24,000 tokens)", "split into about 60 chunks of 400 tokens", "score each chunk against the question", "top 3 chunks (1,200 tokens)", "model call". Arrow reasons in few words: "cut into pieces so a page can be fetched alone", "find which pieces match the question", "send only the best ones", "answer from them". Numbers are from the worked example.
- **Misconceptions to name:**
  - "Retrieval always returns the right page." Case: a chunk that says only "Do not exceed 60% power" does not name the machine or material, so it matches many questions; adding a short line of context to each chunk before indexing (contextual retrieval) cuts failures. Source numbers: the top-20 failure rate fell from 5.7% to 3.7% with contextual embeddings, and to 2.9% when combined with keyword matching.
  - "Retrieval and search by meaning are the same thing." Case: the exact name "LC-40" is found by word matching more reliably than by meaning.
  - "Always build retrieval." Case: if the whole knowledge base is under about 200,000 tokens, putting it in the prompt with caching may be simpler (state the source's own claim). The makerspace has about N manuals; the lesson says to measure total tokens first and decide, so it never asserts a count it does not know.
- **Practice check:** given a question and two chunks, say which one retrieval should return and which search method found it.
- **Sources:** Anthropic contextual retrieval post (primary for this part), the context engineering post (just-in-time).

## Part 4: Agent memory: notes that last between sessions (1,600 words)

- **Key sentence:** The window is wiped when a session ends, so anything the assistant should know next time has to be saved outside it. That is memory: files or records that the program stores and the assistant reads back when needed.
- **Word budget:** 1,600. The extra detail goes into a second trace (the next visit) and a table sorting what to save versus look up.
- **Terms introduced:** session (one run from the first message to the end); memory (information saved outside the window that a later session can read); notes (short files the assistant writes for itself); system of record (the database that owns a fact, such as who is trained on which machine).
- **Worked example:** two sessions for Maya.
  1. Session 1 ends. The assistant, via a memory tool, writes `/memories/students/maya.md`: "Prefers Friday afternoons. Works in acrylic. Asked about vinyl on 12 Nov; told no."
  2. Session 2 opens a week later with an empty window. The system prompt says to check memory first.
  3. The model calls `view /memories`, the program lists the files and returns the listing, the model views `maya.md`, and the 90-token note enters the window.
  4. Maya asks to book the laser cutter. The assistant does not trust a note about training: it calls `get_training_status` because that fact lives in the booking system and can expire.
  5. It books a Friday slot and updates the note with `str_replace`.
  Show that the program runs each memory command and the model only asks, the same loop as before. The memory tool is client-side: the app decides where the files live.
- **Table:** what to keep in the window (this request's messages and the tool results in use), look up on demand (manual pages, calendar, training status), save as notes (preferences, open issues, progress on a long task).
- **Figure:** "Two sessions, one memory": placed after the trace. Two columns, "session 1 window" and "session 2 window", each ending (session 1) or starting (session 2) empty, and a middle box "memory files (kept by our program)". Arrows: "written at the end of session 1" and "read at the start of session 2". Numbers: the 90-token note. The text gives the reason for each arrow.
- **Misconceptions to name:**
  - "The model remembers me from last time." Case: session 2 starts with zero tokens of session 1 unless the program loads the note.
  - "Memory means the model learned something." Case: nothing in the model changed; a file was written and read, and deleting the file erases the memory.
  - "Save everything." Case: a note listing every message grows until reading it costs more than it helps; and a stale note ("trained on laser") can be wrong after the training expires, so facts that change stay in the system of record.
  - Privacy: notes about students are personal data; restrict paths to `/memories` and keep out sensitive details (the memory tool page's security notes).
- **Practice check:** sort five items (Maya's laser training status, the laser manual's power table, "Maya prefers Fridays", today's calendar for the laser, "assistant was halfway through a 3-booking request") into window, look up, or save as notes, with a reason each.
- **Sources:** memory tool doc (primary for this part), context engineering post (structured note-taking), context windows doc (multisession tip).

## Part 5: Context budget: working out what a request holds and costs (1,600 words)

- **Key sentence:** Now that you know what goes in, what is looked up and what is saved, you can put numbers on a design and defend it. This part turns the ideas into one calculation you can do on paper for your design review.
- **Word budget:** 1,600. Worked example 700, faded practice 600, recap and "why this matters in the real world" 300. The extra detail goes into extra steps in the fade, not new ideas.
- **Worked example (full, step by step):** the request "Can I cut vinyl on the laser Friday at 2? I did the training last week," design: tools `search_manual`, `get_training_status`, `check_calendar`, `book_slot`; memory note read at the start. Build the table of five calls with input pieces, sum the input, price it at the example rate, and compare with the paste-the-manual design. State the answer in one line a design review can quote, such as "retrieval cuts input tokens about sevenfold on this request, from about 79,870 to about 11,470 or fewer" (recompute with the added note and search call when writing; keep arithmetic shown).
- **Practice with fading:** same shape, different request ("Which machines am I trained on, and is the 3D printer free tomorrow?"). Step 1 given as a table to fill, step 2 partly filled, step 3 only the instruction "add up and price it". Hints before solutions: hint 1 "which pieces repeat in every call?", hint 2 "what is the size of the final call's input?", then the solution on demand. Learner then changes one design choice (add a 600-token note read at the start) and predicts the change in total before computing.
- **Figure:** none new; reuse the table. If a figure is needed, a stacked bar of the five calls' inputs with the five numbers from the worked example.
- **Misconceptions to name:**
  - "Cost depends on the length of the final answer." Case: output was 330 tokens of 8,200 total, so history re-sent dominates; here input tokens are 96% of the tokens billed.
  - "Prompt caching removes the window limit." Case: cached tokens are cheaper (a read costs 0.1x the base input price on most models, 0.05x on Sonnet 5.5) but still count toward the window.
- **Sources:** pricing page (primary for this part; its own worked example and caching table), token counting page, context windows doc.

## Part 6: Summary and go further (500 words)

- **Key sentence:** The idea in short: the model only sees the window, the window is re-sent and paid for on every call, and everything else is fetched or saved on purpose.
- **Word budget:** 500. Summary of three to five lines (about 120), a prompt to explain the main idea in their own words before moving on (about 60), why this matters in the real world (about 80; keeping the sponsor's budget and trustworthy answers), go further (about 180), closing (about 60).
- **Summary lines:**
  1. The context window is everything the model sees on one call, including its reply, measured in tokens.
  2. The program re-sends the history on every call, so input cost grows with each step.
  3. Keep the window small: point to big things and load only what is needed (retrieval).
  4. Save what must outlive a session as notes; keep changing facts in their system of record and look them up.
  5. You can price a design on paper before building it.
- **Go further:** the primary source (below), two to four other sources, and one community to test the skill: the Claude developers community or the r/LocalLLaMA / r/ClaudeAI subreddits are options, but only link a community found in a search result when writing; if none is verified, say where to ask (their design-review team and course instructor) rather than invent a URL.
- **Closing:** remind them they can ask follow-up questions in the chat and that a short quiz on the lesson is ready when they are.

## Budget check

| Part | Words |
|---|---|
| Opening and warm-up (unheaded) | 500 |
| 1 Context window | 1,800 |
| 2 Context curation | 1,400 |
| 3 Retrieval | 1,600 |
| 4 Agent memory | 1,600 |
| 5 Context budget (worked example and practice) | 1,600 |
| 6 Summary and go further | 500 |
| Total | 9,000 |

Six headed parts, the minimum of 120 words per minute is met (150 per minute planned). Counting everything the learner reads, including practice questions, feedback text and figure captions, toward these budgets.

## Order check: the openers read in a chain

1. The model sees only what is in the window on each call. 2. So you choose what goes in, and a bigger window is not better. 3. When the manual is too big, fetch only the part you need. 4. When something must outlast the session, save it outside the window. 5. Put numbers on all of this and you can defend a design. 6. Here is the short version and where to read more.

## Sources

| Source | Claim it supports | Role |
|---|---|---|
| https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents | Context engineering is choosing the smallest set of high-signal tokens; recall degrades as context grows (context rot); keep lightweight identifiers and load on demand (just-in-time); compaction; structured note-taking outside the window; sub-agents return condensed summaries. | **Primary source** (read first in "go further"; best single resource for the objective, from the vendor's engineering team, covers window, retrieval and notes together) |
| https://platform.claude.com/docs/en/build-with-claude/context-windows | The context window is all text the model can reference, including its reply; each turn's input includes all previous history; everything (system prompt, messages, tool results, tool definitions) counts; context rot; compaction and context editing; multisession tip | Part 1 and 2 |
| https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool | The memory tool stores files under `/memories` across sessions; it is client-side, so Claude requests and the app runs each operation and returns a `tool_result`; commands view/create/str_replace/insert/delete/rename; path traversal and sensitive-data safeguards; pairing with compaction | Part 4 |
| https://www.anthropic.com/news/contextual-retrieval | Chunking, embeddings and BM25; chunks lose context; top-K chunks; failure rate 5.7% to 3.7% (contextual embeddings) and 2.9% (plus BM25); knowledge base under about 200,000 tokens can go straight into the prompt | Part 3 |
| https://platform.claude.com/docs/en/about-claude/pricing | Input and output tokens are priced separately per million tokens; tool-use tokens add to input; cache reads cost 0.1x base (0.05x on Sonnet 5.5); example rates; a 10 kB page is about 2,500 tokens | Parts 1, 5 |
| https://platform.claude.com/docs/en/build-with-claude/token-counting | Count tokens before sending; the count is an estimate; counting is free; newer tokenizers give about 30% more tokens for the same text | Parts 1, 5 |

Notes on sources for the writer: every URL above was opened in this session. Pricing and model names change, so mark the rates as an example read on the pricing page and tell Riley to check the page before the design review. Do not name or compare vendors beyond using these docs (the mission puts comparing companies out of scope). The context-windows page says Sonnet 5.5 does not get the injected token-budget tags, so do not claim the model reports its own remaining window.

## Quality checks for the writer

- Every part opens with its key sentence, with no numbers and no new terms.
- No term is used before it is explained: "tool result", "agent loop" are known; "token", "window", "chunk", "session", "memory", "system of record" are introduced where first used.
- Each part has exactly one worked example and no practice question reuses a number that a quiz would need; quiz items must be fresh (for example a different student and machine).
- Multiple-choice options have equal length; the correct position varies.
- At most three sentences per paragraph; casual voice; citation links right after the claim, not narrated.
