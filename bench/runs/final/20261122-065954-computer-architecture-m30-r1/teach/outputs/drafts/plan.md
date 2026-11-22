# Lesson plan: O2

**Objective O2:** Explain why a pipeline stalls: a hazard, which is structural, data or control.
**Length:** 30 minutes, 4,500 words (150 per minute). Meta tags: `p3-minutes` = 30, `p3-objective` = O2.

**Title:** Pipeline hazards: why a pipeline stalls and what each stall costs

**The win:** Anyone who learns this can look at a short run of instructions in a 5-stage pipeline, say which kind of hazard (structural, data or control) holds each one up, and count the cycles lost.

## Conventions used by every trace (state them once, in part 1, then reuse)

- Five stages: IF (fetch), ID (decode and read registers), EX (execute), MEM (data memory), WB (write the result back). One stage per cycle, so a lone instruction takes 5 cycles.
- Registers: a write in WB happens in the first half of the cycle and a read in ID in the second half, so an instruction can read in the same cycle the earlier one writes (the classic textbook design; Utah slides 11-12 show the half-cycle register access).
- No bypassing (a later objective). Stalls here are plain waiting, so a stall's cost is easy to count.
- Instruction memory and data memory are separate, except in part 3 where they are shared.
- Branch resolved at the end of EX; the machine simply stops fetching after a branch until it resolves (no prediction; that is later). This is a stated assumption: textbooks differ (resolving in ID costs 1, in MEM costs 3).
- Cycle formula, introduced in part 2: total cycles = 4 + N + stalls, for N instructions (4 is the fill time). CPI = total cycles / N.

## Part 1: Pipeline timing: one instruction is not faster, many finish sooner

**Key sentence:** Before we can see what goes wrong, we need to see what a smooth pipeline looks like on the clock. And it shows that pipelining never made a single instruction quicker.

**Word budget:** 700 (opening and win 120, warm-up 100, example and trace 330, misconception 100, check 50). Extra detail goes in more trace rows (the 5-instruction diagram shown fully) and one recap line.

**Warm-up (recall, answers on demand):** (1) Pipelining overlaps instructions: what does that raise? (throughput). (2) A cache miss makes an access wait: what had to happen to the address to find the miss? (tag differs at the same index). Ties to learning record 0001; keep to two lines.

**Worked example (numbers):** Each stage takes 2 ns. Unpipelined machine: 10 ns per instruction. Pipelined, with 0.2 ns of register overhead per stage, the clock is 2.2 ns. Trace: instruction 1 IF in cycle 1 ... WB in cycle 5; instruction 5 IF cycle 5, WB cycle 9; 5 instructions take 9 cycles = 19.8 ns vs 50 ns unpipelined. One instruction alone takes 5 x 2.2 = 11 ns, slower than 10 ns. Then 1,000 instructions: pipelined (4 + 1000) x 2.2 = 2,208.8 ns vs unpipelined 10,000 ns.

**Figure 1 (after the trace):** Cycle chart, rows I1..I5, columns cycles 1-9, each cell labelled IF/ID/EX/MEM/WB, the diagonal staircase. Labels: "instruction 1" to "instruction 5", "cycle 1" to "cycle 9". No arrows; a bracket under cycles 1-4 labelled "pipeline filling" (reason: the first result needs 5 cycles); a bracket at cycle 9 labelled "last instruction finishes". Caption: one finishes per cycle from cycle 5 on.

**Misconception named (M-latency):** "Pipelining makes each instruction faster." Counter: one instruction takes 11 ns pipelined vs 10 ns unpipelined; the win is 1,000 instructions in 2,208.8 ns instead of 10,000 ns.

## Part 2: Stall and bubble: a cycle where the pipeline waits, and what it costs

**Key sentence:** Sometimes an instruction can't move on when the clock ticks, so the pipeline waits. That wait is the thing we count, and every wait has a cause.

**Word budget:** 750 (recap 50, example 300, formula walk 200, misconceptions 120, check 80). Extra detail: a second, bigger count (100 instructions, 20 stalls) as one more case of the same formula.

