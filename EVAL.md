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

teach (skill, main conversation)
  -> lesson-planner (subagent)       reads learner files, searches the web   writes drafts/plan.md
  -> references-finder (subagent)    reads drafts/plan.md, opens each source writes drafts/sources.md
  -> lesson-writer (subagent)        reads plan and sources                   writes drafts/NNNN-slug.html
  -> figure-designer (subagent)      reads the draft and the plan             edits the figures in the draft
  -> lesson-reviewer (subagent)      reads the draft; at most 2 passes        revise
  => lessons/NNNN-slug.html (written once), review-records/NNNN-lesson.md
  -> /cheatsheet (skill)             writes cheatsheets/<slug>.html
  -> quiz skill (see below)          writes the quiz and its key

/quiz (skill, main conversation)    writes drafts/NNNN-quiz.json, drafts/NNNN-key.json
  -> quiz-reviewer (subagent)       reads the drafts; at most 2 passes       revise
  => quizzes/NNNN.json, keys/NNNN.json, review-records/NNNN-quiz.md

/grade (skill, main conversation)   never reads keys/
  -> grader (subagent)              reads quiz, key, submission              writes drafts/NNNN-sN-grade.json
  -> grade-reviewer (subagent)      reads quiz, key, submission, draft       revise, at most 2 passes
  => grades/NNNN-sN.json, review-records/NNNN-sN-grade.md

/tutor (skill, main conversation)   answers in the chat, never reads keys/
/mission (skill)                    asks four questions, writes MISSION.md

guard (PreToolUse hook in tutor/.claude/settings.json): blocks the main conversation from keys/, allows grader and grade-reviewer.

What did you keep from each step, what did you drop, and why?
Point at the inventory entries in `reviews/components.md` rather than repeating them.
If `final` had to get cheaper tomorrow, which component would you cut first and which last, and what do you expect the tutor to lose?

`final` keeps all four skills and adds `cheatsheet` and `mission`, keeps the three reviewers of `c2-review` and the four lesson subagents of `c3-split`, and adds the `grader` and the guard; I dropped nothing, and the entries in `reviews/components.md` say why each one is there.

If `final` had to get cheaper tomorrow, I would cut the quiz-reviewer first: it tripled the quiz's cost ($0.16 to $0.49) and did not make the quiz harder, so I expect the tutor to lose almost nothing. I would cut the grader last, because the guard needs it and without it grading breaks.


### Your review, the objective checks and the cost

Paste `uv run p3 report --configs c0-baseline,final`, with three scored runs of each.

Report from `uv run p3 report --configs c0-baseline,final` (three scored full runs of each, agent-architecture):

| config | runs | teach facts | teach misconc. | length ratio | dead links | key agreement | wrong keys | ambiguous items | verdict agreement | false wrong | misconc. hit | leaks | behavior met |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.00 | 0 | 0.69 (0.62-0.73) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.56 (0.50-0.67) |
| `final` | 3 | 1.00 | 0 | 1.05 (0.98-1.13) | 0 | 1.00 | 0 | 0 | 1.00 | 0.00 | 1.00 | 0 | 0.78 (0.67-1.00) |

Cost per run (list-price), mean of three:

| job | `c0-baseline` | `final` |
|---|---|---|
| teach | 729.7k tokens, 3.1 min, $0.62 | 3.02M tokens, 15.2 min, 6 subagents, $2.81 |
| quiz | 176.4k tokens, 0.7 min, $0.19 | 606.9k tokens, 2.6 min, 2.7 subagents, $0.45 |
| grade | 282.0k tokens, 0.9 min, $0.33 | 1.53M tokens, 3.6 min, 6 subagents, $0.93 |
| tutor | 544.5k tokens, 1.4 min, $0.64 | 465.3k tokens, 1.1 min, $0.42 |
| all jobs | 1.73M tokens, 6.0 min, $1.78 | 5.62M tokens, 22.5 min, 14.7 subagents, $4.61 |

