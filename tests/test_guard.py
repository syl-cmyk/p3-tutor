"""Tests for the key guard hook, tutor/.claude/hooks/keys_guard.py.

Each test writes a sample hook input to the script's stdin and checks its exit code: 2 blocks the call,
0 lets it go ahead. None of them calls Claude.
"""

import json
import subprocess
import sys
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "tutor" / ".claude" / "hooks" / "keys_guard.py"


def run_guard(tool_name, tool_input, agent_type=None, raw=None):
    """Run the guard on one tool call and return (exit code, stderr)."""
    if raw is None:
        payload = {"tool_name": tool_name, "tool_input": tool_input}
        if agent_type:
            payload["agent_type"] = agent_type
            payload["agent_id"] = "agent-1"
        raw = json.dumps(payload)
    done = subprocess.run(
        [sys.executable, str(SCRIPT)], input=raw, capture_output=True, text=True, timeout=30
    )
    return done.returncode, done.stderr


class MainConversationIsBlocked(unittest.TestCase):
    def assert_blocked(self, tool_name, tool_input):
        code, err = run_guard(tool_name, tool_input)
        self.assertEqual(code, 2, f"{tool_name} {tool_input} was not blocked")
        self.assertIn("Blocked", err)

    def test_read_of_a_key(self):
        self.assert_blocked("Read", {"file_path": "keys/0001.json"})

    def test_read_with_a_dot_slash_path(self):
        self.assert_blocked("Read", {"file_path": "./keys/0001.json"})

    def test_read_with_an_absolute_path(self):
        self.assert_blocked("Read", {"file_path": "/tmp/work/keys/0001.json"})

    def test_read_with_windows_separators(self):
        self.assert_blocked("Read", {"file_path": "keys\\0001.json"})

    def test_grep_in_keys(self):
        self.assert_blocked("Grep", {"pattern": "answer", "path": "keys"})

    def test_grep_with_a_glob_for_keys(self):
        self.assert_blocked("Grep", {"pattern": "answer", "path": "lessons", "glob": "keys/*.json"})

    def test_grep_over_the_whole_workspace(self):
        self.assert_blocked("Grep", {"pattern": "answer"})
        self.assert_blocked("Grep", {"pattern": "answer", "path": "."})

    def test_glob_for_keys(self):
        self.assert_blocked("Glob", {"pattern": "keys/*.json"})

    def test_bash_cat(self):
        self.assert_blocked("Bash", {"command": "cat keys/0001.json"})

    def test_bash_cat_with_a_shell_pattern(self):
        self.assert_blocked("Bash", {"command": "cat k*/0001.json"})
        self.assert_blocked("Bash", {"command": "cat ke?s/0001.json"})

    def test_bash_with_cd(self):
        self.assert_blocked("Bash", {"command": "cd keys && cat 0001.json"})

    def test_powershell_get_content(self):
        self.assert_blocked("PowerShell", {"command": "Get-Content keys/0001.json"})


class AllowedAgentsAreNotBlocked(unittest.TestCase):
    def test_grader_reads_a_key(self):
        code, _ = run_guard("Read", {"file_path": "keys/0001.json"}, agent_type="grader")
        self.assertEqual(code, 0)

    def test_grader_uses_every_tool_on_keys(self):
        for tool, args in [
            ("Grep", {"pattern": "answer", "path": "keys"}),
            ("Glob", {"pattern": "keys/*.json"}),
            ("Bash", {"command": "cat keys/0001.json"}),
            ("PowerShell", {"command": "Get-Content keys/0001.json"}),
        ]:
            with self.subTest(tool=tool):
                code, _ = run_guard(tool, args, agent_type="grader")
                self.assertEqual(code, 0)

    def test_grade_reviewer_reads_a_key(self):
        code, _ = run_guard("Read", {"file_path": "keys/0001.json"}, agent_type="grade-reviewer")
        self.assertEqual(code, 0)

    def test_another_subagent_is_blocked(self):
        code, _ = run_guard("Read", {"file_path": "keys/0001.json"}, agent_type="lesson-reviewer")
        self.assertEqual(code, 2)


class OtherReadsStillWork(unittest.TestCase):
    def assert_allowed(self, tool_name, tool_input):
        code, err = run_guard(tool_name, tool_input)
        self.assertEqual(code, 0, f"{tool_name} {tool_input} was blocked: {err}")

    def test_reading_a_quiz(self):
        self.assert_allowed("Read", {"file_path": "quizzes/0001.json"})

    def test_reading_the_learner_files(self):
        self.assert_allowed("Read", {"file_path": "MISSION.md"})
        self.assert_allowed("Read", {"file_path": "PREFERENCES.md"})

    def test_reading_a_draft_key(self):
        self.assert_allowed("Read", {"file_path": "drafts/0002-key.json"})

    def test_listing_lessons(self):
        self.assert_allowed("Bash", {"command": "ls lessons"})

    def test_grep_in_a_named_folder(self):
        self.assert_allowed("Grep", {"pattern": "cache", "path": "lessons"})

    def test_glob_for_lessons(self):
        self.assert_allowed("Glob", {"pattern": "lessons/*.html"})

    def test_a_word_that_only_contains_keys_is_not_a_key_folder(self):
        self.assert_allowed("Bash", {"command": "echo monkeys and keyboards"})

    def test_a_tool_the_guard_does_not_cover(self):
        self.assert_allowed("Write", {"file_path": "quizzes/0002.json", "content": "{}"})


class UnreadableInputIsBlocked(unittest.TestCase):
    def test_not_json(self):
        code, err = run_guard(None, None, raw="not json at all")
        self.assertEqual(code, 2)
        self.assertIn("Blocked", err)

    def test_empty_input(self):
        code, _ = run_guard(None, None, raw="")
        self.assertEqual(code, 2)

    def test_json_that_is_not_an_object(self):
        code, _ = run_guard(None, None, raw="[1, 2]")
        self.assertEqual(code, 2)


if __name__ == "__main__":
    unittest.main()
