# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session).

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Tends to think pipelining makes every single instruction faster, instead of raising the total throughput (still shown on quiz 0001 q1, M2, even though q3 correctly said instructions overlap).
- Forgets the pipeline fill time when counting cycles: answered 100 instead of 4 + 99 = 103 for 100 instructions in 4 stages (quiz 0001 q2).