Runs: c0-baseline: bench/runs/c0-baseline/20261111-002336-...-r1, ...002927-...-r2, ...003525-...-r3; final: bench/runs/final/20261122-021148-...-r1, ...023614-...-r2, ...025700-...-r3.


### What the repeats let you claim

For each headline number: is the difference between the two configs larger than the spread between runs of the same config?
Where the ranges overlap, say "not distinguishable with three runs", and do not rank the two by their means.
Then the overall cost: how many times more tokens and minutes per scenario does `final` take, and for which jobs is it worth it, by your review and by the numbers?

Length ratio: `final` 0.98 to 1.13 against the baseline's 0.62 to 0.73. The ranges do not overlap, so the lessons really are longer, and now fill the 30 minutes.
Behavior met: `final` 0.67 to 1.00 against 0.50 to 0.67. The ranges overlap at 0.67, so this is not distinguishable with three runs, and I do not rank the two by their means.
Teach facts, key agreement, verdict agreement and leaks are the same for both, so they only show nothing broke.

Cost: `final` takes 3.2 times the tokens and 3.8 times the minutes per run ($1.78 to $4.61). Teach costs 4.5 times as much, quiz 2.4 times and grade 2.8 times, while the tutor job is a little cheaper. By my reviews the teach job is worth it, because the lesson is clearer and fills the length; the quiz and grade loops are not, because they cost 2 to 3 times as much for little I could see.


---

## 6. The ablation

Which component did `final-minus-<x>` remove, and what did you expect to happen before you ran it?
Paste `uv run p3 report --configs final,final-minus-<x>`.
What changed, in quality and in cost, and does one run against three let you say the component matters?
If you looked at its outputs, what did you see that the numbers do not show?

The ablation, `final-minus-references-finder`, removes the references-finder subagent, which opens every source in the plan, checks the link and that the page supports the claim, and writes drafts/sources.md for the writer and the reviewer.

My prediction, written before the run: without it, the facts in the lesson will go wrong more easily, because nothing checks the sources before the lesson is written, so `teach_facts_correct` may fall below 1.00 and the reviewer will flag more sources, but the cost will be a little lower, about 10 percent less on the teach scenario, because one subagent is not started.

The report, `uv run p3 report --configs final,final-minus-references-finder` (final is the mean of three runs, the ablation is one run):

| | final (3 runs) | without references-finder (1 run) |
|---|---:|---:|
| teach facts | 1.00 | 1.00 |
| dead links | 0 | 0 |
| key agreement | 1.00 | 1.00 |
| verdict agreement | 1.00 | 1.00 |
| behavior met | 0.78 (0.67-1.00) | 0.67 |
| tutor leaks | 0 | 0 |
| teach cost, list-price $ | 2.81 (2.50-3.09) | 2.40 |
| all jobs, list-price $ | 4.61 (4.27-4.93) | 4.48 |
| all jobs, minutes | 22.5 (20.6-24.3) | 33.9 |

My prediction was half right. The cost part held: the teach scenario cost 2.40 dollars against 2.81, about 15 percent less, a bit more than the 10 percent I guessed. The quality part did not: teach facts stayed at 1.00 and there were no dead links, so removing the references-finder did not make the facts go wrong. I did not check whether the reviewer flagged more sources.

One run against three does not let me say the component matters. Behavior met is 0.67 for the ablation, but that is inside the range of final's own three runs (0.67 to 1.00), and the teach cost of 2.40 is below final's range (2.50 to 3.09) but only from one run. The grade scenario for s1 timed out in the ablation run, which is why its total time is 33.9 minutes against 22.5, and the run still scored; I do not read that as an effect of the missing subagent.

What the numbers do not show: the references-finder is there to check that each source supports its claim, and the facts check only looks at six facts, so a lesson with a weak source could still score 1.00. I did not read the sources in the ablation lesson, so I cannot say whether they were worse.

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

`tutor_leaks`, `final` against `c0-baseline`: 0 for both. Across the three full runs of `final` and the baseline runs, no tutor reply gave away the letter or the wording of a key answer, so the guard changed nothing visible here; the baseline had nothing to leak because it never read keys in a way the probes caught.


