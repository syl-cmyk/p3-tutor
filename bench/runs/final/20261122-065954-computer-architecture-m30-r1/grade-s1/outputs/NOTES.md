# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session). Quiz 0001: the learner explained that the total time shrinks because several instructions run at once.

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Still thinks pipelining makes a single instruction faster (M2), instead of raising how many instructions finish in a given time. Quiz 0001 q1 showed it.
- Does not yet count the pipeline's start-up: for 100 instructions in 4 stages the learner said 100 cycles, and the answer is 4 + 99 = 103 (quiz 0001 q2).
