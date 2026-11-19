# Reviews: c1-skills

Your quick rounds while you build `c1-skills`, and then its major review, once you have snapshotted it and made its full run.
In this step no round adds a subagent, because subagents arrive in `c2-review` and `c3-split`: a round changes or adds a skill, or makes another change the skills need, such as an allow rule (Kind `other`).
Your first round can start from the tutor as it ships, so the baseline is the output without your first change.
The major review covers all four jobs, and its previous step is `c0-baseline`, so compare with your baseline runs.
What it finds becomes the checklists of your reviewer subagents in `c2-review`, so be specific.
`reviews/README.md` says how to write each part.
You write your thoughts, ratings and feedback; Claude Code writes only the What changed part of each round.
Keep every heading as it is, because `p3 check` reads them, and add a round by copying the last one with its marker lines.

## Quick rounds

### Round 1

**Run:** bench/runs/_live/20261117-184442-agent-architecture-m30-r1, a quick run

**My thoughts:**

The step-by-step examples (student asks → model calls a tool → result comes back → model replies) were good and easy to follow; keep them.
The lesson is not as short as my preferences ask: it has 10 sections and long paragraphs.
The tone is too formal, not casual like a friend. For example: "Anthropic describes keeping "lightweight identifiers" such as file paths or queries and loading data with tools only when needed."
The quiz was fine; I got 4 of 6 and the questions were clear.
I want shorter lessons with short paragraphs and a casual tone.


**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/references/LESSONS.md
- Why: The lesson had 10 sections, long paragraphs and a formal voice that narrated its sources, so teach's lesson guide now asks for a casual voice, paragraphs of at most three sentences, at most six headed parts, and a step-by-step trace for every main idea, which these thoughts wanted kept.

### Round 2

**Run:** bench/runs/_live/20261117-191248-agent-architecture-m30-r1, teach only

**My thoughts:**

The change helped a little: 6 headings instead of 10.
What worked: the call 1, 2, 3 example, showing that every call resends the whole conversation so the cost grows. The retrieval trace (student asks, search_manuals, three sections come back, answer) was good too.
What did not: the "worked example: what you pay" part lost me. The token arithmetic is too hard, and once I lost it I could not read the rest.
The "what is kept between steps" part still reads like a manual: three fixes, each with "Anthropic says ...".
I did not know what the "check yourself" box was for, and its question did not fit the section above it.
Overall the lesson feels scattered. I want every section to open with one or two plain sentences that give me the point at a glance, before any numbers or details, so each part clicks the way a step-by-step explanation does.

**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/references/LESSONS.md
- Why: The lesson felt scattered and lost the learner in its details, so teach's lesson guide now has every headed part open with one or two plain sentences that give its point before any numbers or sources, and those openers, read in order, tell the lesson as a chain of small steps.

### Round 3

**Run:** bench/runs/_live/20261117-195628-agent-architecture-m30-r1, teach only

**My thoughts:**

The change helped: every part now opens with a plain sentence that gives its point, and I could follow most of the lesson.
But the last part ("Worked example, practice, summary") lost me. It uses "three homes" as if I already knew it, and it mixes two different examples, sorting four items and then a token cost calculation, in one part.
I want each worked example to use only ideas the lesson already explained, and one example per part.


**What changed:**

- Kind: modified skill
- Files: tutor/.claude/skills/teach/references/LESSONS.md
- Why: The last part used "three homes" before explaining it and packed a sorting example and a cost calculation into one part, so teach's lesson guide now builds every worked example only from ideas already explained and gives each part one example, with a second idea getting its own part.

### Round 4

**Run:** bench/runs/_live/20261117-202706-agent-architecture-m30-r1, tutor-p01 to tutor-p06


**My thoughts:**

The lesson changes from Round 3 helped, and the lesson is good now, so this round is about the tutor job.
The tutor never gives the letter, which is good, but its hints point to the answer anyway. In p01 it asks what changes "at the point where the loop decides to stop", and in p02 it says "It's a language model, so it can only write text", which rules out options a and d.
When a question goes beyond the course (p05, deriving PPO), it goes too deep with formulas instead of first pulling me back to my project.
I want a tutor skill whose hints fit every option equally, and that answers an off-topic question in one or two plain sentences, then brings me back to my project.


**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/tutor/SKILL.md
- Why: The tutor job still ran inside /teach, whose hints in p01 and p02 pointed to the answer and which met p05 with PPO math, so a tutor skill of its own now tests every hint against each option and drops any topic fact the item tests, and answers a question beyond the course in one or two plain sentences before bringing the learner back to their mission.

### Round 5

**Run:** TODbench/runs/_live/20261117-204150-agent-architecture-m30-r1, quiz only


**My thoughts:**

