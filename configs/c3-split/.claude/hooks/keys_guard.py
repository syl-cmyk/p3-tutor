#!/usr/bin/env python3
"""PreToolUse guard: keeps the answer keys in keys/ away from the tutor's main conversation.

Claude Code sends the tool call as JSON on stdin. Inside a subagent the JSON carries "agent_type"
(the subagent's name); in the main conversation it does not. Exit 2 blocks the call and the model
sees what is written to stderr; exit 0 lets it go ahead. Every case below decides on purpose,
including input it cannot read.

Known gap (see EVAL.md section 7): a shell command that builds the folder name in a way no pattern here
recognises, for example from pieces joined at run time, gets through.
"""

import json
import re
import sys

# The agents that need a key to do their job, and no others.
ALLOWED_AGENTS = {"grader", "grade-reviewer"}

# The word "keys" as a path part or a word, but not inside another word such as "monkeys" or "keyboard".
KEYS_WORD = re.compile(r"(?<![A-Za-z0-9_-])keys(?![A-Za-z0-9_-])", re.IGNORECASE)
# A shell pattern that can stand for keys, such as k*, ke*, key*, k?ys or [k]eys.
KEYS_PATTERN = re.compile(r"(?<![A-Za-z0-9_-])(?:k(?:e(?:y(?:s)?)?)?[*?\[]|\[[kK]\])")
# Where a search with no folder named would start: the whole workspace, keys/ included.
WORKSPACE_ROOT = {"", ".", "./", "*", "**"}

MESSAGE = (
    "Blocked: the answer keys in keys/ are not available to this conversation. "
    "Do not read them. To grade a submission, start the grader subagent and wait for its report; "
    "for anything else, work from quizzes/, lessons/ and the learner's files."
)


def block(reason=MESSAGE):
    sys.stderr.write(reason + "\n")
    sys.exit(2)


def normalize(text):
    """Use forward slashes, so keys\\0001.json and ./keys/0001.json look the same."""
    return str(text or "").replace("\\", "/")


def touches_keys(text):
    text = normalize(text)
    return bool(KEYS_WORD.search(text) or KEYS_PATTERN.search(text))


def main():
    try:
        data = json.load(sys.stdin)
        if not isinstance(data, dict):
            raise ValueError("input is not an object")
    except Exception:
        block("Blocked: the key guard could not read the tool call, so it blocks it to be safe.")

    if data.get("agent_type") in ALLOWED_AGENTS:
        sys.exit(0)

    tool = data.get("tool_name", "")
    args = data.get("tool_input") or {}
    if not isinstance(args, dict):
        block("Blocked: the key guard could not read the tool call, so it blocks it to be safe.")

    if tool == "Read":
        if touches_keys(args.get("file_path")):
            block()
    elif tool == "Grep":
        if touches_keys(args.get("path")) or touches_keys(args.get("glob")):
            block()
        if normalize(args.get("path")).strip() in WORKSPACE_ROOT:
            block(
                "Blocked: a search over the whole workspace would reach keys/. "
                "Name the folder to search, such as lessons/ or quizzes/."
            )
    elif tool == "Glob":
        if touches_keys(args.get("pattern")) or touches_keys(args.get("path")):
            block()
    elif tool in ("Bash", "PowerShell"):
        if touches_keys(args.get("command")):
            block()

    sys.exit(0)


if __name__ == "__main__":
    main()
