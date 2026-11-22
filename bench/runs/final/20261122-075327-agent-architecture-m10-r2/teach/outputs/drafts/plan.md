# Plan: O3, context and memory in an agent

Objective O3: Explain context and memory in an agent: the context window, what is kept between steps and between sessions, and retrieval and notes as memory.
Requested length: 10 minutes. Total budget: 1,500 words (150 per minute; the floor is 1,200).
Meta tags for the lesson: `p3-minutes` = 10, `p3-objective` = O3.

## Title and win

**Title:** Context and memory: what an agent sees, keeps and looks up

**Win:** Anyone who learns this can take a piece of information an agent needs and decide whether it belongs in the context window, in saved notes between sessions, or in a store that is searched on demand.

**Tone:** Casual, example first and then the idea. Short paragraphs, three sentences at most. The learner is Riley. All numbers are illustrative unless a source is cited, and the lesson says so once.

**Builds on:** learning record 0001 (the model only knows its training plus the text it is given) and 0002 (the agent loop). No earlier lessons exist yet. The lesson introduces "token" in one plain sentence, because NOTES.md says Riley cannot yet say what it is.

## Budget table

| Piece | Words |
|---|---|
| Opening (win, why it matters for the makerspace assistant) and warm-up recall on the agent loop | 150 |
| 1. Context window: what the model can see on one call | 220 |
| 2. Message history: what is kept from one step to the next | 200 |
| 3. Context limits: what to do when the window fills up | 190 |
| 4. Memory notes: what is kept between sessions | 220 |
| 5. Retrieval: finding the right page in a long manual | 220 |
| 6. Putting it together: worked example, faded practice, summary and sources | 300 |
| **Total** | **1,500** |

Where extra detail goes: more lines in each part's numbered trace and one extra number in each figure caption. Never a new topic. Part 6 holds the recap.

## Opening (unheaded, 150 words)

- Win sentence, then one line tying it to the mission: the assistant must answer from long manuals and remember each student's training status between visits.
- Warm-up recall, answer on demand: "In the agent loop, who runs the tool, the model or the program?" (the program, from record 0002).
- Define token in one sentence: a small chunk of text, roughly three-quarters of a word. This is the unit the window is counted in.

## Part 1. Context window: what the model can see on one call (220 words)

**Key sentence:** The model can only use the text it is handed on each call, and that text has a size limit. So every call, someone is choosing what goes in.

**Worked example (trace):**
1. User says: "How thick can the laser cutter cut acrylic?"
2. The program builds the context for call 1: system prompt 800 tokens, three tool descriptions 600 tokens, the question 18 tokens. That is 1,418 tokens.
3. The model picks the tool `search_manual("laser cutter acrylic max thickness")`, about 30 tokens.
4. The program runs it. What comes back is one manual passage of 350 tokens: "Acrylic: up to 10 mm at 60 W."
5. Call 2 sees all of the above plus the passage, 1,798 tokens. The reply is: "Up to 10 mm. Thicker sheets need the other cutter."

**Idea after the example:** the context window is everything the model sees on one call, and its size is counted in tokens. Say that the window has a ceiling, and that the model's accuracy at recalling the contents drops as it fills ("context rot", cited from the primary source).

**Figure 1:** A horizontal stacked bar for call 2, 1,798 tokens in total. Segments, in order: "Instructions (system prompt)" 800, "Tool descriptions" 600, "Student's question" 18, "Tool call" 30, "Manual passage that came back" 350. A dashed line at the right edge is labelled "Window limit". Placed after the trace. The arrow reasons: "program adds the result" from the passage segment back to the bar.

**Misconception:** "The model looks things up in the manuals by itself." Real case: in the trace, the 10 mm figure reached the model only because the tool result was added to the window. Without the search call, the model would guess from training, as in record 0001.

## Part 2. Message history: what is kept from one step to the next (200 words)

**Key sentence:** Between steps, the model keeps nothing on its own. The program sends the whole conversation again each time, so the window only ever grows.

**Worked example (trace):** the request "Book the laser cutter for me on Friday afternoon."
1. Call 1 input: 1,418 tokens. The model picks `get_calendar(laser_cutter, 2026-11-27)`.
2. Result: free 10:00 to 12:00 and 14:00 to 15:00, 120 tokens.
3. Call 2 input: 1,418 + 30 + 120 = 1,568 tokens. The model picks `book_slot(laser_cutter, 2026-11-27 14:00, 1 h)`.
4. Result: "Confirmed, booking #4412", 40 tokens.
5. Call 3 input: 1,568 + 30 + 40 = 1,638 tokens. Reply: "You're booked Friday 14:00 to 15:00, booking #4412."
6. Total input tokens read across the three calls: 1,418 + 1,568 + 1,638 = 4,624. This is why cost grows faster than the length of the conversation, and why it matters on a small budget.

