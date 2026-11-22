# Riley knows what makes an agent and what the model outputs, but two gaps remain

On the spaced-practice attempt (quiz 0001, s2), Riley correctly said the loop is what makes a system an agent, that the model outputs a tool request rather than running anything, and that the tool result goes back in as the model's next input.
Two gaps are still open: Riley believes the model runs the tools itself (M4, seen in q4's reasoning), and chose "let it run longer" over a step limit for a stuck agent (M6, q3).
Riley also said the model picks a tool "by the name", not from the tool descriptions it is given (q6).

**Evidence:** quiz 0001, submission s2, items q1, q2, q5 (correct), q3 (wrong, M6), q4 (partial, M4), q6 (partial).

**Implications:** Before building on tools in context and memory, revisit who does what in one loop turn: the model asks, the program runs. Teach tool descriptions and stopping conditions with a concrete run.
