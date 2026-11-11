# Open misconception: the model runs the tools itself (M4), and remembers on its own (M3)

Quiz 0001 (s1) shows Riley knows what makes an agent, that a step limit is needed, and that the model picks tools from their descriptions.
Riley still believes the model runs the tools itself (M4), which makes the loop look like one model call, and that it remembers earlier sessions without being given them (M3).

**Evidence:** quiz 0001, submission s1: q2 (chose that the model opens the booking system), q4 (answered 1 call, "it runs the 3 tools itself"), q6 (said the model remembers past tool choices across sessions). Correct on q1 and q3; partial on q5 (omitted why the result goes back).

**Implications:** Before building on the loop, have Riley mark which steps are model and which are program. In the context and memory lesson, show that the model sees only what the program puts in its input, so cross-session memory has to be saved and re-sent by the program. Submission s2 is not yet graded and will show whether this has shifted.