**Idea:** each step is a separate call (this was left unchecked in record 0002). "Memory" inside a conversation is the program re-sending the history.

**Figure 2:** Three horizontal bars stacked vertically, one per call, with lengths 1,418, 1,568 and 1,638. Labels: "Call 1: question", "Call 2: + calendar result", "Call 3: + booking result". An arrow between bars is labelled "everything re-sent, plus the new result". Placed after the trace.

**Misconception:** "The model remembers step 1 because it was just there." Real case: if the program forgot to re-send the calendar result, call 3 could not book the 14:00 slot. The model would see only the question, with no slot to book.

## Part 3. Context limits: what to do when the window fills up (190 words)

**Key sentence:** A long session fills the window with old results the model no longer needs. So you trim or summarize them, rather than count on a bigger window.

**Worked example (trace):** a staff member checks 20 machines in one session.
1. Each calendar result is 2,000 tokens. After 20 checks, the history holds 40,000 tokens of old calendars, and the one booking that matters is buried in them.
2. Fix A, clear old tool results: the program drops the 20 calendars and keeps a one-line record for each: "get_calendar(laser_cutter) was called". The history falls to about 1,000 tokens of those records. The calendars can be fetched again if needed.
3. Fix B, compaction: the program asks the model to write a 300-token summary ("Booked #4412, laser cutter Fri 14:00; 3D printer is full until Monday") and starts a fresh window from the summary.
4. The next call sees about 2,300 tokens instead of 42,000.

**Idea:** the aim is the smallest set of useful tokens, not the largest window. Both fixes are named in the primary source (tool-result clearing as the lightest form of compaction).

**Figure 3 (optional):** two bars, "Before: 40,000 tokens of old calendars" against "After clearing: about 1,000 tokens of one-line records". The arrow reason is "old results dropped, calls kept".

