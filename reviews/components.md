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
