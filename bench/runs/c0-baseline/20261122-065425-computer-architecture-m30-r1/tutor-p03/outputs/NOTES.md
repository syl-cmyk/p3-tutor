# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session).

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Asked (2026-11-21) whether overlapping instructions in a pipeline means one never has to wait: believes pipelines never stall. Corrected in chat (a later instruction can need a result an earlier one hasn't produced yet); not yet shown the correction landed. Follow up with a short check, then teach hazards.
- Tends to think pipelining makes every single instruction faster, instead of raising the total throughput.