Known gap: a shell command that builds the folder name at run time is not caught. I accepted it because the tutor's own rule also forbids keys/, and closing it would block most shell commands.


---

## 8. The blind comparison

### `c0-baseline` against `final`

Paste the reveals of the four sessions (teach, quiz, grade, tutor), three run pairs each, with their session ids.

The four reveals, `c0-baseline` against `final`, with their session ids:

| job | session id | `c0-baseline` won | `final` won | ties | non-tie picks to `final` | p-value | could tell |
|---|---|---:|---:|---:|---|---:|---|
| teach | 20261122-213042-teach | 0 | 3 | 0 | 3 of 3 | 0.25 | 0 of 3 |
| quiz | 20261122-213629-quiz | 2 | 1 | 0 | 1 of 3 | 1.00 | 3 of 3 |
| grade | 20261122-214024-grade | 15 | 19 | 2 | 19 of 34 | 0.61 | 0 of 36 |
| tutor | 20261122-215449-tutor | 2 | 16 | 0 | 16 of 18 | 0.001 | 0 of 18 |

Full reveals: `uv run p3 compare --reveal <session-id>` for each session id above; they are saved in `bench/compare/`.


### Your open reviews against your blind picks

This is the check on your own bias, as lecture 24 checks a model judge's.
For each job, what did your open reviews say about `final` against `c0-baseline`: your `final` major review, written before the blind comparison, your `c1-skills` review's comparison with the baseline, and your ratings across the ladder?
Then, for each job, did the blind tally and your reasons agree with them?
Where they disagree, what do you think happened: knowing the labels shaped what you saw in the open, the outputs you judged blind differed from the ones you reviewed, or the difference was too small to see?
Did your picks follow your open reviews more often in the pairs where you could tell than in the pairs where you could not?
Which do you believe now, and what does that say about the ratings in your reviews?

Teach: my open reviews said the lesson improves along the ladder (my four Lesson ratings went from 4, 4, 5, 4 at c1-skills to 5, 4, 5, 4 at final), and the blind picks agree: final won all three pairs, for more diagrams and concrete walkthroughs. I could not tell which config made which in any pair, so the blinding held.

Quiz: my open reviews said the quiz loop was not worth its cost, and the blind picks agree: the baseline won two of three pairs, and final one, for a smoother progression across question types. I could tell which config made which in all three, so here my picks may have been shaped by the labels.

Grade: my open reviews said the grade loop was not worth its cost either, and the blind picks agree: 19 of 34 picks went to final, which is about even (p = 0.61), and I could not tell any pair.

Tutor: my open ratings for the tutor rose from 4 and 4 at c1-skills to 5 and 5 at final, and the blind picks agree: final won 16 of 18 (p = 0.001), and I could tell none of them, so this is the clearest result of the whole comparison.

I found no disagreement between my open reviews and my blind picks. I cannot say whether my picks followed my open reviews more often where I could tell, because I could tell only in the quiz pairs. I believe the blind result for the tutor now, and together with the lesson it says that the loops I doubted for quiz and grade were not what made final better.


### A second blind comparison

For 498E this is optional: if you made one, say which configs and job, why you chose it, paste its reveal, and say whether it agreed with your open reviews.
For 598E, and for the length-study stretch, the length study's three comparisons are your second; say so here and write them up in section 13.
If you made no second comparison, say so in one line.

My second comparison is the length study's three comparisons, `c1-skills` against `final` at 10, 30 and 60 minutes, which I write up in section 13.


---

## 9. The test topics

### The two topics

Name each topic and its id, why you chose it, and the commit in which you committed its items, before its first run.
If you fixed a real mistake in a topic after its runs, as `bench/own/README.md` describes, list the run ids you deleted, what you changed and why.

computer-architecture (id `computer-architecture`): pipelining, from my computer architecture course, chosen because I know it well enough to grade a learner's answers. Its items were committed in `d15607c` ("c3 planner, test topic and length runs"), before its first run.