The tutor skill helped: behavior met went from 0.50 to 0.83, and the hints in p01 and p02 no longer point to an answer. p06 got worse, though: the new analogy has no one who actually carries out the request.
The quiz is fine: clear questions and a mix of types (four mcq, one numeric, one short).
I want a quiz skill of its own that keeps this quality, with shorter stems, one or two sentences each.

**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/quiz/SKILL.md
- Why: The quiz was fine but still came from /teach, so a quiz skill of its own keeps the clear items and the mix of types and caps every stem at one or two short sentences, as these thoughts ask.

### Round 6

**Run:** bench/runs/_live/20261117-204711-agent-architecture-m30-r1, quiz, grade-s1 and grade-s2


**My thoughts:**

The quiz skill helped: stems are shorter, q1 is one sentence, and key agreement stayed at 1.00.
Grading from /teach is already good: all 12 verdicts agree, and the feedback says plainly what part was wrong, like q2 in s1.
I want a grade skill of its own that keeps this: a straight right or wrong first, then the exact part that was wrong, in two or three sentences.


**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/grade/SKILL.md
- Why: Grading was already good but still came from /teach, so a grade skill of its own keeps the verdicts and opens every item's feedback with a plain right or wrong, then names the exact part that was off in two or three sentences, as these thoughts ask.

## Major review

**Run:** bench/runs/c1-skills/20261117-220110-agent-architecture-m30-r1

**Live tries:**

Live try on 2026-11-19, tutor in tutor/, quiz 0001 on context and memory.
The grading is direct: each item says right or wrong first, then why. The quiz is fairly easy, but I want the difficulty to rise step by step. There are a few examples, but I would like one short example of what goes into CLAUDE.md, for item 3. Item 2 uses the word "setup" without explaining it, so I did not know what to count.


### Lesson

#### Technical correctness and facts

Rating: 4

Misconceptions are named but never shown with a simple real example. A short numeric case, worked through step by step, would make the wrong idea and the correction click.


#### Pedagogy

Rating: 4

After each explanation there are examples and a quiz to try yourself, which is the right order. But some parts explain the idea before any example, and I could not follow those until I reached the example.


#### Alignment with the learning goal

Rating: 5

The lesson explains what to keep in the context and what to leave out: it only brings in the few passages a question needs, not the whole manual. The worked example makes it concrete, with about 900 tokens fetched instead of 12,000.


#### Overall quality

Rating: 4

Good overall, but short: the lesson sits right at the low end of the requested length (ratio 0.60). I would like more detail in the places where an idea is only named, such as the misconceptions and the steps for what stays between steps.


### Quiz

#### Difficulty

Rating: 4

The quiz is clear, but most items sit at the same level, asking which label fits a description. I want one harder item that applies the same idea to a new case, using only what the lesson explains, so the learner has to reason rather than match a label.


#### Coverage of the lesson's core

Rating: 3

Almost every item asks about workflow versus agent. Nothing tests what stays in the context or retrieval, which are the lesson's main points. I want the quiz spread across the concepts so each one gets its share of questions.


#### Wording and possible misreadings

Rating: 5

The stems are short and each item asks one thing, so it is always clear what the question wants.


#### Writing quality

Rating: 5

The quiz mixes item types: four multiple choice, one numeric and one short answer, so it checks recall, calculation and explanation, not just picking an option.



#### Alignment with the learning goal

Rating: 3

The quiz tests the learning goal only in part. Almost every item is about workflow versus agent, so it checks that goal well, but it never checks what goes into the context, which is the other main goal.


### Feedback

#### Useful

Rating: 3

The feedback names the mistake, but the explanation is hard to follow. For q2, the sentence about the model writing a request is more complicated than it needs to be, so I can't always use it to fix the error.


#### Explains enough

Rating: 3

The feedback gives the reason, but it needs more simple examples with real data, one short concrete case per item. A life example can help a little, but the real data example should come first.


#### Personalized to how I like things explained

Rating: 5

The feedback opens with a direct "Right." or "Not quite.", then says what was wrong, which matches how I like feedback.


### Tutor

#### Guardrails

Rating: 4

p06 uses an everyday analogy, which fits "no code", but it ends without a simple real example. I want the analogy followed by one small concrete case with real data, such as one tool call with its real result.


#### Personalization

Rating: 4

The tutor gives explanations and follows the tone I asked for, but it still misses the right difficulty for someone new to the topic. The examples are sometimes too hard, so I could not follow them.


### Compared with the previous step

The tutor skill improved the tutor: behavior met went from 0.56 to 0.83, and the cost is about the same. The lesson got shorter, from a length ratio of 0.69 to 0.60.


### What the next step should fix

The next step should fix the quiz: it should test what goes into the context and retrieval, not only workflow versus agent.

