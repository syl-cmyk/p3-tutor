# Riley thinks the model runs its own tools (M4), and that it remembers across sessions (M3)

In quiz 0001 (s1) Riley got the loop (q1) and the step-limit safeguard (q3) right, but believed the model itself opens the booking system (q2) and runs the three tools itself, so counted 1 model call instead of 4 (q4). Riley also added that the model remembers its past tool picks across sessions (q6).
Next lessons should show that the model only writes a request, the program runs the tool, and each step is a separate model call with a fresh input; this also sets up context and memory.

**Evidence:** quiz 0001, submission s1, items q2, q4, q6. Spaced retake s2 is not graded yet.

**Implications:** Do not treat the agent-loop record (0002) as fully secure: the loop is understood at a high level, but who does what is not.
