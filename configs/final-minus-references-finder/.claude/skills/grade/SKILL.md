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
Read `FORMATS.md` (the exact shape of `grades/NNNN-sN.json`), `PREFERENCES.md`, `NOTES.md`, the files in `learning-records/`, the quiz in `quizzes/`, the submission in `submissions/`, and the lesson on the quiz's objective if there is one.
Never read `keys/`: a guard blocks it for this conversation, and the `grader` subagent is the one that reads the key.
Then read `.claude/skills/teach/references/GRADING.md`, the rules for verdicts and misconceptions; this skill adds to it, and where the two differ, follow this skill.
Never edit `PREFERENCES.md`, `FORMATS.md` or anything under `.claude/`.

## Steps

1. **Pin down** the quiz and the submission to grade, and the next free names: the draft `drafts/NNNN-sN-grade.json` and the final `grades/NNNN-sN.json`.
2. **Start the `grader` subagent** with the Agent tool, and wait for its report before you go on.
   Its task message names the quiz (`quizzes/NNNN.json`), its key (`keys/NNNN.json`), the submission (`submissions/sN.json`) and the draft file to write; it reads the key, the learner files and `GRADING.md` itself, judges every item, names the misconceptions, writes the feedback and the summary as the sections below describe, and writes the draft.
   You do not judge the items yourself, because you cannot read the key.
3. **Read the draft back** to be sure it exists and is valid JSON with an entry for every quiz item; if it does not, start the grader again once.
4. **Review loop, at most two passes.** Start the `grade-reviewer` subagent with the Agent tool, and wait for its report before you go on.
   Its task message names: the draft grades path, the quiz, its key and the submission, and the files it must read: `PREFERENCES.md`, `NOTES.md` and, when there is one, the lesson in `lessons/` on the quiz's objective.
   Do not tell it how you reasoned.
   - Hand every finding to the `grader` again, in a task message with the draft path and the reviewer's findings, and wait for its report; note in the record any finding it did not fix, and read the draft back after each fix.
   - After a fix, run the reviewer again; stop as soon as its last line is `Verdict: done`, or after the second review, whichever comes first.
5. **Write the final file once:** `grades/NNNN-sN.json`, copied in full from the last draft with the Write tool, exactly as `FORMATS.md` shows, and read it back to check it is valid JSON.
6. **Write the record** to `review-records/NNNN-sN-grade.md`: how many review passes ran, the findings of each pass, and what changed because of each one.
7. **Record** what the grades show: a learning record for real understanding or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`, and an update to `NOTES.md`.
8. **Finish** in the chat with the summary and the one next step.

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
