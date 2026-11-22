# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session).

## Working notes
- Lesson 0001 (pipeline hazards, objective O2) and quiz 0002 are ready; not yet taken, so nothing about hazards is shown as known yet.
- The lesson's conventions: 5 stages, half-cycle register access, no bypassing, branch decided at end of EX (2 stalls).
- Next likely topic: how a pipeline handles a hazard (bypassing), and branch prediction.

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Tends to think pipelining makes every single instruction faster, instead of raising the total throughput.
