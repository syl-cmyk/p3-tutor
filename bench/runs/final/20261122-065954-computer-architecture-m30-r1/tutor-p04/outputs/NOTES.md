# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session).

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Tends to think pipelining makes every single instruction faster, instead of raising the total throughput.
- Asked how out-of-order + register renaming + speculation "avoids every stall" (false premise: they reduce stalls, never remove all). Curious about advanced CPUs before learning hazards; steer back to hazards and stall-cycle counting first.