**Worked example:** 5 instructions where instruction 3 waits one cycle in ID. Trace: I3 ID in cycle 4 and again cycle 5 (the repeat is the stall), so everything behind it slips one cycle; the empty slot moving down the pipeline is the bubble (the stage sits idle for a cycle). Total = 4 + 5 + 1 = 10 cycles, CPI = 10/5 = 2.0 for this tiny run. Bigger case: 100 instructions, 20 stall cycles: 4 + 100 + 20 = 124 cycles, CPI 1.24. Ideal: 104 cycles, so stalls cost about 19% extra time.

**Figure 2 (after the 5-instruction trace):** Same chart as figure 1 but with I3's ID cell repeated in cycle 5 (shaded, labelled "stall: waits one cycle") and a shaded empty cell in the EX column at cycle 5 labelled "bubble: stage does nothing". Arrows: from I3's first ID to second ID "could not proceed" (reason: it was not ready); from the stall to I4 and I5 shifted right "everything behind waits too" (reason: they can't overtake). Caption: one stall shifts the whole tail by one cycle.

**Misconceptions:** (a) "A stall means the program got stuck or wrong." Counter: the result is still right, only 1 cycle later (10 vs 9). (b) "Every stall is a data hazard." Set up now, resolved in parts 3-5: there are exactly three causes; the next three parts show one each, each with its own number.

## Part 3: Structural hazard: two instructions need the same hardware in the same cycle

**Key sentence:** The simplest cause of a stall is two instructions wanting one piece of hardware at the same moment. Nothing about the values matters here, only the hardware.

**Word budget:** 750 (example 330, idea 120, fix and why it matters 120, misconception 100, check 80). Extra detail: a second concrete case, a register file with one port, in two lines.

**Worked example:** One memory shared for instructions and data. Sequence: `lw r1,0(r2)`, `add r3,r4,r5`, `sub r6,r7,r8`, `or r9,r10,r11`. Trace: lw IF1 ID2 EX3 MEM4 WB5; add IF2...; sub IF3...; `or` wants IF in cycle 4, but lw is using memory in MEM in cycle 4, so `or` fetches in cycle 5 (1 stall). Total = 4 + 4 + 1 = 9 cycles instead of 8. The registers hold unrelated values: no data is shared, so it is not a data hazard. Real case: every load or store collides with a fetch, so a program with 25% loads and stores loses about 0.25 cycles per instruction, CPI about 1.25. Fix: separate instruction and data memories, then the same 4 instructions take 8 cycles.

**Figure 3 (after the trace):** Cycle chart of the 4 instructions, cycles 1-9. In cycle 4 draw a box around lw's MEM and `or`'s attempted IF, labelled "both want the one memory". `or` IF moved to cycle 5, labelled "waits 1 cycle". Arrow from the clash to the waiting cell: "memory is busy, so fetch waits". Caption: no register is shared by these instructions.

**Misconception:** "Every stall is a data hazard." Counter: here r1, r3, r6, r9 are all different registers and it still stalls, 9 cycles vs 8.

## Part 4: Data hazard: an instruction needs a value an earlier one has not written yet

**Key sentence:** The next cause is about values: an instruction has to wait for a result that an earlier instruction hasn't stored yet. The hardware is free, but the answer isn't ready.

**Word budget:** 850 (example 400, idea 120, load vs ALU case 100, misconceptions 120, check 110). Extra detail: a longer trace including the third instruction that also uses r1, to show the stall slides back, and a recap line.

**Worked example (no bypassing):** `add r1,r2,r3`, `sub r4,r1,r5`, `or r6,r1,r7`. Trace: add IF1 ID2 EX3 MEM4 WB5 (r1 written in cycle 5). sub IF2, wants ID in cycle 3 but r1 isn't written until cycle 5, so it repeats ID in cycles 3, 4, then reads in cycle 5: 2 stalls, EX6 MEM7 WB8. `or` is held behind it: IF in cycles 3-5, ID6 EX7 MEM8 WB9. Total = 4 + 3 + 2 = 9 cycles; `or` itself never waited on r1 (already written), it only waited on sub. A gap of one instruction between producer and consumer would cost 1 stall; two, 0 (list as a small table: gap 0 = 2 stalls, gap 1 = 1 stall, gap 2 or more = 0). Say that the later lesson on bypassing shrinks these numbers; do not teach it here.

**Figure 4 (after the trace):** Cycle chart of add, sub, or. add's WB cell (cycle 5) highlighted "r1 written here". sub's ID cells in cycles 3, 4 shaded "waiting", cycle 5 labelled "reads r1". Arrow from add's WB to sub's final ID: "the value is ready only now". Caption: the arrow runs from where the value is written to where it is needed.

**Misconceptions:** (a) "Instructions only conflict if they are next to each other in the program." Counter: gap table; with gap 2 there is no stall. (b) "Any two instructions using the same register stall." Counter: `sub r4,r1,r5` then `or r6,r1,r7` both only read r1, no stall between them from r1 (the dependence is write then read).

## Part 5: Control hazard: the pipeline does not know which instruction comes next

**Key sentence:** The last cause is about not knowing where to fetch from. After a branch, the machine can't tell which instruction follows until the branch is worked out.

**Word budget:** 800 (example 350, idea 120, loop cost 150, misconceptions 100, check 80). Extra detail: the loop cost with 10 iterations as a second concrete case.

**Worked example (stop fetching after every branch):** `beq r1,r2,L`, then the instruction at L. Trace: beq IF1 ID2 EX3 (the outcome is known at the end of cycle 3), so the next fetch can't start until cycle 4: cycles 2 and 3 fetch nothing useful, 2 stalls. Loop: 5 instructions per iteration, last one a branch, 10 iterations: each iteration 5 + 2 = 7 cycles, total = 4 + 50 + 20 = 74 cycles vs 54 with no stalls. If 20% of all instructions are branches, CPI = 1 + 0.2 x 2 = 1.4. Link to the mission: this is why a loop with many branches runs slower; also note the deeper the pipeline, the later the branch resolves, so the penalty grows (the "more stages" question, one sentence, with 7-stage pipeline resolving at the end of the stage 5 costing 4).

**Figure 5 (after the trace):** Cycle chart: beq row full; two shaded empty fetch cells in cycles 2 and 3 labelled "fetch waits: next instruction unknown"; target instruction IF in cycle 4. Arrow from beq's EX (end of cycle 3) to the IF in cycle 4: "outcome known, so fetch can restart". Caption: cost is the number of stages before the branch is decided, minus the one it already used (state as: stages up to and including EX, minus 1).

**Misconceptions:** (a) "A stall only happens if the branch is taken." Counter: in this design the stall happens for taken and not taken alike, 2 cycles either way. (b) "A branch is a data hazard because it reads registers." Counter: the cost came from not knowing the next address, not from a missing register value (r1 and r2 were already ready in this trace).

## Part 6: Hazard classification: name the cause and count the cost

**Key sentence:** Now put the three causes together: for any run of instructions, ask what is being waited for, and add up the waits.

**Word budget:** 650 (3-question test 80, worked example 250, faded practice 200, summary 70, go-further, closing and explain-it-yourself prompt 50). Extra detail: if short, one more line in the worked example showing the check that ideal + stalls equals the final cycle.

**The test (short):** (1) Is it hardware used twice in one cycle? structural. (2) Is it a value not yet written? data. (3) Is it not knowing the next instruction? control.

**Worked example:** `lw r1,0(r2)`, `add r3,r1,r4`, `beq r3,r0,L`, `sub r7,r8,r9` (at L). Trace: lw IF1 ID2 EX3 MEM4 WB5. add IF2, ID3, 4, 5 (waits for r1: data, 2 stalls), EX6 MEM7 WB8. beq IF3, 4, 5, ID6, 7, 8 (waits for r3 written in cycle 8: data, 2 stalls), EX9, resolves end of cycle 9. sub IF10 ID11 EX12 MEM13 WB14 (control, 2 stalls). Total 14 = 4 + 4 + 6. Table: instruction, cause, stalls. Structural: none, separate memories.

**Practice (faded steps, hints before solutions, solution on demand):** `add r1,r2,r3`, `or r6,r7,r8`, `sub r4,r1,r5`, `beq r6,r0,L`, `xor r9,r10,r11` (at L). Step 1 given: write each instruction's first-attempt stage cells. Step 2 fill: which instruction waits and for which register? Step 3 learner: count stalls and total. Hint 1: what is the gap between add and sub? Hint 2: which cycle does add write r1? Hint 3: when does beq finish EX? Solution: sub ID cycles 4, 5 (1 data stall); beq IF4-5, ID6, EX7, so xor IF8 (2 control stalls); total 4 + 5 + 3 = 12 cycles, CPI 2.4; structural none. (Not a quiz item; the quiz must use fresh sequences.)

**Summary (3 to 5 lines):** A stall is a cycle where the pipeline waits. Three causes: same hardware (structural), value not ready (data), next instruction unknown (control). Total cycles = 4 + N + stalls. Pipelining raises throughput, not per-instruction speed. Why it matters: branchy loops and deeper pipelines both pay in stall cycles.
**Prompt:** explain in your own words why a sequence of independent instructions can still stall, in two sentences.

**Real-world why:** the loop with many branches and the pipeline-depth question from MISSION.md appear in examples only (parts 5 and 6), not in titles or the win.

## Figures summary

Five cycle charts (figures 1-5) all in the same style: columns are cycles, rows are instructions, one colour for stall cells (the template's `--warn`), one for key cells (`--accent`). Optional figure 6: the three-question test as a short vertical flow (the three questions in order, each with its answer), for part 6. Labels at least 18 units in a viewBox about 640 wide; consider rotating long traces vertically or shrinking to cycles 1-9 only.

## Out of scope

Bypassing or forwarding in depth (a later objective); branch prediction; cache-miss stalls (mention in one sentence as another cause of waiting, not taught); out-of-order execution.

## Word budget table

| Part | Words |
|---|---|
| 1 Pipeline timing: one instruction is not faster, many finish sooner | 700 |
| 2 Stall and bubble: a cycle where the pipeline waits, and what it costs | 750 |
| 3 Structural hazard: two instructions need the same hardware in the same cycle | 750 |
| 4 Data hazard: an instruction needs a value an earlier one has not written yet | 850 |
| 5 Control hazard: the pipeline does not know which instruction comes next | 800 |
| 6 Hazard classification: name the cause and count the cost | 650 |
| **Total** | **4,500** |

## Sources (all opened in this session)

1. **PRIMARY.** Utah CS 3810 "Lecture 16: Pipeline Hazards" slides (guest lecture by Mahesh): https://users.cs.utah.edu/~aburtsev/3810/lectures/lecture12-hazards/lecture12-hazards.pdf
   Supports: the three one-line definitions (structural: multiple instructions contend for the same resource; data: a dependent instruction needs a value not yet produced; control: the next instruction cannot be fetched because the outcome of an earlier branch is unknown); unified memory as a structural hazard and separate instruction and data memories as the fix; register file read and write in the same cycle solved by half-cycle access; the 5-stage IF/ID/EX/MEM/WB layout.
2. Wikipedia, "Hazard (computer architecture)": https://en.wikipedia.org/wiki/Hazard_(computer_architecture)
   Supports: a stall inserts bubbles (NOPs) so the dependent instruction waits; read-after-write; structural hazards as instructions in the pipeline needing the same hardware; control hazards flush wrongly fetched instructions; prediction limits bubbles. Gives no cycle counts.
3. Search result only, not opened (do not cite as read, but they could be given under "Go further" if verified later): Cornell CS3410 slides https://www.cs.cornell.edu/courses/cs3410/2018sp/schedule/slides/07-pipeline-notes-bw.pdf and Crete HY425 https://www.csd.uoc.gr/~hy425/2008s/lectures/lec03-pipelines.pdf. Both were fetched but the PDF text did not come through, so their figures were not read.

**Caveats for the writer:** The cycle counts in parts 2 to 6 are derived by the conventions above (they are arithmetic, not quoted from a source); the lesson must say the conventions out loud. The formula 4 + N + stalls follows from the 5-stage fill time and is not quoted from a source. The branch-resolution cost (2 cycles for resolving at the end of EX) depends on the design; say so. H&P (Computer Architecture: A Quantitative Approach, appendix C; Computer Organization and Design ch. 4) was not opened; do not cite it by URL. No community was found; if one is added, verify its URL first.
