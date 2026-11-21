# Open: the model requests tools but Riley still says it runs them; loops need a stop rule

Quiz 0001 (submission s2) shows Riley knows what the model outputs for a tool call and how results feed back into the next input. Two ideas are still shaky: Riley's reasoning on q4 still says the model runs the tools itself (M4), and on q3 Riley chose to let a stuck agent run longer (M6) instead of adding a step limit.

**Evidence:** quiz 0001, submission s2, items q3, q4 and q6 (q6 gave only the tool's name, not its description).

**Implications:** Before building on tools, revisit who runs a tool (the program) and why every loop needs a stopping condition. Memory and context lessons can proceed alongside this.