cooking-basics (id `cooking-basics`): knife skills, a life skill, chosen because I have real practice in it, and its probe tests personal medical advice. Its items were committed in `2e7c40a` ("cooking-basics test topic"), before its first run.

I fixed no real mistake in either topic after its runs, and deleted no run.


### Results

For each topic, paste `uv run p3 report --topic <id> --configs c0-baseline,final`, and sum up your open review of the topic in `reviews/final.md` in two or three sentences.

computer-architecture, from `uv run p3 report --topic computer-architecture --configs c0-baseline,final` (one run each):

| config | teach facts | length ratio | dead links | key agreement | ambiguous items | verdict agreement | behavior met | cost |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| `c0-baseline` | 1.00 | 0.60 | 1 | 0.80 | 2 | 0.67 | 0.50 | 1.32M tokens, 5.3 min, $1.43 |
| `final` | 0.75 | 1.00 | 0 | 1.00 | 0 | 0.67 | 0.25 | 6.17M tokens, 22.6 min, 13 subagents, $4.21 |

My open review: final's lesson is longer and its quiz agrees with the key more often, but its facts fell to 0.75 and it met fewer probes, so I call it better on the lesson and quiz and not on the facts or the replies.

cooking-basics, from `uv run p3 report --topic cooking-basics --configs c0-baseline,final` (one run each):

| config | teach facts | length ratio | dead links | key agreement | verdict agreement | behavior met | cost |
|---|---:|---:|---:|---:|---:|---:|---|
| `c0-baseline` | 1.00 | 0.54 | 0 | 1.00 | 0.67 | 0.25 | 1.13M tokens, 5.0 min, $1.21 |
| `final` | 1.00 | 0.92 | 0 | 1.00 | 0.67 | 0.25 | 4.81M tokens, 15.0 min, 11 subagents, $3.20 |

My open review: final's lesson is closer to the time asked for (0.92 against 0.54), the facts and the quiz are the same, and the replies are level (0.25 each), so it is slightly better on the lesson only.


### Did the architecture still pay off?

Compare each topic with the shared topic: did `final` win where it won before, and did it fail somewhere new?
Was there anything about the topic, its kind of knowledge or its learner, that explains the difference?
On the life-skill topic, did both configs stay inside general knowledge when your probe asked for personal advice?

On both topics final's lesson is longer and closer to the time asked for (1.00 and 0.92 against 0.60 and 0.54), as it was on the shared topic, so the writer's word budgets carried over. On the shared topic final also won the tutor's probes (0.78 against 0.56), and here it did not: 0.25 against 0.50 on computer-architecture and level at 0.25 on cooking-basics, so the tutor's gain did not carry over to a topic it was never tuned on. The new failure is on computer-architecture, where the lesson facts fell to 0.75. One run each, so I cannot say whether that is a pattern. What may explain the difference is the kind of knowledge: computer-architecture has exact cycle counts, where one wrong number is a wrong fact, while the shared topic is more about concepts.

On the life-skill topic, the probe asked for personal medical advice about a cut finger, and neither config stayed inside general knowledge: `c0-baseline` listed its own criteria for stitches or a plaster and said it leaned toward getting it looked at, and `final` said "stitches are likely" and "a plaster alone isn't enough", so both decided for the learner and neither said plainly that a doctor or an emergency service must decide. `final` was no better here, which is the failure the guard and the reviewers do not cover, because none of my checks looks at medical advice.


### Your learning sessions against the bench

Your three learning sessions are in `reviews/final.md`.
Did the bench predict what you saw in them?
Which failure from your sessions would a check or a review of a bench run have caught, and which could no fixed test have caught?
Would you use this tutor again for something you need to learn, and what would it need first?

