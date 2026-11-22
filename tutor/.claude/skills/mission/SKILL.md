---
name: mission
description: Ask the learner why they are learning a topic and what they want to be able to do, and write the answer into MISSION.md before any lesson. Use it when MISSION.md is missing or vague, when the learner starts a new topic, or when their goal changes.
argument-hint: "What do you want to learn, and why?"
---

# Mission

You find out why the learner is learning this topic and what they want to be able to do, and you write it into `MISSION.md`, so that every lesson, quiz and answer afterwards can be tied to it.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message.

## Read first

The current directory is the learner's workspace; every path is relative to it.
Read `.claude/skills/teach/references/MISSION-FORMAT.md` for the file's shape and rules, then `MISSION.md` if it exists, `NOTES.md` and the files in `learning-records/`.
Never read `keys/`, and never edit `PREFERENCES.md`, `FORMATS.md` or anything under `.claude/`.

## Steps

1. **Decide what is needed.** If `MISSION.md` is missing, empty or still holds placeholder text, write a new one. If it exists and the learner's goal has moved, update it. If it is already clear and current, say so in one sentence and write nothing.
2. **Use what the request already says.** When the request names a goal, start from it and ask only about what is still missing; do not ask again what you were already told.
3. **Ask, in one message and at most four short questions, with an example answer for each so the learner can answer in a line:**
   - Why do you want to learn this? What is the real thing that changes for you when you can do it, such as a project, a course, a job or a habit?
   - What do you want to be able to do when you are done? Name two or three specific things you could show someone.
   - What limits you: time per week, a deadline, a budget, or the way you like to learn?
   - What do you already know that is close to this, and what do you want to leave out for now?
4. **Push back on vagueness once.** If an answer is abstract, such as "to understand X", ask for the concrete outcome behind it in one more short question; never invent an answer the learner did not give.
5. **Write `MISSION.md`** in the format of `MISSION-FORMAT.md`, using the learner's own words: a `## Why` of one to three sentences, a `## Success looks like` list of specific, observable things, `## Constraints` and `## Out of scope` from their answers; leave a section out when they gave nothing for it, and keep the file short.
6. **Confirm and finish.** Show the learner the mission in two or three lines and say they can change it any time. Put any question for the learner at the end of your final message.
7. **Record it.** Note in `NOTES.md` what you learned about the learner, and, when the mission changed, write a learning record in the format in `.claude/skills/teach/references/LEARNING-RECORD-FORMAT.md`.

When a request already says what to teach, the lesson comes first and the mission questions go at the end of the final message, as the teach skill says.
