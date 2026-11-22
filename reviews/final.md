# Reviews: final

Your review of `final`: optional quick rounds, its major review, your three learning sessions, and your review of the two test topics.
Quick rounds are optional here; use one for each component that `final` adds, such as a grader subagent, so its inventory entry has its with and without.
`p3 check` ignores an optional round you leave untouched.
The major review covers all four jobs on one of the three runs of `final`, and its previous step is `c3-split`; for the quiz and the feedback, which `c3-split` did not review, compare with `c2-review`, and for the tutor with `c1-skills`.
Its live tries are your three learning sessions, all on one of your two test topics, written up under Learning sessions below, so its Live tries line points at them.
Hold the sessions on `tutor/` as you snapshotted `final`, and note what they make you want to change instead of changing it.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1 (optional)

**Run:** bench/runs/c2-review/20261121-003424-agent-architecture-m30-r1, grade-s1 and grade-s2


**My thoughts:**

The key guard is about to keep keys/ away from the main conversation, so /grade can no longer read the key where it runs now. I want grading done by a grader subagent that reads the key, the quiz and the submission, writes the grades, and returns its report, and the grade skill should start it and wait for the report. Only the grader and the grade-reviewer may read keys/.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/grader.md, tutor/.claude/skills/grade/SKILL.md, tutor/.claude/skills/quiz/SKILL.md, tutor/.claude/settings.json
- Why: The key guard keeps keys/ away from the main conversation, where /grade read the key, so a grader subagent that the guard allows now judges every item and writes the draft grades, the grade skill starts it and the grade-reviewer and never reads a key, the quiz skill no longer reads earlier keys, and the guard hook is registered in tutor/.claude/settings.json with onFailure block.

### Round 2 (optional)

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

### Round 3 (optional)

**Run:** bench/runs/_live/20261121-212122-agent-architecture-m30-r1, teach only, whose cheat sheet came from the teach skill

**My thoughts:**

I cannot relearn everything from scratch every time. A one-page cheat sheet for each lesson cuts the time I spend repeating what I already learned, so I can keep my effort for the problems that really need thinking. Today the teach skill only writes a cheat sheet sometimes, when it decides a lesson holds something worth looking up, and it is not something I can ask for on its own.
I want a cheatsheet skill that I can start by name on any lesson or topic and that always writes a one-page cheat sheet to cheatsheets/, with the key terms, the formulas or steps, and one worked example.


**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/cheatsheet/SKILL.md, tutor/.claude/skills/teach/SKILL.md
- Why: The teach skill wrote a cheat sheet only sometimes and it could not be asked for by name, so a cheatsheet skill now writes a one-page cheat sheet on any lesson or topic to cheatsheets/ with the key terms, the steps, one worked example and the common mistakes, and the teach skill starts it instead of writing the sheet itself.

### Round 4 (optional)

**Run:** a live try in tutor/ of /cheatsheet on lesson 0001, which wrote tutor/cheatsheets/context-and-memory.html


**My thoughts:**

The Round 3 change helped a little: /cheatsheet wrote a one-page sheet of 319 words with the key terms, the rules, a worked example and the common mistakes.
But the sheet is only so-so, because its rules are less clear than they could be. They are stated in a compressed way, such as "The window is re-read in full on every turn" and "Total tokens = setup + loaded files + the whole chat", and the word "setup" is never explained. I want each rule as one short plain sentence, every term explained where it first appears, and a short reason beside each rule.


**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/cheatsheet/SKILL.md
- Why: The cheat sheet's rules were compressed and used the word "setup" without explaining it, so the cheatsheet skill now orders the key terms by what the rules need, explains every word a beginner could not know, and writes each rule as one short plain sentence with its reason beside it.

### Round 5 (optional)

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

### Round 6 (optional)

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

## Major review

**Run:** bench/runs/final/TODO

**Live tries:**

TODO: one line that points at your three learning sessions under Learning sessions below, and names anything else you tried with `final`.

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

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What I would do next

TODO

## Learning sessions

### Session 1

**Date:** TODO

**Topic:** TODO

TODO

### Session 2

**Date:** TODO

**Topic:** TODO

TODO

### Session 3

**Date:** TODO

**Topic:** TODO

TODO

## Test topics

### TODO: your first test topic's id

TODO

### TODO: your second test topic's id

TODO
