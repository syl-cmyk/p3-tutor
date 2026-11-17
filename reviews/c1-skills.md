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

## Major review

**Run:** bench/runs/c1-skills/TODO

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

### Tutor

#### Guardrails

Rating: TODO

TODO

#### Personalization

Rating: TODO

TODO

### Compared with the previous step

TODO

### What the next step should fix

TODO
