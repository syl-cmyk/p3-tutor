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
- Kept in final: TODO

### tutor

- Kind: skill
- Step added: c1-skills
- Purpose: Answers the learner in the chat. Its hints must fit every option alike so they never point to a quiz answer, and a question beyond the course gets one or two plain sentences before it brings the learner back to the project.
- With and without: reviews/c1-skills.md, Round 4 (without) and Round 5 (with)
- Review: Without it, behavior met was 0.50 and the hints in tutor-p01 and tutor-p02 pointed to the answer; with it, behavior met was 0.83 and those were fixed, along with tutor-p05. The analogy in tutor-p06 got worse, but tutor also got cheaper ($0.64 to $0.41 per run), so it was worth it.
- Kept in final: TODO

### quiz

- Kind: skill
- Step added: c1-skills
- Purpose: Writes the quiz and its key. It keeps a mix of item types and keeps every stem to one or two sentences.
- With and without: reviews/c1-skills.md, Round 5 (without) and Round 6 (with)
- Review: Without it, the stems were longer; with it, they got shorter, q1 is one sentence, and key agreement stayed at 1.00. It costs a little less ($0.19 to $0.16 per run), but it still does not cover all the lesson's ideas evenly.
- Kept in final: TODO

### grade

- Kind: skill
- Step added: c1-skills
- Purpose: Grades the learner's answers. Each item's feedback says right or wrong first, then the exact part that was wrong, in two or three sentences.
- With and without: reviews/c1-skills.md, Round 6 (without) and Round 7 (with)
- Review: Grading was already correct without it, and it stayed correct with it (verdict agreement 1.00). The feedback says right or wrong first, as I wanted, but it still needs simpler real examples to explain enough. It costs about the same ($0.33 to $0.30 per run).
- Kept in final: TODO

### quiz-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Checks a draft quiz with a fresh context against nine checks: coverage spread over the objective's ideas, rising difficulty, every term defined, short stems, one defensible answer, no giveaways, real distractors, correct numbers and a mix of item types.
- With and without: reviews/c2-review.md, Round 1 (without) and Round 2 (with)
- Review: Without it the quiz cost $0.16, with it $0.49, about three times as much. Its fixes, such as turning q2 into a hybrid case and replacing weak distractors, did not make the quiz harder: my Difficulty rating stayed at 4, and key agreement stayed at 1.00. I do not think it was worth the cost.
- Kept in final: TODO

### grade-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Checks a draft grades file with a fresh context against nine checks: the verdicts re-judged, real misconception ids, the verdict first, the exact wrong part named, a full reason with one simple real example, wording a new learner can follow, short feedback, a fit with my preferences, and a concrete next step.
- With and without: reviews/c2-review.md, Round 3 (without) and Round 4 (with)
- Review: Without it grading cost $0.30, with it $0.84, about 2.8 times as much. Grading was already correct (verdict agreement 1.00 both times), and with it the feedback got real examples and no closing questions: Useful rose from 3 to 5 and Explains enough from 3 to 4. It still does not explain what the model's output looks like in q2, so I do not think it was worth the cost.
- Kept in final: TODO

### lesson-reviewer

- Kind: subagent
- Step added: c2-review
- Purpose: Checks a draft lesson with a fresh context in four separate sections: facts checked against sources with web search, pedagogy, alignment with the objective and my mission, and overall quality. It also estimates the lesson's length and names where to add detail.
- With and without: reviews/c2-review.md, Round 5 (without) and Round 6 (with)
- Review: Without it the lesson cost $0.83 with a length ratio of 0.60, and with it $1.52 and 0.87, about 1.8 times as much. It corrected facts (a claim cited to the wrong page, arithmetic that did not match the example), added real cases to the misconceptions and made the lesson longer, and my Technical correctness and Pedagogy ratings both rose from 4 to 5. I think it was worth the cost, though the length change also comes from the length rule I added in Round 6.
- Kept in final: TODO

### lesson-planner

- Kind: subagent
- Step added: c3-split
- Purpose: TODO
- With and without: reviews/c3-split.md, Round 1 (without) and Round 2 (with)
- Review: TODO
- Kept in final: TODO
