# Evaluation report

This is the report on what each step of your architecture bought and what it cost.
I read it for one thing above all: whether each claim matches its evidence, including the steps that did not pay.
A step you measured carefully and then dropped is as good a result as a step that won.

Three kinds of material go here.
The tables are pasted from commands: `uv run p3 report --configs a,b` for the objective checks, the cost and your ratings, and `uv run p3 compare --reveal <session-id>` for each blind comparison.
Paste them as they are, and name the session id or the run ids next to each one, so I can find them in `bench/compare/` and `bench/runs/`.
The evidence from your reviews stays in `reviews/`, and here you point at it: name the round, such as `c2-review` Round 3, or the criterion, such as the `c1-skills` review's Wording and possible misreadings, so I can follow the trail.
The prose is yours.

Each section ends with a marker line.
Replace that line with your own writing; `uv run p3 check --final` fails while one is left.

Words used below.
**Your ratings** is the table `p3 report` prints from your major reviews, one row per criterion and one column per step, from 1 to 5.
A **round** is a quick round in one of your step files in `reviews/`, and its **What changed** is the change Claude Code made from your thoughts in it.
A **pass** is one revise-and-review iteration inside one of your tutor's review loops, so a loop capped at two passes reviews a draft at most twice.
A **tally** is the wins for each config and the ties in one blind comparison, and the **p-value** is the reveal's two-sided sign test on the picks that were not ties: with 10 such picks, 8 for one config is suggestive and 9 is strong.
**Could tell** is the share of pairs where you said you could tell which config made which.
The objective checks use the names `p3 report` prints, such as `teach_facts_correct`, `quiz_key_agreement`, `grade_false_wrong` and `tutor_leaks`, the README's section "The scenarios and the objective checks" lists them, and `guide/06-the-bench.html` ("The headline numbers") says what each one measures.
**Cost** is tokens, output tokens, minutes and subagents per scenario, and the list-price equivalent, which is not what you pay on a subscription.

---

## 1. The baseline, `c0-baseline`

Paste the `p3 report` table for `c0-baseline` (three full runs on the shared topic).

Report from `uv run p3 report --configs c0-baseline` (3 scored full runs, agent-architecture):

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.69 (0.62-0.73) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |

Cost per run (list-price): teach $0.62, quiz $0.19, grade $0.33, tutor $0.64, all jobs $1.78 (1.73M tokens).

Runs:
- bench/runs/c0-baseline/20261111-002336-agent-architecture-m30-r1
- bench/runs/c0-baseline/20261111-002927-agent-architecture-m30-r2
- bench/runs/c0-baseline/20261111-003525-agent-architecture-m30-r3


What did the baseline do well, and where did it fall short, for each of the four jobs?
Read its outputs as you will read your own steps', because your `c1-skills` review compares against it.
Which of the gaps in `KNOWN-GAPS.md` did you see in your own runs, and did you find one that is not listed?
Which number moved the most from one run to the next, and what does that spread mean for a step measured on a single run?

What the baseline did well:
- Lesson: the core ideas are all there, and every key fact was correct in all three runs (teach facts 1.00).
- Quiz: the item types are fine, and the keys agreed with the solver on every item (key agreement 1.00).
- Feedback (grading): it graded every item correctly in all three runs (verdict agreement 1.00).
- Tutor: it says right or wrong first, then the reason, as I wanted; tutor-p03 in r1 opens with "No, that isn't right".

Where it fell short:
- Lesson: in my first review round (a live run with only the teach skill but already my preferences, bench/runs/_live/20261117-184442-agent-architecture-m30-r1) the lesson had 10 sections and long paragraphs, and its tone was too formal. Reading the c0 lesson now, it is fairly clear, but I want more detail with real examples at the same difficulty.
- Quiz: the items do not cover all the lesson's ideas evenly.
- Feedback (grading): I found nothing wrong.
- Tutor: the format is right, but I want more detailed, real examples that are not harder.

