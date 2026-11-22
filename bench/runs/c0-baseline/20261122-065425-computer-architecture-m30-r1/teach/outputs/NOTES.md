# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session).

## Working notes
- Lesson 0001 (O2, 30 min) and quiz 0002 written. Not yet taken; the learner has not shown understanding of O2.
- Misconception ids: M2 = pipelining makes one instruction faster (from key 0001); M3 = every stall is a data hazard (used in key 0002).
- Lesson convention: 5-stage pipeline, register file writes first half and reads second half, so a dependent neighbour costs 2 stalls without forwarding; taken branch costs 2.
- Next: how hazards are handled (forwarding, load-use, branch prediction), then stage count versus stall cost (mission).

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Tends to think pipelining makes every single instruction faster, instead of raising the total throughput.