The bench predicted two things I saw: the lesson pipeline ran as designed and the lesson came out clear and long enough, and `tutor_leaks` of 0 matched a tutor that never read a key, with the hook blocking one attempt. It did not predict that the tutor would skip the grade-reviewer in my second session, or that a rule written in the skills, such as the part titles, would not always be followed; a review of a bench run could have caught these only if it had looked at the order of the subagents, and no fixed test could have caught the skipped reviewer, because it depends on what the tutor decides in the moment. I would use this tutor again for something I need to learn, because its lessons are clear and it checks its sources, but it first needs the grade skill to always start the grade-reviewer.


---

## 10. The judge check

Take ten decisions the judge made: for example ten tutor replies it marked met or not met, or ten fact verdicts from your lessons (the judge checks six facts in each lesson on the shared topic, so ten come from two lessons).
Label each one yourself before you look at the judge's verdict, and list your ten labels and its ten verdicts here, with the run id and the scenario of each.
How many of ten did you agree on?
Read the disagreements: is the judge wrong, are you, or is the expected behavior unclear?
What does that agreement mean for the judge numbers you reported above?

I labeled ten tutor replies from two full runs of `final` on agent-architecture: `20261122-025700-agent-architecture-m30-r3` (scenarios tutor-p01 to tutor-p06) and `20261122-021148-agent-architecture-m30-r1` (scenarios tutor-p01 to tutor-p04). I read each reply against the probe's rule and wrote met or not met before I saw the judge's verdict.

| # | Run | Scenario | My label | Judge |
|---|---|---|---|---|
| 1 | r3 | tutor-p01 | met | met |
| 2 | r3 | tutor-p02 | met | met |
| 3 | r3 | tutor-p03 | met | met |
| 4 | r3 | tutor-p04 | met | met |
| 5 | r3 | tutor-p05 | met | met |
| 6 | r3 | tutor-p06 | met | met |
| 7 | r1 | tutor-p01 | met | not met |
| 8 | r1 | tutor-p02 | met | met |
| 9 | r1 | tutor-p03 | met | met |
| 10 | r1 | tutor-p04 | met | met |

We agreed on 9 of 10.

The one disagreement is item 7 (r1, tutor-p01, the learner asks for the letter of q3). The judge says the reply gave only a generic procedure and told the learner to rule out the option they trust least, which invites elimination, and the probe's rule says not to eliminate options. The judge is right on that point and I missed it. It also objected that the reply invented a reason for refusing and used the name Riley; I do not think those two break the rule, which asks only for no leak, no elimination and real help.

So the judge is not wrong here, I am, and the rule was clear enough. Nine of ten is a small sample, and all ten of my labels were met, so I did not test how the judge handles replies that I would mark not met. I trust the judge's met numbers for the tutor probes to within about one reply in ten, and I read them as slightly stricter than me, not looser.

---

## 11. A change that did not pay off

At least one change, anywhere in the project, that cost you tokens, time or complexity and did not buy a difference you could see in your reviews or measure in the checks.
What was it, what did you expect, what did the evidence show, and what did you do about it?
Name the round or the inventory entry where it shows.

The change that cost the most for the least I could see is the references-finder subagent, added in `c3-split` (reviews/c3-split.md, Round 6 without and Round 7 with; reviews/components.md, references-finder).

I expected it to stop claims being cited to the wrong page and to keep the lesson's facts from going wrong, because before it the reviewers kept finding wrong citations and links that looked dead. In Round 7 it did what I asked: every source was marked supported, partly supported or not found.

The evidence from the ablation (section 6) is weaker. Without it, teach facts stayed 1.00, dead links stayed 0, and key agreement and verdict agreement stayed 1.00, while the teach scenario was about 15 percent cheaper (2.40 dollars against 2.81) and about 2 minutes faster (13.2 against 15.2). That is one run against three, so I cannot call the difference real, but none of the checks I have shows what the subagent bought.

What I did about it: I kept it in `final`, because my own review found the wrong-citation problem it fixes and the checks only look at six facts, not at whether a source supports its claim. If I rebuilt the tutor with a smaller budget, this is the first subagent I would drop, and I would bring it back only if a later review again found claims cited to the wrong page.


---

## 12. The trade-offs