Gaps from KNOWN-GAPS.md that I saw in my own runs:
- The tutor narrows a quiz item down while refusing to answer it: tutor-p01 was not met in any of the three runs.
- The tutor answers above the learner's level: tutor-p05 was not met in r1 and r3.
- Tutor replies run long: tutor-p06 ran 335, 370 and 409 words and was not met in any run.
- Lessons come in short: length ratio 0.62, 0.73 and 0.71, just above the 0.6 floor.
One gap that is not listed: the quiz is on a different objective (O4, workflow versus agent) from the lesson (O3, context and memory), so it never tests what the lesson teaches.

The number that moved the most was tutor behavior met, from 0.50 to 0.67 across the three runs, then the length ratio, from 0.62 to 0.73. So a step measured on one run can only claim a change bigger than that spread: c1-skills' behavior met of 0.83 is above the baseline's best run, but its length ratio of 0.60 is only a little below the baseline's lowest, which one run cannot settle.



---

## 2. Step 1: `c1-skills` against `c0-baseline`

### What changed

Name the rounds that built this step, such as `c1-skills` Rounds 1 to 4, and the inventory entries of the skills they added; the trail from thoughts to change to outcome is already in `reviews/` and `reviews/components.md`, so do not retell it here.
Then what you put in `PREFERENCES.md`, and anything about how the four skills work together that no single inventory entry says.

`c1-skills` Rounds 1 to 3 changed teach, and Rounds 4 to 6 added tutor, quiz and grade. My preferences, in PREFERENCES.md, ask for short plain lessons with real examples and no answers given away.
The four skills share one set of guides: tutor, quiz and grade each read teach's reference files (TUTORING.md, QUIZZES.md, GRADING.md) and add their own rules on top, so teach keeps the common rules in one place. All four read PREFERENCES.md, NOTES.md and the learning records first, so what grade writes into the learning records shapes the next lesson and the next tutor reply. Only quiz and grade touch keys/; the tutor skill never opens it.


### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,c1-skills`: the objective checks, the cost per job, and your ratings.

From `uv run p3 report --configs c0-baseline,c1-skills`: behavior met went from 0.56 (`c0-baseline`) to 0.83 (`c1-skills`).
Report from `uv run p3 report --configs c0-baseline,c1-skills`:

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.69 (0.62-0.73) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |
| `c1-skills` | 1 | 1.00 | 0 | 0.60 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |

Cost per run (list-price):

| job | `c0-baseline` (3 runs) | `c1-skills` (1 run) |
|---|---|---|
| teach | 729.7k tokens, $0.62 | 1.38M tokens, $0.83 |
| quiz | 176.4k tokens, $0.19 | 122.8k tokens, $0.16 |
| grade | 282.0k tokens, $0.33 | 281.8k tokens, $0.30 |
| tutor | 544.5k tokens, $0.64 | 421.6k tokens, $0.41 |
| all jobs | 1.73M tokens, $1.78 | 2.20M tokens, $1.70 |

Runs:
- c0-baseline: bench/runs/c0-baseline/20261111-002336-agent-architecture-m30-r1, ...002927-...-r2, ...003525-...-r3
- c1-skills: bench/runs/c1-skills/20261117-220110-agent-architecture-m30-r1

Your ratings (from `uv run p3 report --configs c0-baseline,c1-skills --reviews`):

| job | criterion | c1-skills |
|---|---|---:|
| Lesson | Technical correctness and facts | 4 |
| Lesson | Pedagogy | 4 |
| Lesson | Alignment with the learning goal | 5 |
| Lesson | Overall quality | 4 |
| Quiz | Difficulty | 4 |
| Quiz | Coverage of the lesson's core | 3 |
| Quiz | Wording and possible misreadings | 5 |
| Quiz | Writing quality | 5 |
| Quiz | Alignment with the learning goal | 3 |
| Feedback | Useful | 3 |
| Feedback | Explains enough | 3 |
| Feedback | Personalized to how I like things explained | 5 |
| Tutor | Guardrails | 4 |
| Tutor | Personalization | 4 |


