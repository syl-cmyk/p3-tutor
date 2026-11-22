# Notes

## What Riley knows
- Python from classes: functions, lists and dicts, reading JSON, and calling a web API in one class project.
- Has used a chatbot for homework help and report drafts, and has noticed that it can state an outdated fact with confidence.
- A language model takes text in and writes text out, one token at a time, from patterns learned in training (learning record 0001).
- The agent loop at a high level: the model asks for an action, the action is carried out, the result comes back, and this repeats until it is done (learning record 0002).

- Quiz 0001, submission s1: understands that an agent is a loop (q1), that a step limit stops a stuck loop (q3), and that the model picks a tool from names and descriptions (q6, first half).

## What Riley does not know yet
- M4 (open): thinks the model runs the tools itself; the model only writes a request and the program runs the tool, with one model call per step (q2, q4 in s1; learning record 0003).
- M3 (open): thinks the model remembers earlier sessions' tool choices on its own (q6 in s1).
- Does not yet say why the result goes back to the model (q5 in s1).
- Has never called a language model from code or written a tool definition.
- Has heard the words "token" and "context window" but cannot say what they limit or why they affect cost.
- Has not met memory, retrieval, workflows versus agents, or multi-agent systems.
- Has no machine-learning background beyond one statistics course.

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  s1 is graded (`grades/0001-s1.json`: 2 correct, 2 partial, 2 wrong); s2 has not been graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
