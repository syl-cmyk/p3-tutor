# Components

One entry for every skill and every subagent you built, from `c1-skills` to `final`, including the ones you dropped, even one you took out again before any snapshot.
The heading is the skill's folder name or the subagent's `name` from its frontmatter, and `reviews/README.md` says what each field holds.
Replace the empty entry at the bottom with your first component, and copy it for each one after that.
Claude Code may fill in Kind, Step added, and With and without; Purpose, Review and Kept in final are yours.

<!--
An example of a finished entry:

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: My c1 review found two quiz items that could be read two ways (q2 and q4) and one whose correct option repeated the stem; a reviewer with a fresh context reads the draft the way a learner will, which the quiz skill writing its own items cannot do, so it is a subagent and not a step in the skill.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it, q2 asked which design "is better" with no criterion; with it, every stem names its criterion and the reviewer's record shows two items flagged and fixed in one pass, for about 0.6M more tokens per quiz, which I think a quiz is worth, because a misread item teaches the wrong thing.
- Kept in final: yes
-->

### teach

- Kind: skill
- Step added: c1-skills
- Purpose: Writes the lesson. My rules make it use paragraphs of at most three sentences and at most six headings, open each part with its main point, give one example per part, and use only words the lesson has already explained.
- With and without: reviews/c1-skills.md, Round 1 (without) and Round 2 (with)
- Review: Without these rules the lesson had 10 headings; with them it had 6. The lesson came out a bit short, and teach cost more ($0.62 to $0.83 per run), but it explains things more clearly.
- Kept in final: yes

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: Answers the learner in the chat. Its hints must fit every option alike so they never point to a quiz answer, and a question beyond the course gets one or two plain sentences before it brings the learner back to the project.
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: Without it, behavior met was 0.50 and the hints in tutor-p01 and tutor-p02 pointed to the answer; with it, behavior met was 0.83 and those were fixed, along with tutor-p05. The analogy in tutor-p06 got worse, but tutor also got cheaper ($0.64 to $0.41 per run), so it was worth it.
- Kept in final: yes

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: Writes the quiz and its key. It keeps a mix of item types and keeps every stem to one or two sentences.
- With and without: reviews/c1-skills.md, Round 5 (without) and Round 6 (with)
- Review: Without it, the stems were longer; with it, they got shorter, q1 is one sentence, and key agreement stayed at 1.00. It costs a little less ($0.19 to $0.16 per run), but it still does not cover all the lesson's ideas evenly.
- Kept in final: yes

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: Grades the learner's answers. Each item's feedback says right or wrong first, then the exact part that was wrong, in two or three sentences.
- With and without: reviews/c1-skills.md, Round 6 (without) and Round 7 (with)
- Review: Grading was already correct without it, and it stayed correct with it (verdict agreement 1.00). The feedback says right or wrong first, as I wanted, but it still needs simpler real examples to explain enough. It costs about the same ($0.33 to $0.30 per run).
- Kept in final: yes

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Checks a draft quiz with a fresh context against nine checks: coverage spread over the objective's ideas, rising difficulty, every term defined, short stems, one defensible answer, no giveaways, real distractors, correct numbers and a mix of item types.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it the quiz cost $0.16, with it $0.49, about three times as much. Its fixes, such as turning q2 into a hybrid case and replacing weak distractors, did not make the quiz harder: my Difficulty rating stayed at 4, and key agreement stayed at 1.00. I do not think it was worth the cost.
- Kept in final: yes

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Checks a draft grades file with a fresh context against nine checks: the verdicts re-judged, real misconception ids, the verdict first, the exact wrong part named, a full reason with one simple real example, wording a new learner can follow, short feedback, a fit with my preferences, and a concrete next step.
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with)
- Review: Without it grading cost $0.30, with it $0.84, about 2.8 times as much. Grading was already correct (verdict agreement 1.00 both times), and with it the feedback got real examples and no closing questions: Useful rose from 3 to 5 and Explains enough from 3 to 4. It still does not explain what the model's output looks like in q2, so I do not think it was worth the cost.
- Kept in final: yes

