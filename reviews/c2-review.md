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

**Run:** bench/runs/c2-review/20261121-003424-agent-architecture-m30-r1

**Live tries:**

not tried for this step

### Lesson

#### Technical correctness and facts

Rating: 5

The bench check agrees: every key fact in the lesson is present and correct (teach facts 1.00), with no misconception asserted and no dead links.


#### Pedagogy

Rating: 5

Every part opens with its key sentence, then explains the idea with examples placed in the middle, which is the structure I asked for. It also fixes my c1 problem that misconceptions had no example: they now have simple real cases.


#### Alignment with the learning goal

Rating: 5

The lesson covers what the learner needs: what stays in the context between steps, what is saved between sessions as notes, and how retrieval finds the right pages in a long manual. The last part practices sorting facts among the three, which is the decision the learner has to make.


#### Overall quality

Rating: 4

The lesson is clear, longer now (length ratio 0.87), and keeps the same difficulty. One small thing I would change: the part titles, such as "What is kept between sessions", sound too casual. I would use the course's technical terms, such as "Context persistence across sessions", with a short plain explanation next to them.


### Quiz

#### Difficulty

Rating: 4

The items now go from definition questions (q1, q2) to application (q3, q5) and a cost calculation (q4), so the difficulty rises a little. I would still like one harder item that mixes two ideas, such as a cost question where one part of the request is a fixed workflow and the rest is an agent.


#### Coverage of the lesson's core

Rating: 5

In the bench the quiz is only on objective O4, and the six items spread over its ideas: the definition, who owns the control flow, what a fixed workflow does with a new request, cost, which request suits an agent, and why booking fits a fixed workflow. Nothing in O4 is left out. My c1 rating of 3 was about the quiz not covering the lesson, which the bench does not ask for.


#### Wording and possible misreadings

Rating: 5

The wording is clear and I could tell what each item was asking. The bench found no ambiguous items and no wrong keys, and q2 now explains "control flow" as who decides which step comes next, so no term is left undefined.


#### Writing quality

Rating: 5

The options in each item are about the same length, and the correct answer is not always the longest one, so nothing gives it away. The quiz also mixes item types: four multiple choice, one numeric and one short answer.


#### Alignment with the learning goal

Rating: 5

The quiz is about what this learner actually needs: telling a workflow from an agent by who owns the control flow, and when a fixed workflow is the better choice, all in the makerspace booking assistant. In the bench the quiz is on objective O4 while the lesson is on O3, which is how the bench is set up and not a problem of the quiz.


### Feedback

#### Useful

Rating: 5

The feedback is useful: for q4 it says the answer 4 is right, names the wrong part (the model does not run the tools, the program does), and counts the calls, 1 for the question plus 1 for each of the three results. The summary ends with one clear next step.


#### Explains enough

Rating: 4

The feedback names the wrong part and gives a real example, but it is still not detailed enough. For q2 it says the model "outputs a request like check_calendar(machine="laser cutter", date="tomorrow")" without saying that this line is just text the model writes, which the program then reads and runs. A new learner can take it as code the model runs itself. I want the feedback to say this step by step, with the model's text and the program's action shown on separate lines.


#### Personalized to how I like things explained

Rating: 5

The feedback matches how I like feedback: it says right or wrong first, points to the exact part that was wrong, and gives a simple real example, without asking me a question or re-explaining the whole topic.


### Compared with the previous step

The c2-review reviewers helped. In the lesson, the misconceptions now have simple real examples, every part opens with its key sentence, and the lesson is longer (length ratio 0.60 to 0.87) at the same difficulty. In the feedback, the examples are real and there are no questions left at the end. The quiz stays on O4 and its items are more spread out. The cost is high: a full run went from $1.70 to $3.31 and from 6.2 to 16.9 minutes.


### What the next step should fix

- The part titles sound too casual, such as "What is kept between sessions". I want titles in the course's technical terms, with a short plain explanation next to them.
- Some concepts can still have more detail, at the same difficulty.
- The review is not clean: the lesson's second pass still said "revise", and the last fixes were never reviewed again.
