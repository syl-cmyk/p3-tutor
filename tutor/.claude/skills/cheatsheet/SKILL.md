---
name: cheatsheet
description: Write a one-page cheat sheet on a lesson or a topic as a self-contained HTML page in cheatsheets/, with the key terms, the formulas or steps, one worked example and the common mistakes. Use it whenever the learner asks for a cheat sheet, a summary page or a quick reference.
argument-hint: "Which lesson or topic should the cheat sheet cover?"
---

# Cheat sheet

You write one cheat sheet for the learner in this workspace, so they do not have to relearn a lesson from scratch each time they come back to it.

## The request

$ARGUMENTS

If the request above is empty, the request is the learner's latest message; when it names no lesson or topic, use the newest lesson in `lessons/`.
Do what the request asks now, and put any question for the learner at the end of your final message.

## Read first

The current directory is the learner's workspace; every path is relative to it.
Read `PREFERENCES.md`, `MISSION.md`, `NOTES.md` and the files in `learning-records/`, then the lesson in `lessons/` the cheat sheet covers; when there is no lesson, read what the request names, and then `RESOURCES.md` and `GLOSSARY.md` when they exist.
Also read `.claude/skills/teach/references/lesson-template.html` for the page's look, and the "Cheat sheets" part of `.claude/skills/teach/references/LESSONS.md`.
Never read `keys/`, and never edit `PREFERENCES.md`, `FORMATS.md` or anything under `.claude/`.

## What goes on the page

A cheat sheet is the compressed essence of the lesson, built for a quick look and for printing: one page, about 250 to 400 words in all, and nothing the lesson did not already teach.

1. **Title and one line** that says what the sheet is for, using the lesson's own technical term for the topic.
2. **Key terms:** each term in a few words, as a short two-column table of the term and what it means in plain words.
   Put the terms in the order the rules need them, and include every word a rule uses that a beginner could not know, such as "setup" or "turn", each with its plain meaning in a few words.
3. **The formulas, steps or rules** the learner will want to look up, as a numbered list or a small table.
   Write each rule as one short plain sentence that says what happens, with a reason in a few words beside it ("because ..."), never as a compressed formula or a phrase that only makes sense once you already know the idea; when a rule is a formula, say it in words first and give the formula after it, and explain every symbol or term in it.
4. **One worked example** with real numbers or a real case taken from the lesson, short enough to read in a minute, with every step shown.
5. **Common mistakes:** the misconceptions the lesson named, each as "wrong idea, then what is true", in one line.
6. **Where to go deeper:** the lesson it comes from, with a relative link such as `../lessons/NNNN-<slug>.html`, and the lesson's primary source.

## How to write it

- Follow `PREFERENCES.md` for tone and examples, and keep the lesson's technical terms word for word, each explained where it first appears on the page.
- Do not add a fact, a number or a link that is not in the lesson or in `RESOURCES.md`; a cheat sheet that repeats a mistake spreads it.
- Make it self-contained: the CSS inline, copied from the template, no script, stylesheet, font or image from the web, a `<title>`, and a layout that prints on one page.
- Write it to `cheatsheets/<slug>.html`, with a short slug from the topic, and read it back to be sure it exists; if a cheat sheet on the same topic already exists, update it instead of adding a second one.

## Finish

Finish with a short message in the tone `PREFERENCES.md` asks for: the sheet's path and what is on it, in two sentences, with nothing from `keys/`.