**Misconception:** "A bigger window fixes it." Real case: the primary source says larger windows do not remove the clutter or relevance problem. Forty thousand tokens of old calendars bury the one booking whatever the window size, and every call still re-reads them (Part 2's cost).

## Part 4. Memory notes: what is kept between sessions (220 words)

**Key sentence:** When a session ends, the window is gone. Anything the assistant should know next time has to be written down outside it, as notes the program stores.

**Worked example (trace):**
1. Monday. Dana says: "I just passed the laser cutter safety training." The model picks `memory create /memories/students/dana.md` with the text "Laser cutter: trained 2026-11-23. 3D printer: not trained."
2. The program writes the file and returns "File created successfully". Reply: "Noted, you're cleared for the laser cutter."
3. The session ends. The window is thrown away.
4. Thursday. A new session starts with an empty history. Dana says: "Can I book the 3D printer?"
5. The model first picks `memory view /memories/students/dana.md`. What comes back is the two lines above, about 25 tokens.
6. Reply: "Not yet. You need the 3D printer training first. The laser cutter is fine."

**Idea:** the memory tool is files. The model asks to view, create or edit a file, and the program does it, so the notes live in storage the team controls (the memory tool docs). This also settles privacy: one file per student, with the path checked so one student's session cannot read another's.

**Figure 4:** Two boxes, "Monday session" and "Thursday session", with a box between them, "Notes file (stored by the program)". Arrow 1, Monday to file: "model asks to write". Arrow 2, file to Thursday: "model asks to read at the start". A label under each session: "window cleared at the end".

**Misconception:** "The model remembers students from earlier chats." Real case: without the notes file, Thursday's session cannot know about Dana's training and would have to ask again. Only what was written down survives.

## Part 5. Retrieval: finding the right page in a long manual (220 words)

**Key sentence:** Some knowledge is too big for the window and too big to write as notes. So the assistant searches it and pulls in only the few passages that fit the question.

**Worked example (trace):**
1. The assistant has 12 manuals of about 120 pages each, 1,440 pages. At roughly 400 tokens per page, that is about 576,000 tokens. The source says a knowledge base under about 200,000 tokens (about 500 pages) can simply go into the prompt, and this one is nearly three times that. One manual alone, about 48,000 tokens, could be pasted.
2. User says: "How do I change the nozzle on the 3D printer?"
3. The model picks `search_manuals("3D printer change nozzle")`.
4. The program has split the manuals into chunks ahead of time. It returns the top 3 chunks, about 300 tokens each, 900 in all.
5. Reply: "Heat the hotend to 200 C, then unscrew the nozzle. See the 3D printer manual, page 41."

**The catch, with a small example:** the chunk "Heat to 200 C, then unscrew" does not say which machine it is from, so a search can miss it. The fix is to add a line of context to each chunk before indexing it: "From the 3D printer manual, chapter Changing the nozzle." The source reports that retrieval failures fell from 5.7% to 2.9% with this fix plus keyword search.

**Idea:** this is just-in-time retrieval. The assistant keeps a light pointer, a search or a file path, and loads the content only when it is needed. A search tool is described and called like any other tool.

**Figure 5 (optional, only if space):** a four-box vertical flow: "12 manuals (about 576,000 tokens)", then "Chunks with a context line added", then "Search returns top 3 (900 tokens)", then "Model's window". The arrow reasons: "split ahead of time", "match the question", "add only these".

**Misconception:** "Retrieval is always better than pasting the text in." Real case: one 48,000-token manual fits in the window, so a search could only add a way to miss the right page. Retrieval pays off at 576,000 tokens.

## Part 6. Putting it together: where does each thing live? (300 words)

**Key sentence:** Now you can ask the same question about every piece of information the assistant needs: how long it matters, and how big it is.

**Compact comparison table (about 60 words):**

| | Context window | Notes between sessions | Retrieval |
|---|---|---|---|
| Holds | this session's conversation | small facts about one student | big documents |
| Lives for | one session | until deleted | permanently, re-indexed on change |
| Example | today's booking #4412 | "Dana: laser trained" | the 3D printer manual |

**Worked example (about 90 words):** place "the laser cutter's weekend hours".
1. Is it needed in every session? Yes.
2. Is it small? Yes, 30 tokens.
3. Place it in the system prompt, which is part of the window. It needs no search and no notes.

**Practice with the steps faded (about 90 words):** place three items.
- Item 1 is fully worked: "Marcus wants the vinyl cutter but is not trained", which goes in notes.
- Item 2 is partly worked: "page 87 of the CNC router manual", and the learner fills in the last step.
- Item 3 is blank: "the calendar result from 10 minutes ago", and the learner does all the steps.
- Hint first ("Ask: does it still matter next week? How big is it?"), solution on demand.
- Answers: item 2 is retrieval, because it is big and needed only for some questions. Item 3 is the window now, and clear it later if the history grows (Part 3).

**Summary (3 to 5 lines, about 50 words):**
- The window is all the model sees on one call, measured in tokens.
- The program re-sends the history each step, so the window and the cost grow.
- Trim or summarize old results instead of waiting for a bigger window.
- Notes carry small facts between sessions. Retrieval brings big documents in on demand.
- Prompt: "Explain in your own words where Dana's training status lives, and why."

Why it matters in the real world (one sentence): each choice here sets the cost per request and how often the assistant is wrong, which is what the design review will ask about.

Then "Go further": primary source, other sources, and a closing line saying the learner can ask follow-up questions in chat and that a quiz is ready.

## Sources

1. **PRIMARY.** Anthropic Engineering, "Effective context engineering for AI agents": https://anthropic.com/engineering/effective-context-engineering-for-ai-agents. Opened in this session. Supports: the definition of context and its finite attention budget; context rot (recall falls as tokens grow); larger windows do not remove the clutter problem; just-in-time retrieval with lightweight identifiers; compaction; clearing old tool results as a light form of compaction; structured note-taking kept outside the window and read back after resets.
2. Claude Docs, "Memory tool": https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool. Opened in this session. Supports: memory is a directory of files persisting across conversations; it is client-side, so Claude requests operations and the application runs them; the `view` and `create` commands and the `/memories` path; the tool is checked first thing in a session; path validation for security; the tool-use loop is standard.
3. Anthropic Engineering, "Introducing Contextual Retrieval": https://www.anthropic.com/engineering/contextual-retrieval. Opened in this session. Supports: chunks lose context and so get missed; adding explanatory context to each chunk; a knowledge base under about 200,000 tokens (about 500 pages) can go straight into the prompt; failure rate 5.7% to 3.7% (embeddings), 2.9% (plus keyword search), 1.9% (plus reranking).
4. Anthropic, "Managing context on the Claude Developer Platform" (the context management announcement): https://www.anthropic.com/news/context-management. Seen in a search result and not opened. Use it only as a "further reading" link for context editing and the memory tool.
5. Claude Docs, "Context editing": https://platform.claude.com/docs/en/build-with-claude/context-editing. The link appeared in the opened memory tool page and the page itself was not opened. Supports only "clearing old tool results" as a named feature, so cite it as a further-reading link.

Not used for facts: third-party blog summaries that appeared in the search results.

## Notes for the lesson writer

- The 400 tokens per page figure is derived from the source's 200,000 tokens, about 500 pages. Say it is a rough rule.
- Every token count in the traces is illustrative, and the lesson should say so once. Real counts depend on the model's tokenizer.
- Dates: Friday is 2026-11-27 (today is Sunday 2026-11-22). Dana's training date of 2026-11-23 is Monday, tomorrow, so use "Monday" in the text and avoid the date, or move it to a past date.
- Do not mention specific machine brands. Do not compare vendors (out of scope in MISSION.md).
- Practice questions here are not quiz items, so the quiz must use different cases.
- Add a cost-per-request line that uses the 4,624 total. Do not quote any prices.
