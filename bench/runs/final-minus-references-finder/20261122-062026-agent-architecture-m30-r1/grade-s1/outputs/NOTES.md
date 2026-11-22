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

- Can pick a stopping safeguard (a step limit) for a looping agent, and knows a model picks a tool from the names and descriptions it is given (quiz 0001, s1).

## Open misconceptions
- M4: believes the model runs the tools itself; in fact it only writes a request and the program runs the tool. Led to "1 model call" for a three-tool run (quiz 0001 s1, q2 and q4; learning record 0003).
- M3: believes the model remembers earlier choices or conversations across sessions on its own (quiz 0001 s1, q6).
- Partial on why the program feeds a tool result back into the model's next input (q5).

## Working notes
- Quiz 0001 (the agent loop and tool calling) was taken twice: `submissions/s1.json` on the day of the agent-loop session, and `submissions/s2.json` four days later, from memory, as spaced practice.
  s1 is graded (`grades/0001-s1.json`: 2 correct, 2 partial, 2 wrong); s2 is not graded yet.
- Next in the mission is context and memory, because the makerspace assistant has to answer from long machine manuals and remember each student's training status between visits.
