# Reviews: c3-split

Your quick rounds while you split up the teach job, and then the major review of `c3-split`.
Add one subagent of the teach pipeline per round, so the run before it shows the lesson without it and the run after it shows the lesson with it.
The major review covers the lesson only, and its previous step is `c2-review`.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/c2-review/20261121-003424-agent-architecture-m30-r1, the c2-review full run, lesson only

**My thoughts:**

The c2-review lesson is clear and has the right length now, but my review found three things I want the split to fix: the part titles sound too casual, some concepts could have more detail at the same difficulty, and the review is not clean because the last fixes were never reviewed again.
I want a planner subagent that plans the lesson before any writing: the sections in order, a title for each in the course's technical terms with a short plain explanation, a word budget for each part, and the example it uses, so every part has enough detail.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson's titles were too casual and some parts lacked detail because nothing planned the lesson before it was written, so a lesson-planner subagent now finds the sources and writes drafts/plan.md with technical titles and plain explanations, a key sentence, a word budget and an example for each part, and the teach skill drafts the lesson from that plan.

### Round 2

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

## Major review

**Run:** bench/runs/c3-split/TODO

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

### Compared with the previous step

TODO

### What the next step should fix

TODO
