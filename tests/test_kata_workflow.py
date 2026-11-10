from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from tools import kata


def configured_problem(monkeypatch: Any, tmp_path: Path) -> tuple[dict[str, Any], Path]:
    problem_root = tmp_path / "0001-two-sum"
    problem_root.mkdir()
    (problem_root / "README.md").write_text(
        '<h2><a href="https://leetcode.com/problems/two-sum">1. Two Sum</a></h2>'
        "<h3>Easy</h3><hr><p>Find <code>target</code>.</p>"
        '<p><strong class="example">Example 1:</strong></p>'
        "<pre><strong>Input:</strong> [2,7], 9\n<strong>Output:</strong> [0,1]</pre>",
        encoding="utf-8",
    )
    reference = problem_root / "0001-two-sum.py"
    reference.write_text(
        "class Solution:\n"
        "    def twoSum(self, nums: list[int], target: int) -> list[int]:\n"
        "        return []\n",
        encoding="utf-8",
    )
    practice = tmp_path / "practice"
    monkeypatch.setattr(kata, "ROOT", tmp_path)
    monkeypatch.setattr(kata, "PRACTICE", practice)
    monkeypatch.setattr(kata, "STATE_PATH", practice / ".session.json")
    monkeypatch.setattr(kata, "SESSIONS_PATH", practice / "sessions.jsonl")
    item: dict[str, Any] = {
        "_root": str(problem_root),
        "problem": {
            "directory": "0001-two-sum",
            "frontend_id": 1,
            "title": "Two Sum",
            "difficulty": "easy",
        },
        "files": {
            "statement": "README.md",
            "reference": reference.name,
            "tests": "tests/test_solution.py",
        },
        "classification": {"patterns": ["hash-map"]},
        "review": {
            "state": "learning",
            "queue": "core",
            "due": "2026-09-16",
            "attempts": 0,
        },
    }
    return item, problem_root


def test_resume_preserves_scratch_and_session(monkeypatch: Any, tmp_path: Path) -> None:
    item, problem_root = configured_problem(monkeypatch, tmp_path)
    kata.start_session(item, "recall", False)
    target = problem_root / "kata.py"
    target.write_text(target.read_text(encoding="utf-8") + "# work in progress\n", encoding="utf-8")
    state_before = json.loads(kata.STATE_PATH.read_text(encoding="utf-8"))

    resumed = kata.resume_session(item, "recall")
    state_after = json.loads(kata.STATE_PATH.read_text(encoding="utf-8"))

    assert resumed["target"] == str(target)
    assert "# work in progress" in target.read_text(encoding="utf-8")
    assert state_after == state_before


def test_force_restart_overwrites_without_archive(monkeypatch: Any, tmp_path: Path) -> None:
    item, problem_root = configured_problem(monkeypatch, tmp_path)
    kata.start_session(item, "recall", False)
    target = problem_root / "kata.py"
    target.write_text("# old scratch\n", encoding="utf-8")

    kata.start_session(item, "recall", True)

    assert "# old scratch" not in target.read_text(encoding="utf-8")
    assert not (kata.PRACTICE / "archive").exists()


def test_statement_is_clean_markdown(monkeypatch: Any, tmp_path: Path) -> None:
    item, _ = configured_problem(monkeypatch, tmp_path)

    statement = kata.statement_markdown(item)

    assert statement.startswith("# 1. Two Sum")
    assert "## Example 1:" in statement
    assert "`target`" in statement
    assert "<strong>" not in statement
