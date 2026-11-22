# Notes

## What the learner knows
- Performance: how to measure how fast a processor runs a program.
- Caches: why a processor keeps recently used data close by, and how an address is split into tag, index and offset.
- Pipelining overlaps instructions, so more instructions finish in the same time (taught in the last session).

## What the learner does not know yet
- Has not learned why a pipeline stalls, so cannot name the three kinds of hazards (structural, data and control), and tends to think a stall is always a data hazard.
- Has not learned how a pipeline handles a hazard, by stalling or bypassing.
- Tends to think pipelining makes every single instruction faster, instead of raising the total throughput.
- Asked whether an out-of-order processor with register renaming and speculation "avoids every stall" (false premise: it hides some stalls, never all). Told that renaming removes false (WAR/WAW) dependences, speculation hides control hazards only when the prediction is right, and true data dependences, cache misses and mispredictions still cost cycles. Hazards are still not taught: next lesson should be the three hazard types and stall counting in a simple in-order pipeline, before out-of-order.
