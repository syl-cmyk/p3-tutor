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

**Run:** bench/runs/_live/20261121-202853-agent-architecture-m30-r1, teach only


**My thoughts:**

The planner helped a little: the plan is complete, with a win, a running example and sources, and the lesson has six parts and the right facts.
But the lesson still reads as an explanation and not as a professional treatment of context and memory. The lesson title, "Context and memory: what your assistant sees, keeps and finds", and its opening promise, that by the end I can say what the makerspace assistant keeps at each step, tie the whole concept to one project instead of stating it in general. The part titles, such as "Why more is not better" and "What stays between steps", are still casual.
I want titles in the course's own terms, such as "Context window" and "Context persistence across sessions", each with a short plain explanation, and the concept stated in general first, with the makerspace assistant only as the example.


**What changed:**

- Kind: other
- Files: tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md, tutor/.claude/agents/lesson-reviewer.md
- Why: The planner's lesson still had casual titles and tied the whole concept to the makerspace assistant, so the planner now writes a technical-term title with a plain explanation for the lesson and every part and states the win in general terms, the teach skill uses those titles word for word, and the lesson-reviewer flags any casual or project-specific title.

### Round 3

**Run:** bench/runs/_live/20261121-204609-agent-architecture-m30-r1, teach only


**My thoughts:**

The Round 2 change helped: the titles are now technical terms with a plain explanation, and the lesson is very clear.
The lesson is still a little short: the length ratio is 0.76. The planner gives each part a word budget, but nothing checks that the writing meets it.
I want a writer subagent that takes drafts/plan.md and writes the lesson part by part to each word budget, so the length and the detail come from the plan.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/lesson-writer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The lesson was still short (length ratio 0.76) because nothing held the writing to the planner's word budgets, so a lesson-writer subagent now writes drafts/NNNN-<slug>.html part by part from drafts/plan.md to each budget and reports its words against them, and the teach skill starts it after the planner and asks for more detail when the total is under 120 words per minute.

### Round 4

**Run:** bench/runs/_live/20261121-210114-agent-architecture-m30-r1, teach only

**My thoughts:**

The Round 3 change helped: the length ratio went from 0.76 to 0.95 and the lesson is very good now.
One thing still goes wrong in the reviewers' records: the figures. They flagged bars that did not match the numbers in the text, a figure that was not to scale and a figure shown before the idea it needs.
I want a figure-designer subagent that draws the figures the plan names, checks every bar and label against the numbers in the lesson, and places each figure after the idea it shows.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/figure-designer.md, tutor/.claude/agents/lesson-writer.md, tutor/.claude/agents/lesson-planner.md, tutor/.claude/skills/teach/SKILL.md
- Why: The reviewers kept finding figures whose bars did not match the text, were not to scale or came before their idea, so a figure-designer subagent now draws every figure as inline SVG to scale, checks each number against the text and places each figure after its idea, the planner lists the figures with their numbers, the writer leaves placeholders, and the teach skill runs the designer between the writer and the reviewers.

### Round 5

**Run:** bench/runs/_live/20261121-212122-agent-architecture-m30-r1, teach only


**My thoughts:**

The figure-designer fixed the figures I complained about: in Figure A every bar and number matches the text, and the reviewers stopped flagging figures.
Figure B still explains too little. The arrow "read on demand" is only a label, and it does not say why a note is read on demand: everything in the window is resent and paid for on every call, so only what is needed should be loaded. The caption "Session 2 starts with 0 tokens of history" also reads as if session 2 knows nothing, although the store keeps Maya's note and session 2 reads it.
I want figures that label each box in plain words (window is what is being used now, store is what is saved) and add the reason next to the arrow.


**What changed:**

- Kind: modified skill
- Files: tutor/.claude/agents/figure-designer.md, tutor/.claude/agents/lesson-planner.md
- Why: The window and store figure labelled its arrows without saying why and a caption could be read as session 2 knowing nothing, so the figure-designer now labels every box in plain words, puts the reason next to every arrow from the lesson's text and completes any label a beginner could misread, and the planner lists those labels and reasons for each figure.

### Round 6

**Run:** bench/runs/_live/20261121-220422-agent-architecture-m30-r1, teach only


**My thoughts:**

The Round 5 change helped: the lesson and its figures are much more professional now, and that is enough for the text and the figures.
The reviewers' records still keep finding problems with sources: a claim cited to the wrong page, a link that looked dead, a description they could not confirm, and claims stronger than the document says.
I want a references-finder subagent that, before the lesson is written, opens each source the plan lists, checks that the link works and that the page supports the claim it is cited for, and writes drafts/sources.md for the writer and the reviewers to use.


**What changed:**

- Kind: new subagent
- Files: tutor/.claude/agents/references-finder.md, tutor/.claude/agents/lesson-writer.md, tutor/.claude/agents/lesson-reviewer.md, tutor/.claude/skills/teach/SKILL.md
- Why: The reviewers kept finding claims cited to the wrong page, dead-looking links and descriptions they could not confirm, so a references-finder subagent now opens every source in the plan, checks the link and that the page supports the claim, and writes drafts/sources.md, the teach skill runs it between the planner and the writer, the writer cites only what it marks as supported, and the lesson-reviewer starts its fact-check from that file.

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
