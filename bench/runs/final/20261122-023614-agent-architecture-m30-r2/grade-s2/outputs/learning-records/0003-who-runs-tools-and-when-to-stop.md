# Riley knows what makes an agent and what the model outputs, but not who runs tools or why loops need a limit

On quiz 0001 (spaced retake, s2) Riley correctly said an agent is a loop, that the model outputs a tool request and not the result, and that the result goes back as the next input. Two gaps remain: Riley still writes that the model runs the tools (M4), and thinks a stuck agent left running longer will eventually succeed (M6). Riley also says the model picks a tool "by the name" and does not yet mention the tool description.

**Evidence:** quiz 0001, submission s2, items q1, q2, q5 (correct), q3 (wrong, M6), q4 (partial, M4), q6 (partial).

**Implications:** Before context and memory, revisit who runs each step (model requests, program runs) and why a loop needs a step limit. Introduce tool descriptions as what the model reads.
