# Open: the program runs tools (M4), and a loop needs a stopping condition (M6)

In quiz 0001 (submission s2, spaced practice), Riley got the loop right (q1, q5) and knew the model outputs a tool request (q2). Two gaps remain: Riley wrote that the model "runs" the tools while counting model calls (M4, q4), and thought a stuck agent would eventually succeed if left running, instead of needing a step limit (M6, q3). Riley also chose tools by name only, not by description (q6).

**Evidence:** quiz 0001, submission s2, items q3, q4, q6.

**Implications:** Before building on context and memory, revisit who does what in one loop step, and tie stopping conditions to the budget. The q6 gap leads into writing tool descriptions.
