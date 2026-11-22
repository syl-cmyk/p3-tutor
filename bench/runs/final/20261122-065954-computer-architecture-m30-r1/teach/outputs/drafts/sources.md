# Sources checked for O2 (pipeline hazards)

All opened in this session. WebFetch could not extract text from the Utah PDF, so the downloaded PDF was read page by page (slides 1-20 seen as images).

## 1. Utah CS 3810 "Lecture 16: Pipeline Hazards" (guest lecture by Mahesh) - PRIMARY

Address: https://users.cs.utah.edu/~aburtsev/3810/lectures/lecture12-hazards/lecture12-hazards.pdf (opened, no redirect)

- Structural definition: SUPPORTED. Slide 6: "Multiple instructions contend for the same resource."
- Data definition: SUPPORTED. Slide 6: "A dependent instruction cannot proceed because it needs a value that hasn't been produced yet."
- Control definition: SUPPORTED. Slide 6: "The next instruction cannot be fetched because the outcome of an earlier branch is unknown."
- Unified memory as structural hazard, separate instruction and data memories as the fix: SUPPORTED. Slides 9-10: "Unified memory for instruction and data", then "Separate Instruction and Data Memories" (the clash is marked at CC 4 on lw's DM and the fetch of add).
- Register read and write in the same cycle solved by half-cycle access: PARTLY SUPPORTED. Slides 11-12 say only "Register file with shared read/write access port" and "Register access in half cycles" (clash marked at CC 5). They do not say "write in the first half, read in the second half"; that detail is the standard convention, so state it as the lesson's convention, not as the slide's words. Slide 12 also files this under structural hazards.
- 5-stage layout: PARTLY SUPPORTED. Slides 3 and 7 show a 5-stage pipeline with boxes IM, Reg, ALU, DM, Reg and stage names "Inst. Fetch, Inst. Decode, Execute, Memory, Write Back". The abbreviations IF/ID/EX/MEM/WB are not used on the slides.
- Also usable: slide 16 shows two nops between a producer and its immediate consumer (gap 0), consistent with the plan's 2 stalls when the half-cycle register access is used. Slide 4: "Branch target is known only at the end of its execution".
- Gives no cycle formula and no CPI figures.

May the writer cite it: yes, as the primary source for the three definitions, the unified-memory example and the half-cycle register access (worded as above).

## 2. Wikipedia, "Hazard (computer architecture)"

Address: https://en.wikipedia.org/wiki/Hazard_(computer_architecture) (opened, no redirect noted; the page is a general encyclopedia article, not a course text)

- Stall inserts bubbles (NOPs): SUPPORTED. "Bubbling the pipeline, also termed a pipeline break or pipeline stall, is a method to preclude data, structural, and branch hazards"; the control logic inserts NOPs; "All forms of stalling introduce a delay before the processor can resume execution."
- Read-after-write: SUPPORTED. The article's data-hazard discussion centres on RAW dependencies, with bubbles as a fix. It gives no standalone one-line definition of a data hazard.
- Structural hazard: SUPPORTED. Two or more instructions already in the pipeline need the same resource (its example is one ALU).
- Control hazard flushes wrongly fetched instructions: PARTLY SUPPORTED. It defines a control hazard as the logic incorrectly predicting the branch, so wrong instructions enter and are discarded (flush). It frames this around prediction. The plan's design has no prediction, so do not use Wikipedia for the "can't fetch until the branch resolves" definition; use Utah slide 6.
- Prediction limits bubbles: SUPPORTED. "a pipeline bubble will only be needed in the case of an incorrect prediction."
- Gives no cycle counts.

May the writer cite it: yes, as a secondary source for bubble/stall wording, RAW and structural hazards. Describe it only as a general encyclopedia article.

## 3. Cornell CS3410 slides and Crete HY425 lecture (listed in the plan as not opened)

Not opened in this session, so not kept. The writer must not cite or link them, not even under "Go further".

## Claims no source supports (the writer must leave out or word as the lesson's own advice)

- All cycle counts, the formula total = 4 + N + stalls, CPI figures, 25% load/store and 20% branch mixes, the gap table (2 / 1 / 0 stalls), the 2 ns / 2.2 ns timing example, the 7-stage branch penalty of 4: these are the lesson's own arithmetic under stated conventions. No page opened gives them.
- Branch resolved at end of EX with fetch simply stopping: the lesson's assumption. Utah slide 4 supports only "branch target is known only at the end of its execution". "Textbooks differ (ID costs 1, MEM costs 3)": not supported by anything opened; word as the lesson's own remark or drop it.
- "The deeper the pipeline, the later the branch resolves": not stated by either opened page; word as the lesson's own reasoning.
- "Write in first half, read in second half" as an exact wording: not on the slides (see above).
- H&P textbooks: not opened; do not cite.