### What the step bought and what it cost

For each job: what did your major review find against `c0-baseline`, and did the objective checks agree?
Where they disagree, which do you believe, and why?
`c1-skills` is also the first config with your `PREFERENCES.md`, while `c0-baseline` keeps the neutral one: which of the differences could come from your preferences rather than the skills?
What did the step cost per scenario, and was the gain worth it?
Say what one run of `c1-skills` against three of `c0-baseline` lets you claim, and what it does not.


Per job, my major review against the objective checks:
- Lesson: I rated it 4, 4, 5, 4 and wanted more detail. The checks agree that it is short: the length ratio fell from 0.69 to 0.60, while teach facts stayed at 1.00.
- Quiz: I rated coverage and alignment 3, because almost every item is about workflow versus agent. Key agreement is 1.00 for both configs, so the checks see no difference. I believe my review here, because the checks only test whether the keys are right, not what the quiz covers.
- Feedback: I rated useful and explains enough 3, and personalized 5. Verdict agreement is 1.00 for both, so again the checks only show that grading stayed correct; whether the feedback helps is something only my review can see.
- Tutor: I rated guardrails and personalization 4, and the checks agree: behavior met went from 0.56 to 0.83, with tutor-p01 and tutor-p05 now met.

What could come from my preferences rather than the skills: the shorter lesson and the casual tone could come from my PREFERENCES.md ("Keep it short"). The tutor's hints that fit every option come from the tutor skill.

Cost: one full run cost $1.70 against $1.78 for the baseline. Teach got more expensive ($0.62 to $0.83, and 730k to 1.38M tokens), while tutor got cheaper ($0.64 to $0.41). For about the same total cost, the tutor improved clearly, so I think the step was worth it.

What one run lets me claim: behavior met of 0.83 is above the baseline's best run (0.67), so the tutor improvement is likely real. The length ratio of 0.60 is only a little below the baseline's lowest run (0.62), so one run cannot tell whether the lesson really got shorter. The other checks are the same for both configs.

---

## 3. Step 2: `c2-review` against `c1-skills`

### What changed

Name the rounds that built this step and the inventory entries of the reviewers they added, as in step 1.
Then the loops' design, for each of teach, quiz and grade: who reviews, what is on each reviewer's checklist and which items came from your `c1-skills` major review, how each reviewer gets a fresh context, how many passes a loop may run and what ends it early, and what each loop records.
Then one design choice you could have made the other way, such as one reviewer against several, a cap of one pass against three, or a reviewer that edits against one that only reports, and why you chose as you did.

`c2-review` Rounds 1 to 6 added three reviewer subagents, `quiz-reviewer` (Rounds 1 and 2), `grade-reviewer` (Rounds 3 and 4) and `lesson-reviewer` (Rounds 5 and 6), each with an entry in `reviews/components.md`; Rounds 2, 4 and 6 changed an existing reviewer or its skill after I read a run.

