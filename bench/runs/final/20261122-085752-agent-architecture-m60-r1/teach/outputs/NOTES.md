# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

## What Riley does not know yet
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  Neither attempt has been graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
- Taught O3 (context and memory) as a 60-minute lesson, `lessons/0001-context-and-memory.html`, with quiz 0002 ready and not yet taken.
  It defines token, context window, message history, context rot, clearing, compaction, retrieval, BM25, embeddings, top-k, notes and lookups; nothing in it has been checked with the learner yet, so no learning record exists for O3.
- The lesson's numbers (800-token instructions, 60,000-token manual, $2 and $10 per million tokens) are made up for illustration, and the lesson says so; the real price must come from the pricing page.
- Design rule taught: training status and bookings come from a lookup, not a note, because they change and gate safety. Watch whether Riley keeps this when quizzed.
- No verified community for agent builders has been found yet (see `RESOURCES.md` Gaps).
- Next after O3: workflows versus agents, then multi-agent splits.
