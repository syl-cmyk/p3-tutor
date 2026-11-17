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
4. **Write** `grades/NNNN-sN.json` exactly as `FORMATS.md` shows, with the summary.
5. **Record** what the grades show: a learning record for real understanding or a misconception to work on, in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`, and an update to `NOTES.md`.
6. **Finish** in the chat with the summary and the one next step.

## Feedback: the verdict first, then the exact part

Each item's feedback is two or three short sentences, in the tone `PREFERENCES.md` asks for, and opens with the verdict in plain words.

- **Correct:** "Right." then the one idea that makes it stick, in a sentence.
- **Partial:** "Partly right." then which part was right, and the exact part that was off and how to fix it.
- **Wrong:** "Not quite." then the exact part that was wrong, quoting or naming what the learner chose or wrote, and the right idea in plain words, with a short concrete case when it helps.
  When a misconception is behind it, name the wrong belief plainly, without blame.

Point at the one part that was off; do not re-explain the whole topic.

## The summary

Three sentences at most: what the learner has down, the one thing to work on next, and a concrete next step, such as a part of a lesson to reread or a question to try.
