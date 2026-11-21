# Reviews: c2-review

Your quick rounds while you build the review loops on teach, quiz and grade, and then the major review of `c2-review`.
Add one reviewer subagent per round, so the run before it shows the output without it and the run after it shows the output with it.
The major review covers the lesson, the quiz and the feedback, and its previous step is `c1-skills`.
Say in it whether the problems your `c1-skills` review found are gone.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c1-skills/20261117-220110-agent-architecture-m30-r1, the c1-skills full run


**My thoughts:**

The c1-skills problems I want the review loops to catch: the quiz tests only workflow versus agent and never what goes into the context, the grading feedback needs simpler real examples, and the lesson needs more detail with real examples.
I want a reviewer for the quiz first, with a checklist that checks every item against the lesson's main ideas, so the quiz covers them evenly.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz tested only one idea and nothing checked it against the lesson, so a quiz-reviewer subagent with a fresh context now checks coverage, rising difficulty and undefined terms, and the quiz skill drafts in drafts/, runs it for at most two passes, and writes the final files once.

### Round 2

**Run:** bench/runs/_live/20261119-213037-agent-architecture-m30-r1, quiz only


**My thoughts:**

The quiz-reviewer helped with difficulty: the last three items are a bit harder than before, and q6 is a mixed case that needs a fixed part and an open-ended part.
It did not fix coverage: all six items are still about workflow versus agent, and no item tests any other concept.
I want the reviewer's coverage check to make the quiz spread across the objective's different ideas, not only one.


**What changed:**

- Kind: other
- Files: tutor/.claude/agents/quiz-reviewer.md, tutor/.claude/skills/quiz/SKILL.md
- Why: The reviewer helped with difficulty but all six items still tested one idea, so its coverage check now splits the objective into distinct ideas, flags any idea with no item or more than two, and the quiz skill plans its items across those ideas before writing.

### Round 3

**Run:** **Run:** bench/runs/_live/20261119-214018-agent-architecture-m30-r1, quiz only


**My thoughts:**

The quiz-reviewer's second version helped: the six items now cover different angles of workflow versus agent, and the questions are clear. The topic stays inside objective O4, which is what the bench asks for, so I do not need a wider quiz.
The review record shows two rough spots: the first reviewer run found nothing because the draft file had not been written yet, and the last revision got no second look because of the two-pass cap.
I want the next reviewer to be for grading.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grade-reviewer.md, tutor/.claude/skills/grade/SKILL.md
- Why: The quiz-reviewer worked and these thoughts ask for the next reviewer to be for grading, so a grade-reviewer with a fresh context now checks verdicts, the exact part named, a simple real example and plain wording, and the grade skill drafts in drafts/, confirms the draft was written before the review, runs at most two passes, and writes the final file once.

### Round 4

**Run:** bench/runs/_live/20261119-214929-agent-architecture-m30-r1, grade-s1 and grade-s2


**My thoughts:**

The grade-reviewer helped: verdicts and misconception ids stayed fully correct, and the feedback now has real examples, like the check_calendar text in q6. The q2 feedback no longer gives the full answer away, and q4 got shorter.
But several explanations end with a question instead of explaining, such as q4's "what does it ask for, and how many more inputs follow?". These items are already graded, so I want the feedback to explain in full, with a simple real example, and not ask me a question.


**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/grade/SKILL.md, tutor/.claude/agents/grade-reviewer.md
- Why: Graded items still got hints and closing questions, so the grade skill now explains a graded item in full with one simple real example and never ends feedback or the summary with a question, and the grade-reviewer flags any hint or question in its place.

### Round 5

**Run:** bench/runs/c1-skills/20261117-220110-agent-architecture-m30-r1, the c1-skills full run, lesson only


**My thoughts:**

The quiz and grade reviewers are good enough, so this round is about the lesson.
The c1-skills lesson is clear, but my review found three things I want a lesson reviewer to catch: errors are named but have no simple real example, some parts explain the idea before any example, and I want more detail with real examples at the same difficulty.
I want a lesson reviewer whose checklist checks these, with a fresh context, and that checks every fact against a source.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The c1-skills lesson named misconceptions without a simple real example and sometimes explained before showing an example, so a lesson-reviewer with a fresh context now checks facts against sources, then pedagogy, alignment and overall quality in four separate sections, and the teach skill drafts in drafts/, runs it for at most two passes, and writes the final lesson once.

### Round 6

**Run:** bench/runs/_live/20261119-220458-agent-architecture-m30-r1, teach only

**My thoughts:**

The lesson-reviewer helped: the facts are all correct, and it caught old links, a number that did not match, and definitions that came before the example.
But the lesson is still too short: the length ratio is 0.56, below the 0.6 floor, even though the reviewer itself said the lesson was too short. I want the same difficulty, with more detail added in each part, not new topics.


**What changed:**

- Kind: other
- Files: tutor/.claude/skills/teach/SKILL.md, tutor/.claude/agents/lesson-reviewer.md
- Why: The reviewed lesson was still short (length ratio 0.56) because nothing made the writer fill the time, so the teach skill now sets a floor of 120 words per minute with a way to estimate it and says to add detail at the same difficulty, and the lesson-reviewer flags a lesson below 0.8 of the requested minutes and names where to add detail.

### Round 7

**Run:** bench/runs/_live/20261121-000532-agent-architecture-m30-r1, teach only


**My thoughts:**

The Round 6 change helped: the length ratio went from 0.56 to 0.77, with the same difficulty, and the facts are still all correct. That is good enough, so I am stopping here.


**What changed:**

- Kind: other
- Files: other
- Why: no change; the round only records that Round 6 helped.

## Major review

**Run:** bench/runs/c2-review/TODO

**Live tries:**

TODO

### Lesson

#### Technical correctness and facts

Rating: TODO

TODO

#### Pedagogy

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

#### Overall quality

Rating: TODO

TODO

### Quiz

#### Difficulty

Rating: TODO

TODO

#### Coverage of the lesson's core

Rating: TODO

TODO

#### Wording and possible misreadings

Rating: TODO

TODO

#### Writing quality

Rating: TODO

TODO

#### Alignment with the learning goal

Rating: TODO

TODO

### Feedback

#### Useful

Rating: TODO

TODO

#### Explains enough

Rating: TODO

TODO

#### Personalized to how I like things explained

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
