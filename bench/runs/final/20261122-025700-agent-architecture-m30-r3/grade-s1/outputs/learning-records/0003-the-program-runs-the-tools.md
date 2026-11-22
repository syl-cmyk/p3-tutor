# The model only asks for a tool; the program runs it (open misconception M4)

In quiz 0001 (submission s1), Riley believed the model runs tools itself: they said the model "runs the 3 tools itself" and answered 1 model call instead of 4, and picked the model opening the booking system on its own.
Riley does have the loop and the step limit, and knows tools are described to the model by name and description, but also thinks the model remembers earlier sessions on its own (M3).
Next lessons should make the split concrete: the model writes a request, the program runs it, and each result triggers a new model call; then show that memory between sessions only exists if the program puts it back into the input.

**Evidence:** quiz 0001, submission s1, items q2, q4 (M4) and q6 (M3); q1 and q3 correct.

**Implications:** Re-check M4 with a fresh quiz item before building on it; context and memory lessons depend on seeing that the model only knows what is in its current input.