The loops, for each of teach, quiz and grade:
- Who reviews: one reviewer subagent per job. `quiz-reviewer` and `grade-reviewer` each have a checklist of nine checks, and `lesson-reviewer` has sixteen checks in four separate sections (facts, pedagogy, alignment, overall).
- What is on the checklists, from my `c1-skills` review: for the quiz, coverage spread over the objective's different ideas, difficulty that rises, and every term defined (my c1 Coverage rating of 3 and the undefined word "setup" in my live try); for grading, the verdict first, the exact part named, and a full reason with one simple real example (my c1 ratings of 3 for Useful and Explains enough); for the lesson, a simple real example for every named misconception, the idea after an example, and the length (my c1 Technical correctness and Overall quality ratings of 4).
- Fresh context: each reviewer is a subagent with its own file and its own tools (Read, Glob and Grep, plus WebSearch and WebFetch for the lesson's fact-check), so it cannot start subagents of its own. The skill gives it only the paths and the objective and does not tell it how the draft was written.
- Passes: at most two. The loop stops early when the reviewer's last line is "Verdict: done". The skills write drafts into `drafts/`, read each draft back before the review, and write the final file once.
- What each loop records: `review-records/NNNN-quiz.md`, `review-records/NNNN-sN-grade.md` and `review-records/NNNN-lesson.md`, with the passes, the findings and what changed.

One choice I could have made the other way: one lesson reviewer with four sections, against four reviewers. I chose one because every subagent pays its own share of the fixed load and reads the whole lesson again, and the teach scenario has a 45-minute limit. The risk is that findings blur together, so the reviewer reports each section under its own heading.

### The loops as they ran

For teach, quiz and grade: how many review passes ran in your bench run, what the reviewers flagged, and whether the revisions moved anything you can point at, a fact corrected, an ambiguous item rewritten, feedback that changed.
The loop records in the run's outputs are the evidence; name the files.

All three loops used the two-pass cap, and none ended early with "Verdict: done". The evidence is in `bench/runs/c2-review/20261121-003424-agent-architecture-m30-r1/`: `teach/outputs/review-records/0001-lesson.md`, `quiz/outputs/review-records/0002-quiz.md`, `grade-s1/outputs/review-records/0001-s1-grade.md` and `grade-s2/outputs/review-records/0001-s2-grade.md`. The run counted 2 lesson-reviewer, 2 quiz-reviewer and 5 grade-reviewer subagents.

- Teach: two passes. The reviewer fixed facts (a memory-tool claim cited to the wrong page, wasted-token arithmetic of 12,000 where the example gave 15,000, a figure whose bars were not to scale, a missing prompt-caching paragraph) and added real cases to the misconceptions and detail to a lesson that was about 23 minutes long (length ratio 0.60 in c1-skills, 0.87 here). Pass 2 still said "revise", and the last fixes were not reviewed again.
- Quiz: two passes. The reviewer saw q1 and q2 both asked for a definition, so q2 became a hybrid case, and it replaced weak distractors and removed words that gave the answer away, such as "fixed workflow" in q3.
- Grade: two passes on each submission. The reviewer asked for shorter feedback, a real example for q6 and a summary that points to an existing learning record. Two of its requests were refused by the writer because the grade skill required them ("Not quite." as the opener, and verdict first before the example).

Three rough spots in the records: in s1 the first reviewer run found nothing because the draft file had not been written yet; in s2 the pass-2 edit command failed, so pass 2 repeated pass 1; and in both cases the last edits were never reviewed again.

I think the loops moved things I can point at: facts corrected, an example added to every named misconception, a quiz item rewritten and feedback shortened. I cannot say the 0.60 to 0.87 length change came from the reviewer alone, because c2-review also has the length rule from my Round 6.


### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c1-skills,c2-review`.

Report from `uv run p3 report --configs c1-skills,c2-review` (one scored full run of each, agent-architecture):

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c1-skills` | 1 | 1.00 | 0 | 0.60 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |
| `c2-review` | 1 | 1.00 | 0 | 0.87 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.67 |

Cost per run (list-price):

| job | `c1-skills` | `c2-review` |
|---|---|---|
| teach | 1.38M tokens, 3.8 min, 0 subagents, $0.83 | 2.51M tokens, 8.0 min, 2 subagents, $1.52 |
| quiz | 122.8k tokens, 0.6 min, 0 subagents, $0.16 | 749.4k tokens, 3.7 min, 2 subagents, $0.49 |
| grade | 281.8k tokens, 0.9 min, 0 subagents, $0.30 | 1.42M tokens, 4.0 min, 5 subagents, $0.84 |
| tutor | 421.6k tokens, 1.0 min, 0 subagents, $0.41 | 520.2k tokens, 1.2 min, 0 subagents, $0.46 |
| all jobs | 2.20M tokens, 6.2 min, 0 subagents, $1.70 | 5.20M tokens, 16.9 min, 9 subagents, $3.31 |

Your ratings:

| job | criterion | c1-skills | c2-review |
|---|---|---:|---:|
| Lesson | Technical correctness and facts | 4 | 5 |
| Lesson | Pedagogy | 4 | 5 |
| Lesson | Alignment with the learning goal | 5 | 5 |
| Lesson | Overall quality | 4 | 4 |
| Quiz | Difficulty | 4 | 4 |
| Quiz | Coverage of the lesson's core | 3 | 5 |
| Quiz | Wording and possible misreadings | 5 | 5 |
| Quiz | Writing quality | 5 | 5 |
| Quiz | Alignment with the learning goal | 3 | 5 |
| Feedback | Useful | 3 | 5 |
| Feedback | Explains enough | 3 | 4 |
| Feedback | Personalized to how I like things explained | 5 | 5 |

Runs: c1-skills: bench/runs/c1-skills/20261117-220110-agent-architecture-m30-r1; c2-review: bench/runs/c2-review/20261121-003424-agent-architecture-m30-r1.


### What the step bought and what it cost

Did the problems your `c1-skills` review found go away, and which ratings moved?
Which loop earned its cost and which did not?
If a loop ran several passes and the final output was no better than the first draft, say so, because that is the finding.

Quiz: the review loop was not worth it. The quiz cost about three times as much ($0.16 to $0.49), yet its items did not get much harder: my Difficulty rating stayed at 4. Coverage and alignment went from 3 to 5, but that was because I learned the bench only asks for objective O4, not because the reviewer fixed anything.

Grade: the loop was not worth its cost either. My ratings rose a little (Useful 3 to 5, Explains enough 3 to 4), but grading was already correct in c1-skills (verdict agreement 1.00 in both), and the feedback still explains too little, such as what the model's output looks like in q2. For about 2.8 times the cost ($0.30 to $0.84), I expected a clearer explanation of that.

Teach: the loop was worth it. The lesson became longer (length ratio 0.60 to 0.87) and my Technical correctness and Pedagogy ratings both rose from 4 to 5, for about 1.8 times the cost ($0.83 to $1.52). It also followed the steps I asked for: each part opens with its key sentence, and every named misconception now has a simple real example.

What one run of each lets me claim: the length ratio went from 0.60 to 0.87, which is outside the baseline's spread of 0.62 to 0.73, so the lesson really got longer, although c2-review also has the length rule from my Round 6. Facts, key agreement and verdict agreement are 1.00 for both, so they only show nothing broke. Behavior met fell from 0.83 to 0.67 although the tutor was not changed, so a single run can move that much by chance, and I do not claim the loops changed anything about the tutor.


---

## 4. Step 3: `c3-split` against `c2-review`

### What changed

Name the rounds that built this step and the inventory entries of the pipeline's subagents.
Then the split: the roles you split the teach job into, what each one receives and returns, what runs in order and what in parallel, and who puts the lesson together at the end.
Why this split and not a smaller one, and what did you try that you took out again?

`c3-split` Rounds 1 to 7 built the split, and added the subagents `lesson-planner` (Rounds 1 and 2), `lesson-writer` (Round 3), `figure-designer` (Rounds 4 and 5) and `references-finder` (Round 6), each with an entry in `reviews/components.md`; Round 7 made no change and only recorded the result.

The split: the teach skill starts four subagents in order. The planner receives the objective and the minutes, reads the learner's files, and returns drafts/plan.md with the lesson title, up to six parts, each with a technical-term title, a key sentence, a word budget, one worked example and its figures. The references-finder receives the plan and returns drafts/sources.md, with each source checked. The writer receives the plan and the sources and returns the draft lesson, with placeholders for the figures. The figure-designer receives the draft and returns it with the figures drawn to scale. Then the c2-review lesson-reviewer reads the assembled draft for at most two passes, and the teach skill alone writes the final lesson into lessons/, once. Everything runs in order, none in parallel, because each role needs the output of the one before it.

I split into four roles and not a smaller pipeline because each reviewer finding that kept coming back belonged to one role: short lessons to the writer's word budgets, wrong figures to the figure-designer and wrong sources to the references-finder. I did not take any role out again after adding it.


### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c2-review,c3-split`.

Report from `uv run p3 report --configs c2-review,c3-split` (one scored full run of each, agent-architecture):

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c2-review` | 1 | 1.00 | 0 | 0.87 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.67 |
| `c3-split` | 1 | 1.00 | 0 | 0.90 | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.83 |

Cost per run (list-price):

| job | `c2-review` | `c3-split` |
|---|---|---|
| teach | 2.51M tokens, 8.0 min, 2 subagents, $1.52 | 2.24M tokens, 13.8 min, 6 subagents, $2.42 |
| all jobs | 5.20M tokens, 16.9 min, 9 subagents, $3.31 | 4.22M tokens, 20.3 min, 14 subagents, $4.13 |

Your ratings, Lesson only: Technical correctness and facts 5 and 5, Pedagogy 5 and 5, Alignment with the learning goal 5 and 5, Overall quality 4 and 5 (c2-review and c3-split).

Runs: c2-review: bench/runs/c2-review/20261121-003424-agent-architecture-m30-r1; c3-split: bench/runs/c3-split/20261122-004820-agent-architecture-m30-r1.


### What the step bought and what it cost

What did the split change in the lesson: its structure, its figures, its references, its fit to you, and how did your four Lesson ratings move against `c2-review`'s?
What did it cost in tokens, minutes and subagents against `c2-review`, and how much of that was overhead rather than writing?
Each step has one run, so say how confident you are, and what would change your mind.

Structure: every part now opens with its key sentence, with titles that are the course's technical term and a plain explanation, which the c2-review lesson did not have. Figures: four figures labelled in plain words with the reason beside every arrow, against two before. References: every source was opened and marked supported before it was cited. Fit to me: the lesson is clear, in my tone, at the length I asked for. My Lesson ratings were 5, 5, 5 and 4 for c2-review and 5, 5, 5 and 5 for c3-split, so only Overall quality moved, by one point.

It cost about $0.9 more on the teach scenario ($1.52 to $2.42) and 5.8 more minutes, with 6 subagents against 2. Most of that is overhead, not writing: each subagent pays its own share of the fixed load of a Claude Code session and reads the plan again. I think the step was worth it for the lesson, because the clearer titles and figures are what I asked for, but the gain over c2-review is small (the facts were already 1.00 and the length ratio moved from 0.87 to 0.90).

I have one run of each, so I am not sure the length change is real: the baseline's own runs varied by 0.11 in length ratio, which is about as large as the change I see. Three runs of each would change my mind.


---

## 5. `final` against `c0-baseline`, with repeats

### What went into `final`

A diagram of `final`: the main conversation, each skill, each subagent and the guard hook, with arrows for who starts whom and which files each one reads and writes.
ASCII art in a code block or a Mermaid block are both fine; for example:

```
/quiz (skill, main conversation)  writes drafts/0002.json
  -> quiz-reviewer (subagent, fresh context)  reads drafts/
  <- revise, at most 2 passes
  => quizzes/NNNN.json, keys/NNNN.json, review-records/NNNN-quiz.md
```

Draw yours, all four jobs, and delete the example.

TODO: your diagram.

What did you keep from each step, what did you drop, and why?
Point at the inventory entries in `reviews/components.md` rather than repeating them.
If `final` had to get cheaper tomorrow, which component would you cut first and which last, and what do you expect the tutor to lose?

TODO: what `final` is made of, and what you would cut first.

### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,final`, with three scored runs of each.

TODO: paste the report tables.

### What the repeats let you claim

For each headline number: is the difference between the two configs larger than the spread between runs of the same config?
Where the ranges overlap, say "not distinguishable with three runs", and do not rank the two by their means.
Then the overall cost: how many times more tokens and minutes per scenario does `final` take, and for which jobs is it worth it, by your review and by the numbers?

TODO: your reading of `final` against the baseline.

---

## 6. The ablation

Which component did `final-minus-<x>` remove, and what did you expect to happen before you ran it?
Paste `uv run p3 report --configs final,final-minus-<x>`.
What changed, in quality and in cost, and does one run against three let you say the component matters?
If you looked at its outputs, what did you see that the numbers do not show?

The ablation, `final-minus-references-finder`, removes the references-finder subagent, which opens every source in the plan, checks the link and that the page supports the claim, and writes drafts/sources.md for the writer and the reviewer.

My prediction, written before the run: without it, the facts in the lesson will go wrong more easily, because nothing checks the sources before the lesson is written, so `teach_facts_correct` may fall below 1.00 and the reviewer will flag more sources, but the cost will be a little lower, about 10 percent less on the teach scenario, because one subagent is not started.

---

## 7. The guard

What does your guard block, and what does it allow, and how does it tell the grader from the main conversation?
Why is it a PreToolUse hook in `tutor/.claude/settings.json`, and not a permission deny rule, a hook in a subagent's frontmatter, a subagent's `tools` list, or an instruction in a skill?
What changed elsewhere in the tutor because of it, such as grading handed to a subagent the guard allows?
Paste the result of running its tests, and list the cases they cover: the main conversation reading `keys/` with each of Read, Grep, Glob, Bash and PowerShell, the grader reading them, and the reads that must still work.
Then the bench evidence that the hook runs in the bench and not only in its tests: the run id and scenario of a trace where it allowed the grader's read of `keys/` or blocked the main conversation's, since a hook that fails to start lets every call through.
Then `tutor_leaks` for `final` against `c0-baseline`, and any denial of the guard you found in a trace.
Last, the gap you know of: one way the main conversation could still reach a key, or a case your tests do not cover, and why you accepted it or how you closed it.

Blocks: the main conversation reading keys/ with Read, Grep, Glob, Bash or PowerShell, in any path style, and a Grep over the whole workspace. Allows: the `grader` and `grade-reviewer` subagents, and all other reads. It tells them apart by `agent_type`, which only a subagent's input carries. Unreadable input is blocked.

Why a PreToolUse hook in `tutor/.claude/settings.json`: a deny rule would block the grader too, a hook in a subagent's frontmatter does not run in the bench, a `tools` list does not cover the main conversation, and a skill instruction can be ignored. `"onFailure": "block"` makes a crash block the call.

Changed elsewhere: grading moved to a `grader` subagent; the quiz skill no longer reads keys.

Tests: `python3 -m unittest tests.test_guard`, 27 tests, all OK. They cover the main conversation with each of the five tools and several path styles, the grader and grade-reviewer reading keys, another subagent being blocked, and the reads that must still work.

Bench evidence: `bench/runs/_live/20261122-012805-agent-architecture-m30-r1`, scenario grade-s1: the grader and grade-reviewer read `keys/0001.json` three times, the main conversation never did, and verdict agreement stayed 1.00. A manual try in tutor/ was refused, but I did not check the trace, so I cannot say whether the hook or the tutor's own rule refused it.

`tutor_leaks`, `final` against `c0-baseline`: TODO, after the runs of final.

Known gap: a shell command that builds the folder name at run time is not caught. I accepted it because the tutor's own rule also forbids keys/, and closing it would block most shell commands.


---

## 8. The blind comparison

### `c0-baseline` against `final`

Paste the reveals of the four sessions (teach, quiz, grade, tutor), three run pairs each, with their session ids.

TODO: paste the four reveals with their session ids.

### Your open reviews against your blind picks

This is the check on your own bias, as lecture 24 checks a model judge's.
For each job, what did your open reviews say about `final` against `c0-baseline`: your `final` major review, written before the blind comparison, your `c1-skills` review's comparison with the baseline, and your ratings across the ladder?
Then, for each job, did the blind tally and your reasons agree with them?
Where they disagree, what do you think happened: knowing the labels shaped what you saw in the open, the outputs you judged blind differed from the ones you reviewed, or the difference was too small to see?
Did your picks follow your open reviews more often in the pairs where you could tell than in the pairs where you could not?
Which do you believe now, and what does that say about the ratings in your reviews?

TODO: your open reviews against your blind picks.

### A second blind comparison

For 498E this is optional: if you made one, say which configs and job, why you chose it, paste its reveal, and say whether it agreed with your open reviews.
For 598E, and for the length-study stretch, the length study's three comparisons are your second; say so here and write them up in section 13.
If you made no second comparison, say so in one line.

TODO: your second blind comparison, or why there is none.

---

## 9. The test topics

### The two topics

Name each topic and its id, why you chose it, and the commit in which you committed its items, before its first run.
If you fixed a real mistake in a topic after its runs, as `bench/own/README.md` describes, list the run ids you deleted, what you changed and why.

TODO: your two topics and their commits.

### Results

For each topic, paste `uv run p3 report --topic <id> --configs c0-baseline,final`, and sum up your open review of the topic in `reviews/final.md` in two or three sentences.

TODO: paste the tables for both topics, with your summaries.

### Did the architecture still pay off?

Compare each topic with the shared topic: did `final` win where it won before, and did it fail somewhere new?
Was there anything about the topic, its kind of knowledge or its learner, that explains the difference?
On the life-skill topic, did both configs stay inside general knowledge when your probe asked for personal advice?

TODO: your reading of the test topics.

### Your learning sessions against the bench

Your three learning sessions are in `reviews/final.md`.
Did the bench predict what you saw in them?
Which failure from your sessions would a check or a review of a bench run have caught, and which could no fixed test have caught?
Would you use this tutor again for something you need to learn, and what would it need first?

TODO: the bench against your sessions.

---

## 10. The judge check

Take ten decisions the judge made: for example ten tutor replies it marked met or not met, or ten fact verdicts from your lessons (the judge checks six facts in each lesson on the shared topic, so ten come from two lessons).
Label each one yourself before you look at the judge's verdict, and list your ten labels and its ten verdicts here, with the run id and the scenario of each.
How many of ten did you agree on?
Read the disagreements: is the judge wrong, are you, or is the expected behavior unclear?
What does that agreement mean for the judge numbers you reported above?

TODO: your ten labels, the agreement, and what it means.

---

## 11. A change that did not pay off

At least one change, anywhere in the project, that cost you tokens, time or complexity and did not buy a difference you could see in your reviews or measure in the checks.
What was it, what did you expect, what did the evidence show, and what did you do about it?
Name the round or the inventory entry where it shows.

TODO: the change that did not pay off.

---

## 12. The trade-offs

Paste your ratings across the whole ladder, from `uv run p3 report --reviews`, and the cost of each step, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final`.

TODO: paste the ratings and cost tables for the whole ladder.

Looking at the whole ladder: which machinery paid for itself, which did not, and how do you know?
If you rebuilt this tutor for P4 with a third of the token budget, what would you keep?
Which number in this report do you trust least, your own ratings included, and why?

TODO: your trade-offs.

---

## 13. The stretch

For 598E this is the rider, and its write-up goes here, with `PREREG.md` beside it.
Cover five things:

1. the option's name;
2. what you did, and the files that hold it;
3. the evidence: the reviews, the blind comparisons, the objective checks and the cost it rests on, pasted or named;
4. what that evidence lets you claim, and what it does not;
5. one thing you would do next, and what result would tell you it worked.

TODO: your stretch.