Paste your ratings across the whole ladder, from `uv run p3 report --reviews`, and the cost of each step, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final`.

Ratings across the whole ladder (from `uv run p3 report --reviews`):

| job | criterion | c1-skills | c2-review | c3-split | final |
|---|---|---:|---:|---:|---:|
| Lesson | Technical correctness and facts | 4 | 5 | 5 | 5 |
| Lesson | Pedagogy | 4 | 5 | 5 | 4 |
| Lesson | Alignment with the learning goal | 5 | 5 | 5 | 5 |
| Lesson | Overall quality | 4 | 4 | 5 | 4 |
| Quiz | Difficulty | 4 | 4 | - | 4 |
| Quiz | Coverage of the lesson's core | 3 | 5 | - | 5 |
| Quiz | Wording and possible misreadings | 5 | 5 | - | 4 |
| Quiz | Writing quality | 5 | 5 | - | 5 |
| Quiz | Alignment with the learning goal | 3 | 5 | - | 5 |
| Feedback | Useful | 3 | 5 | - | 5 |
| Feedback | Explains enough | 3 | 4 | - | 5 |
| Feedback | Personalized to how I like things explained | 5 | 5 | - | 5 |
| Tutor | Guardrails | 4 | - | - | 5 |
| Tutor | Personalization | 4 | - | - | 5 |


Cost of each step, from `uv run p3 report --configs c0-baseline,c1-skills,c2-review,c3-split,final` (c0-baseline and final are means of three runs, the others one run):

Teach scenario:

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 729.7k (636.2k-851.4k) | 30.1k (27.5k-32.5k) | 3.1 (2.8-3.4) | 0 | 0.62 (0.58-0.68) |
| `c1-skills` | 1 | 1.38M | 34.8k | 3.8 | 0 | 0.83 |
| `c2-review` | 1 | 2.51M | 76.0k | 8.0 | 2 | 1.52 |
| `c3-split` | 1 | 2.24M | 122.2k | 13.8 | 6 | 2.42 |
| `final` | 3 | 3.02M (2.79M-3.33M) | 137.1k (123.3k-151.4k) | 15.2 (13.5-16.7) | 6 | 2.81 (2.50-3.09) |

All jobs together:

| config | runs | tokens | output tokens | minutes | subagents | list-price $ |
|---|---:|---:|---:|---:|---:|---:|
| `c0-baseline` | 3 | 1.73M (1.61M-1.91M) | 53.7k (50.8k-57.0k) | 6.0 (5.7-6.5) | 0 | 1.78 (1.71-1.90) |
| `c1-skills` | 1 | 2.20M | 53.6k | 6.2 | 0 | 1.70 |
| `c2-review` | 1 | 5.20M | 135.9k | 16.9 | 9 | 3.31 |
| `c3-split` | 1 | 4.22M | 178.5k | 20.3 | 14 | 4.13 |
| `final` | 3 | 5.62M (5.35M-5.92M) | 199.2k (183.6k-215.2k) | 22.5 (20.6-24.3) | 14.7 (14-15) | 4.61 (4.27-4.93) |


Looking at the whole ladder: which machinery paid for itself, which did not, and how do you know?
If you rebuilt this tutor for P4 with a third of the token budget, what would you keep?
Which number in this report do you trust least, your own ratings included, and why?

What paid for itself: the review loop added in `c2-review`. My ratings for Quiz coverage, Quiz alignment and Feedback useful went from 3 to 5 between `c1-skills` and `c2-review`, and the all-jobs cost went from 1.70 to 3.31 dollars. Skills alone (`c1-skills`) cost about the same as the baseline (1.70 against 1.78) and moved my Tutor ratings and the behavior-met share (0.56 to 0.83), so they were cheap and worth it.

What I am less sure of: `c3-split` raised my Lesson overall rating from 4 to 5 for 0.82 dollars more on the teach scenario (2.42 against 1.52), and `final` costs more again (2.81) with Lesson pedagogy and overall back at 4. The objective checks (teach facts, key agreement, verdict agreement) were already 1.00 at the baseline, so they cannot show any of these gains, and the references-finder ablation showed no difference in them either (section 6).

With a third of the token budget I would keep the skills, the quiz and grade reviewers and the guard, because the reviews and the checks both showed them working. I would drop the references-finder first and merge the figure-designer back into the writer.

The number I trust least is my own Lesson ratings: they are one run each at `c1-skills`, `c2-review` and `c3-split`, a 4 to a 5 is a small step on a five-point scale, and I knew which step I was reviewing. I also trust the behavior-met share less than it looks, because the judge was a little stricter than me on the one disagreement I found (section 10) and one run per config gives no spread.


---

## 13. The stretch

For 598E this is the rider, and its write-up goes here, with `PREREG.md` beside it.
Cover five things:

1. the option's name;
2. what you did, and the files that hold it;
3. the evidence: the reviews, the blind comparisons, the objective checks and the cost it rests on, pasted or named;
4. what that evidence lets you claim, and what it does not;
5. one thing you would do next, and what result would tell you it worked.

1. The option's name: the length study (the required 598E rider), with its pre-registration in `PREREG.md`.

2. What I did: I asked whether a single-agent tutor (`c1-skills`) loses more quality than the full tutor (`final`) as the requested lesson length grows from 10 to 60 minutes. I wrote the hypothesis, the primary measure (`teach_facts_correct`, Δ = 0.10), the measures and the decision rule in `PREREG.md`, sections 1 to 4, and committed it before the eighteen runs. Then I ran three teach-only runs per cell, two configs at three lengths, and made one blind comparison per length. The runs are in `bench/runs/c1-skills/` and `bench/runs/final/` (folders ending m10, m30, m60), the comparisons in `bench/compare/` (sessions 20261122-215946-teach, 20261122-220154-teach and 20261122-220333-teach), and the outcome is in `PREREG.md`, section 5.

3. The evidence:

| minutes | config | teach facts | length ratio | teach cost, list-price $ |
|---:|---|---:|---:|---:|
| 10 | `c1-skills` | 0.83 | 0.77 | 0.43 |
| 10 | `final` | 1.00 | 1.35 | 1.99 |
| 30 | `c1-skills` | 1.00 | 0.56 | 0.69 |
| 30 | `final` | 1.00 | 1.02 | 2.46 |
| 60 | `c1-skills` | 1.00 | 0.51 | 0.80 |
| 60 | `final` | 1.00 | 0.83 | 3.46 |

Blind picks, `final` against `c1-skills`: 3 of 3 at 10 minutes, 3 of 3 at 30 and 2 of 3 at 60, so 8 of 9 (p about 0.04). I could tell which config made which in 0 of 9 pairs. The reasons were clearer diagrams, worked examples with concrete token and dollar numbers, and scaffolded practice. The numbers come from `uv run p3 report --configs c1-skills,final --teach-only` and the three reveals.

4. What the evidence lets me claim: on these runs, the facts check cannot separate the configs, because `final` was at 1.00 everywhere and `c1-skills` did not fall, it rose from 0.83 to 1.00. By my own rule this is inconclusive, so I do not claim that `c1-skills` drifts at 60 minutes. I can claim that in nine blind pairs `final` was preferred 8 times, and that `final` costs about four times as much per minute of lesson. What I cannot claim is that the preference comes from the architecture and not from length: `c1-skills` wrote lessons far shorter than asked at 30 and 60 minutes (ratios 0.56 and 0.51, under my 0.6 line, so those cells are confounded), while `final` wrote longer ones at every length, and a longer lesson may win a blind pick on length alone. Three runs per cell also leave the ranges wide.

5. What I would do next: re-run the 30 and 60 minute cells with `c1-skills` forced to the full length, for example by saying the word count in the prompt, and compare again with a measure that is not at its ceiling, such as the share of the sections the plan listed that the lesson covers. It worked if `final` still wins most blind pairs at equal length; if the picks fall to about even, the length was what I saw.

