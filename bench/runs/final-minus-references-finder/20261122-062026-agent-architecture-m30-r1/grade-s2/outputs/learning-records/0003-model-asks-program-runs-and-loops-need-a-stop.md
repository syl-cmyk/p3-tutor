# The model only asks for a tool; the program runs it (M4 still open), and a loop needs a stop (M6)

On the spaced re-take of quiz 0001, Riley correctly said the model outputs only a request naming the tool and its arguments, and that the program feeds each result back as the next input. Still open: in the q4 explanation Riley wrote that the model "runs" each tool (M4), and Riley chose "left to run longer, it will eventually fix the bug" for a stuck loop (M6), so a step limit as a safeguard is not yet understood. Also, Riley thinks a tool is chosen from its name alone, not from its description and parameters.

**Evidence:** quiz 0001, submission s2, items q2, q5 (correct) and q3, q4, q6 (not fully right).

**Implications:** Before building on context and memory, revisit who does what in one loop step and why every loop needs a stopping condition.
