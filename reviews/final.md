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

**Run:** a live try in tutor/ of /cheatsheet on lesson 0001, which updated tutor/cheatsheets/context-and-memory.html


**My thoughts:**

The Round 4 change helped: /cheatsheet updated the sheet so that "turn", "session" and "setup" are explained in the key terms and every rule has a "because" beside it, so the rules are much clearer than before.
Setting the goal first lets me decide which knowledge is worth learning and which can wait. I want a skill that asks me why I am learning a topic and what I want to be able to do, and writes that into MISSION.md before any lesson.


**What changed:**

- Kind: new skill
- Files: tutor/.claude/skills/mission/SKILL.md
- Why: Lessons started without asking why the learner was learning, so a mission skill now asks up to four short questions about the reason, the specific outcomes, the limits and what to leave out, and writes the answer into MISSION.md in the learner's own words before any lesson.

### Round 6 (optional)

**Run:** TODO

**My thoughts:**

TODO

**What changed:**

- Kind: TODO
- Files: TODO
- Why: TODO

## Major review

**Run:** bench/runs/final/20261122-025700-agent-architecture-m30-r3


**Live tries:**

Live tries are my three learning sessions under Learning sessions below, all on computer-architecture; I did not try anything else with final.


### Lesson

#### Technical correctness and facts
Rating: 5
The bench check agrees: all six key facts are present and correct, with no misconception asserted and no dead links. The lesson draws the line between the model and the program, and the token rule (what is sent, and what is paid for on each call) is stated and worked through.

#### Pedagogy
Rating: 4
Each part leads with the point, then an example, then the detail, and the common mix-ups each have a concrete case. Two things to change: the summary at the start of "Context design" should be shorter, and the definition at the start of the retrieval part should move after its example.

#### Alignment with the learning goal
Rating: 5
The lesson covers what the learner needs, deciding what the agent keeps in its context, what it saves and what it looks up, with the makerspace budget and the design trade-offs. At 4,418 words its length is about right, and the examples and the decision table stay tied to the goal.

#### Overall quality
Rating: 4
The worked example, the decision table and the self-check are solid, but the closing section and the external links are crowded, so it is not yet as clean as the rest.


### Quiz

#### Difficulty
Rating: 4
Question 6 tests applying the idea to a policy and a one-word answer, which is an application test, not harder reasoning than question 5, so the items are at about the same level.

#### Coverage of the lesson's core
Rating: 5
The six items cover the O4 ideas: who decides the next step, the call count of a fixed workflow against an agent, choosing a design for a fixed set of steps, labelling a question with a fixed follow-up, when an agent helps a diagnosis, and who owns a policy step.

#### Wording and possible misreadings
Rating: 4
Question 6 asks "model or the code" and says "Answer with one word", but "code" and "program" mean the same thing, and "The code." would go over one word, so the wording can be read two ways.

#### Writing quality
Rating: 5
The options are about the same length, and the right answer is not always the longest one.

#### Alignment with the learning goal
Rating: 5
The quiz is on O4 and ties to the makerspace's engineering trade-offs, which is what this learner needs now.


### Feedback

#### Useful
Rating: 5
The summary says which item to redo and lists the three things to write for it, and each wrong or partly right item has a clear correction to make.

#### Explains enough
Rating: 5
Each item explains the mechanism and why the answer fails, with concrete examples such as check_calendar and a three-step tool lookup.

#### Personalized to how I like things explained
Rating: 5
Each item gives the verdict first and points to the exact part that is off, with no questions back to me, which matches how I like feedback.


### Tutor

#### Guardrails
Rating: 5
All six replies stay inside the rules: none gives a quiz answer or confirms an option, none leaks a key, and the replies to the off-topic question and the personal-advice question stay general and send the learner back to the course.

#### Personalization
Rating: 5
The replies are direct and plain, give hints before answers, and do not ask the learner questions back, which matches how I like to be talked to.


