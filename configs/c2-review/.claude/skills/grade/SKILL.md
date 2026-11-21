---
name: grade
description: Grade the learner's answers to a quiz - a verdict for every item, the misconception it shows, and short, direct feedback that says right or wrong first and then the exact part that was off - written as FORMATS.md describes. Use it whenever the learner hands in a quiz or asks for answers to be graded.
argument-hint: "Which submission should I grade?"
---

# Grade

You grade one submission to one quiz, write the grades file, update the learner's records, and finish with a short summary in the chat.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
When the learner gave a full set of answers in the chat instead of a file, first write them exactly as given to the next `submissions/sN.json`, as `FORMATS.md` shows.
Do what the request asks now, and put any question for the learner at the end of your final message.

## Read first

The current directory is the learner's workspace; every path is relative to it.
Read `FORMATS.md` (the exact shape of `grades/NNNN-sN.json`), `PREFERENCES.md`, `NOTES.md`, the files in `learning-records/`, the quiz in `quizzes/`, its key in `keys/`, the submission in `submissions/`, and the lesson on the quiz's objective if there is one.
Then read `.claude/skills/teach/references/GRADING.md`, the rules for verdicts and misconceptions; this skill adds to it, and where the two differ, follow this skill.
Never edit `PREFERENCES.md`, `FORMATS.md` or anything under `.claude/`.

## Steps

1. **Judge every item**, in the quiz's order, including blank ones: a verdict (`correct`, `partial` or `wrong`) by what the response means, not how it is worded, following `GRADING.md`.
2. **Name the misconception** a response shows, by an id the workspace already uses, or `null`; never invent an id.
3. **Write the feedback** for each item as below.
4. **Draft** the grades to `drafts/NNNN-sN-grade.json`, in the shape `FORMATS.md` shows, with the summary.
   Never write a draft into `grades/`: the bench scores that folder, and it gets the final file only.
   Then read the draft back to be sure it was written and is valid JSON; if the read fails, write it again before going on.
5. **Review loop, at most two passes.** Start the `grade-reviewer` subagent with the Agent tool, and wait for its report before you go on.
   Its task message names: the draft grades path, the quiz, its key and the submission, and the files it must read: `PREFERENCES.md`, `NOTES.md` and, when there is one, the lesson in `lessons/` on the quiz's objective.
   Do not tell it how you reasoned.
   - Fix every finding in the draft, or note in the record why you did not, and read the draft back after each fix.
   - After a fix, run the reviewer again; stop as soon as its last line is `Verdict: done`, or after the second review, whichever comes first.
6. **Write the final file once:** `grades/NNNN-sN.json` from the last draft, exactly as `FORMATS.md` shows, and read it back to check it is valid JSON.
7. **Write the record** to `review-records/NNNN-sN-grade.md`: how many review passes ran, the findings of each pass, and what you changed because of each one.
8. **Record** what the grades show: a learning record for real understanding or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`, and an update to `NOTES.md`.
9. **Finish** in the chat with the summary and the one next step.

## Feedback: the verdict first, then the exact part

Each item's feedback is short, in the tone `PREFERENCES.md` asks for, and opens with the verdict in plain words.
A submitted quiz is being graded, so its items are no longer open: explain each one in full and state the right answer and why.
`PREFERENCES.md` asks for hints and not answers on quiz items the learner is still taking; that rule does not apply to feedback on a graded submission.

- **Correct:** "Right." then the one idea that makes it stick, in a sentence.
- **Partial:** "Partly right." then which part was right, the exact part that was off, and how to fix it, with one simple real example.
- **Wrong:** "Not quite." then the exact part that was wrong, quoting or naming what the learner chose or wrote, the right idea and why it holds, and one simple real example with real numbers or a real case, no harder than the idea itself.
  When a misconception is behind it, name the wrong belief plainly, without blame.

Never end an item's feedback, or the summary, with a question to the learner, and do not turn the explanation into a hint or a puzzle; say what is true and show it with the example.
Point at the one part that was off; do not re-explain the whole topic.

## The summary

Three sentences at most: what the learner has down, the one thing to work on next, and a concrete next step, such as a part of a lesson to reread or an item to redo, stated as an instruction and not as a question.
