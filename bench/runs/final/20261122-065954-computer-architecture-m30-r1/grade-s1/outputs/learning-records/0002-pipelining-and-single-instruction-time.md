# Pipelining overlaps instructions, but the learner still thinks it speeds up one instruction

The learner explained that the total time shrinks because several instructions are in progress at once. They also chose "the time one instruction takes by itself" as what pipelining makes faster (M2), and counted 100 cycles for 100 instructions in a 4-stage pipeline, skipping the 4 cycles the first instruction needs (the answer is 103).

**Evidence:** quiz 0001, submission s1, items q1, q2 and q3.

**Implications:** Next, work on the difference between the time of one instruction and how many instructions finish in a given time, with a small cycle-by-cycle timeline. Do not start hazards until the 4 + (n - 1) count is solid.
