---
name: quiz
description: Write a quiz and its answer key on one objective for this learner - short, clear items of mixed types, each with exactly one defensible answer, in the files FORMATS.md describes. Use it whenever the learner asks for a quiz, a test or practice questions.
argument-hint: "Which objective, and how many questions?"
---

# Quiz

You write one quiz and its key for the learner in this workspace, and finish with a short message that it is ready.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.
Do what it asks now, and put any question for the learner at the end of your final message.

## Read first

The current directory is the learner's workspace; every path is relative to it.
Read `FORMATS.md` (the exact shape of `quizzes/NNNN.json` and `keys/NNNN.json`), `PREFERENCES.md`, `MISSION.md`, `NOTES.md`, the files in `learning-records/`, the lessons on the objective in `lessons/`, and the earlier quizzes, keys and grades.
Then read `.claude/skills/teach/references/QUIZZES.md`, the guide to writing good items and keys; this skill adds to it, and where the two differ, follow this skill.
Never edit `PREFERENCES.md`, `FORMATS.md` or anything under `.claude/`.

## Steps

1. **Pin down** the objective, its id, and the number of items asked for (four or five when none is given).
2. **Find the core:** the handful of ideas a learner must get right to meet the objective, from its lessons or, when there are none, from a high-trust source you search for and read.
3. **Plan the items** before writing: one core idea per item, a mix of types (mostly `mcq`, plus at least one `numeric` when the objective involves a quantity and at least one `short`), and the difficulty spread through the quiz.
4. **Write** the quiz to `quizzes/NNNN.json` and the key to `keys/NNNN.json`, with the same next free number, exactly as `FORMATS.md` shows.
5. **Check** every item as below, and rewrite any that fails.
6. **Finish** with a short message, in the tone `PREFERENCES.md` asks for: the quiz's path, what it covers and how many items, with no answers and nothing from the key.

## Short, clear stems

- Every stem is one or two short sentences: the situation, then the question.
  Cut background the answer does not depend on; keep every number, unit and condition it does.
- Plain words, in the learner's terms from the lessons and `GLOSSARY.md`; no double negatives, no "all of the above", no trick wording.
- Use a concrete case from the learner's mission when it fits, but keep it to the facts the item needs.

## Options and the key

- `mcq` options: usually four, each a misconception or a typical error, all about the same length and grammar, with the correct one in a different position from item to item.
- `numeric`: the unit in the stem and in `unit`, and a `tolerance` that matches the precision asked for.
- `short`: ask for a word, a phrase or one sentence, and list the other correct wordings in `accepted`.
- Every key item has a one- or two-sentence `rationale`, and maps each wrong `mcq` option that encodes a misconception to its id in `distractors`.

## Check before you finish

- Answer each item from its stem alone, without the key, and compare; rewrite any item where you hesitate or where a careful expert could argue for a second answer.
- Count the sentences in each stem: more than two means cut it.
- Check that no item gives away another's answer, that the quiz file holds no answers, and that no item repeats a practice question from a lesson.