### Compared with the previous step

final is measured against the baseline on three runs each. The lesson is longer and fills the 30 minutes (length ratio 1.05, against 0.69 for the baseline, and the ranges do not overlap), and the tutor meets more of its probes (0.78, against 0.56; the ranges just touch at 0.67). Every quality check is the same for both, so they only show that nothing broke. The cost is about 2.6 times the baseline ($4.61 against $1.78, 22.5 minutes against 6.0, and 14.7 subagents against none), and most of it is in the teach job.


### What I would do next


The next step is nothing more to add, but the tutor's quiz and grade loops are not worth their cost, so I would cut the quiz reviewer first and check whether the lesson keeps its length without the writer's budgets.


## Learning sessions

### Session 1

**Date:** 2026-11-22

**Topic:** computer-architecture, how a pipeline handles data hazards (stalling and forwarding)

I asked for a 10-minute lesson on how a pipeline handles hazards. The tutor ran its whole pipeline of subagents, planner, references-finder, writer, figure-designer and two reviews, and wrote a lesson, a five-item quiz and a cheat sheet in about 11 minutes. The content was correct, and I thought the process was very good. It checked its sources and used only the two pages that opened. The lesson was about 1,700 words, a little over 10 minutes, and its part titles did not follow the "term: plain explanation" pattern, because the second review ran out of passes.

The quiz suited a beginner well. I answered it and it graded my five answers: it told me right or wrong first, then gave the reason with the numbers, and the grade-reviewer made it fix one word, "ALU", that the lesson never taught. I got all five right, so I did not see how it handles a wrong answer.

The guard worked for real: the tutor tried to copy the key into keys/ with a shell command, the hook blocked it with its message, and the tutor wrote the key with the Write tool instead. It also noticed that my MISSION.md is about agent memory and asked whether this topic belongs to another course.

### Session 2

**Date:** 2026-11-22

**Topic:** computer-architecture, a short quiz on load-use stalls and reordering instructions

I asked for a three-question quiz and answered it, all correct. The grader wrote the grades in about 12 seconds without reading the lesson or the guides, and this time the tutor skipped the grade-reviewer that the grade skill requires, so it checked the grader's draft itself against its own answers. It said it had checked the draft "against the key", but the log shows that the main conversation never read keys/; it only started the grader and wrote its own quiz's key, so the guard held. The feedback was short and direct, right or wrong first and then the cycle count, but because I got everything right I still did not see how it handles a wrong answer. I would change two things in the tutor: make the grade skill always start the grade-reviewer, and make the grader read the lesson before grading.


### Session 3

**Date:** 2026-11-22

**Topic:** computer-architecture, a question beyond my lesson: whether out-of-order execution with register renaming avoids all stalls

I asked a question far above my lesson. The tutor named the wrong premise in its first sentence, "an out-of-order processor with register renaming does not avoid all stalls", then gave a three-instruction example, with a name clash that renaming removes and a real dependency it cannot. It said twice that its sketch and its list of stalls that never go away came from general knowledge and not from a source it had checked, and it offered a short lesson because the question was outside my lesson. It tied the answer to the forwarding I had learned. The answer was a little long for my preference of short replies, with a table and a list of three more stalls. I would change nothing in what it said, only make it shorter.


## Test topics

### computer-architecture
final is better on this topic, because its lesson is longer and fills the time (length ratio 1.00, against 0.60 for the baseline), its quiz agrees with the answer key more often (1.00 against 0.80), and its lesson is more complete. On the tutor's probes it is not better (1 of 6 against 2 of 6), so the gain is in the lesson and the quiz, not in the replies. One run each, so I hold this lightly.

### cooking-basics
final is better, or slightly better, on this topic, because its lesson is closer to the time asked for (length ratio 0.92, against 0.54 for the baseline) and the quiz agrees with the key on both (1.00). The tutor's probes are level (1 of 6 each), so the gain again is in the lesson and the quiz.