### lesson-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Checks a draft lesson with a fresh context in four separate sections: facts checked against sources with web search, pedagogy, alignment with the objective and my mission, and overall quality. It also estimates the lesson's length and names where to add detail.
- With and without: reviews/c2-review.md, Round 5 (without) and Round 6 (with)
- Review: Without it the lesson cost $0.83 with a length ratio of 0.60, and with it $1.52 and 0.87, about 1.8 times as much. It corrected facts (a claim cited to the wrong page, arithmetic that did not match the example), added real cases to the misconceptions and made the lesson longer, and my Technical correctness and Pedagogy ratings both rose from 4 to 5. I think it was worth the cost, though the length change also comes from the length rule I added in Round 6.
- Kept in final: yes

### lesson-planner

- Kind: subagent
- Step added: c3-split
- Purpose: Plans the lesson before any writing: the title and the win in general terms about the concept, up to six parts each with a technical-term title, a key sentence, a word budget, one worked example and the misconceptions with real examples, plus the figures and the sources.
- With and without: (leave as it is)
- Review: Without it the lesson's titles were casual and its length fell short (length ratio 0.76); with it the titles became technical terms with a plain explanation and the plan fixed the word budgets. I think it was worth the cost.
- Kept in final: yes

### lesson-writer

- Kind: subagent
- Step added: c3-split
- Purpose: Writes the draft of the lesson as a self-contained HTML page from the plan, part by part, to each word budget, and reports its words against the budget.
- With and without: reviews/c3-split.md, Round 3 (without) and Round 4 (with)
- Review: Without it the lesson was a little short (length ratio 0.76); with it the ratio went to 0.95 and then 0.90, for about $0.9 more on the teach scenario. I think it was worth it.
- Kept in final: yes

### figure-designer

- Kind: subagent
- Step added: c3-split
- Purpose: Draws every figure as inline SVG to scale, checks each bar and label against the numbers in the lesson, labels each box in plain words with the reason beside each arrow, and places each figure after its idea.
- With and without: reviews/c3-split.md, Round 4 (without) and Round 5 (with)
- Review: Without it the reviewers kept flagging figures whose bars did not match the text; with it they stopped, and the lesson had more figures (two, then five), for about $0.1 more. I think it was worth it.
- Kept in final: yes

### references-finder

- Kind: subagent
- Step added: c3-split
- Purpose: Opens every source in the plan, checks that the link works and that the page supports the claim it is cited for, and writes drafts/sources.md for the writer and the reviewer.
- With and without: reviews/c3-split.md, Round 6 (without) and Round 7 (with)
- Review: Without it the reviewers kept finding claims cited to the wrong page and links that looked dead; with it every source was marked supported, partly supported or not found, for about $0.26 more. The ablation final-minus-references-finder tests whether it matters.
- Kept in final: yes

### grader

- Kind: subagent
- Step added: final
- Purpose: Grades one submission against the answer key and writes the draft grades with feedback, and is the only agent besides the grade-reviewer that the guard lets read keys/.
- With and without: reviews/final.md, Round 1 (without); the with is the grade-s1 live run in bench/runs/_live/20261122-012805-agent-architecture-m30-r1, where the grader and the reviewers read the key and the main conversation did not
- Review: Without it the grade skill read the key in the main conversation, which the guard blocks; with it grading stayed correct (verdict agreement 1.00) and the main conversation never read a key. It is needed for the guard, so it is kept.
- Kept in final: yes

### cheatsheet

- Kind: skill
- Step added: final
- Purpose: Writes a one-page cheat sheet on a lesson or a topic, with the key terms, the rules each with its reason, one worked example and the common mistakes, when I start it by name.
- With and without: reviews/final.md, Round 3 (without) and Round 4 (with)
- Review: Without it the teach skill wrote a cheat sheet only sometimes; with it I got a one-page sheet of about 390 words, and after Round 4 its terms were explained and every rule had a "because". I think it is worth keeping.
- Kept in final: yes

### mission

- Kind: skill
- Step added: final
- Purpose: Asks up to four short questions about why I am learning a topic, what I want to be able to do and what limits me, and writes the answer into MISSION.md before any lesson.
- With and without: reviews/final.md, Round 5 (without) and Round 6 (with)
- Review: I ran it once in tutor/: it noticed that MISSION.md already existed and asked whether to replace it or keep both, then asked four short questions, each with an example answer, and waited for my answers instead of making any up. The bench has no mission scenario, so I could not measure it, but it did what the skill says, and it is the sixth skill the project needs.
- Kept in final: yes
