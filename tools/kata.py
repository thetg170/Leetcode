#!/usr/bin/env python3
from __future__ import annotations

import argparse
import ast
import json
import os
import random
import re
import subprocess
import sys
import tomllib
from datetime import date, datetime, timedelta
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

import tomli_w


ROOT = Path(__file__).resolve().parents[1]
PRACTICE = ROOT / "practice"
STATE_PATH = PRACTICE / ".session.json"
SESSIONS_PATH = PRACTICE / "sessions.jsonl"
LADDER = [1, 3, 7, 14, 30, 60]


class StatementParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.in_pre = False
        self.pre_just_started = False
        self.skip_depth = 0
        self.example_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if self.skip_depth:
            self.skip_depth += 1
            return
        if tag in {"h2", "h3"}:
            self.skip_depth = 1
        elif tag == "pre":
            self.in_pre = True
            self.pre_just_started = True
            self.parts.append("\n```text\n")
        elif self.in_pre:
            return
        elif tag == "p":
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "strong" and "example" in (attributes.get("class") or ""):
            self.parts.append("\n\n## ")
            self.example_depth = 1
        elif tag == "strong":
            self.parts.append("**")
        elif tag == "em":
            self.parts.append("*")
        elif tag == "code":
            self.parts.append("`")
        elif tag == "sup":
            self.parts.append("^")
        elif tag == "img" and attributes.get("src"):
            self.parts.append(f"\n[Diagram]({attributes['src']})\n")

    def handle_endtag(self, tag: str) -> None:
        if self.skip_depth:
            self.skip_depth -= 1
            return
        if tag == "pre":
            self.in_pre = False
            if self.parts:
                self.parts[-1] = self.parts[-1].rstrip("\n")
            self.parts.append("\n```\n\n")
        elif self.in_pre:
            return
        elif tag == "li":
            self.parts.append("\n")
        elif tag == "strong" and self.example_depth:
            self.example_depth = 0
            self.parts.append("\n")
        elif tag == "strong":
            self.parts.append("**")
        elif tag == "em":
            self.parts.append("*")
        elif tag == "code":
            self.parts.append("`")

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        if self.in_pre:
            if self.pre_just_started:
                data = data.lstrip("\n")
                self.pre_just_started = False
            self.parts.append(data)
        elif "\xa0" in data and data.isspace():
            self.parts.append(" ")
        elif data.isspace():
            return
        else:
            self.parts.append(re.sub(r"\s+", " ", data.replace("\xa0", " ")))


def statement_markdown(item: dict[str, Any]) -> str:
    problem_root = Path(item["_root"])
    source = problem_root / item["files"]["statement"]
    parser = StatementParser()
    parser.feed(source.read_text(encoding="utf-8"))
    body = "".join(parser.parts)
    body = re.sub(r"\*\*([^*\n]+?)\s+\*\*", r"**\1**", body)
    body = re.sub(
        r"(?m)^\*\*(Constraints:|Follow[- ]?up:)\*\*[ \t]*",
        r"## \1\n\n",
        body,
    )
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    body = re.sub(r"\n\n(?=- )", "\n", body)
    problem = item["problem"]
    header = [
        f"# {problem['frontend_id']}. {problem['title']}",
        "",
        f"**Difficulty:** {str(problem['difficulty']).title()}",
    ]
    if problem.get("source_url"):
        header.extend(["", f"[Open on LeetCode]({problem['source_url']})"])
    return "\n".join(header) + "\n\n" + body + "\n"


def load_problems() -> list[dict[str, Any]]:
    problems: list[dict[str, Any]] = []
    for path in sorted(ROOT.glob("*/meta.toml")):
        with path.open("rb") as handle:
            meta = tomllib.load(handle)
        meta["_meta_path"] = str(path)
        meta["_root"] = str(path.parent)
        problems.append(meta)
    return problems


def resolve_problem(selector: str | None = None, path: str | None = None) -> dict[str, Any]:
    problems = load_problems()
    if path:
        current = Path(path).resolve()
        if current.is_file():
            current = current.parent
        for parent in (current, *current.parents):
            meta_path = parent / "meta.toml"
            if meta_path.is_file():
                return next(item for item in problems if item["_meta_path"] == str(meta_path))
        raise SystemExit(f"no meta.toml found above {path}")
    if not selector:
        raise SystemExit("a problem directory or current path is required")
    exact = [item for item in problems if item["problem"]["directory"] == selector]
    if exact:
        return exact[0]
    matches = [
        item
        for item in problems
        if str(item["problem"]["repo_id"]) == selector
        or str(item["problem"]["frontend_id"]) == selector
    ]
    if len(matches) != 1:
        raise SystemExit(f"problem selector is missing or ambiguous: {selector}")
    return matches[0]


def due_problems(*, include_backlog: bool = False, pattern: str | None = None) -> list[dict[str, Any]]:
    today = date.today().isoformat()
    result = []
    for item in load_problems():
        problem = item["problem"]
        review = item["review"]
        classification = item["classification"]
        if not problem.get("active", False):
            continue
        if pattern and pattern not in classification.get("patterns", []):
            continue
        if include_backlog:
            result.append(item)
        elif review.get("queue") == "core" and review.get("due", "") <= today:
            result.append(item)
    result.sort(
        key=lambda item: (
            0 if item["review"].get("queue") == "core" else 1,
            item["review"].get("due") or "9999-12-31",
            item["review"].get("attempts", 0),
            item["review"].get("seed_order", 9999),
            item["problem"]["directory"],
        )
    )
    return result


def public_problem(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "directory": item["problem"]["directory"],
        "frontend_id": item["problem"]["frontend_id"],
        "title": item["problem"]["title"],
        "difficulty": item["problem"]["difficulty"],
        "patterns": item["classification"].get("patterns", []),
        "state": item["review"]["state"],
        "queue": item["review"]["queue"],
        "due": item["review"].get("due", ""),
        "attempts": item["review"].get("attempts", 0),
    }


def stub_source(reference: Path) -> str:
    tree = ast.parse(reference.read_text(encoding="utf-8"))
    classes = [
        node
        for node in tree.body
        if isinstance(node, ast.ClassDef) and node.name not in {"ListNode", "Node", "TreeNode"}
    ]
    if not classes:
        raise SystemExit(f"no practice class found in {reference}")
    referenced = {node.id for node in ast.walk(tree) if isinstance(node, ast.Name)}
    node_types = {"ListNode", "Node"} | referenced.intersection(
        {"GraphNode", "RandomListNode", "TreeNode"}
    )
    node_imports = ", ".join(sorted(node_types))
    lines = [
        "from __future__ import annotations",
        "",
        "import bisect",
        "import heapq",
        "import math",
        "from collections import Counter, defaultdict, deque",
        "from typing import List, Optional",
        "",
        f"from tests.support.nodes import {node_imports}",
        "",
        "",
    ]
    for class_node in classes:
        lines.append(f"class {class_node.name}:")
        methods = [node for node in class_node.body if isinstance(node, ast.FunctionDef)]
        if not methods:
            lines.append("    pass")
        for index, method in enumerate(methods):
            signature = ast.unparse(method.args)
            returns = f" -> {ast.unparse(method.returns)}" if method.returns else ""
            lines.append(f"    def {method.name}({signature}){returns}:")
            lines.append("        raise NotImplementedError")
            if index != len(methods) - 1:
                lines.append("")
        lines.extend(["", ""])
    return "\n".join(lines).rstrip() + "\n"


class SingleMutation(ast.NodeTransformer):
    def __init__(self, choice: int) -> None:
        self.choice = choice
        self.seen = 0
        self.description = ""

    def visit_Compare(self, node: ast.Compare) -> ast.AST:
        self.generic_visit(node)
        if self.description or not node.ops:
            return node
        replacements = {
            ast.Lt: ast.LtE,
            ast.LtE: ast.Lt,
            ast.Gt: ast.GtE,
            ast.GtE: ast.Gt,
            ast.Eq: ast.NotEq,
            ast.NotEq: ast.Eq,
        }
        replacement = replacements.get(type(node.ops[0]))
        if replacement:
            if self.seen == self.choice:
                old = type(node.ops[0]).__name__
                node.ops[0] = replacement()
                self.description = f"comparison {old} -> {replacement.__name__}"
            self.seen += 1
        return node


def repair_source(reference: Path, seed: int) -> tuple[str, str]:
    tree = ast.parse(reference.read_text(encoding="utf-8"))
    candidates = sum(
        isinstance(node, ast.Compare)
        and bool(node.ops)
        and type(node.ops[0]) in {ast.Lt, ast.LtE, ast.Gt, ast.GtE, ast.Eq, ast.NotEq}
        for node in ast.walk(tree)
    )
    if not candidates:
        raise SystemExit(f"no safe repair mutation is available for {reference.name}")
    mutation = SingleMutation(random.Random(seed).randrange(candidates))
    mutated = mutation.visit(tree)
    ast.fix_missing_locations(mutated)
    header = "from __future__ import annotations\nfrom typing import List, Optional\nfrom tests.support.nodes import ListNode, Node\n\n"
    return header + ast.unparse(mutated) + "\n", mutation.description


def start_session(item: dict[str, Any], mode: str, force: bool) -> dict[str, Any]:
    problem_root = Path(item["_root"])
    reference = problem_root / item["files"]["reference"]
    target = problem_root / ("buggy.py" if mode == "repair" else "kata.py")
    if target.exists():
        if not force:
            raise SystemExit(f"{target} already exists")
        target.unlink()

    mutation = ""
    seed = int(datetime.now().timestamp())
    if mode == "repair":
        content, mutation = repair_source(reference, seed)
    else:
        content = stub_source(reference)
    target.write_text(content, encoding="utf-8")

    state = {
        "problem": item["problem"]["directory"],
        "mode": mode,
        "started_at": datetime.now().astimezone().isoformat(timespec="seconds"),
        "target": str(target.relative_to(ROOT)),
        "test_runs": 0,
        "failed_runs": 0,
        "last_test_passed": False,
        "mutation_seed": seed if mode == "repair" else None,
        "mutation": mutation,
    }
    PRACTICE.mkdir(exist_ok=True)
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return {
        **public_problem(item),
        "mode": mode,
        "statement": str((problem_root / item["files"]["statement"]).resolve()),
        "statement_markdown": statement_markdown(item),
        "target": str(target.resolve()),
        "tests": str((problem_root / item["files"]["tests"]).resolve()),
        "mutation": mutation,
    }


def resume_session(item: dict[str, Any], mode: str) -> dict[str, Any]:
    problem_root = Path(item["_root"])
    target = problem_root / ("buggy.py" if mode == "repair" else "kata.py")
    if not target.exists():
        raise SystemExit(f"no existing scratch file to resume: {target}")

    state: dict[str, Any] | None = None
    if STATE_PATH.exists():
        candidate = json.loads(STATE_PATH.read_text(encoding="utf-8"))
        if candidate.get("problem") == item["problem"]["directory"] and candidate.get(
            "target"
        ) == str(target.relative_to(ROOT)):
            state = candidate
    if state is None:
        state = {
            "problem": item["problem"]["directory"],
            "mode": mode,
            "started_at": datetime.now().astimezone().isoformat(timespec="seconds"),
            "target": str(target.relative_to(ROOT)),
            "test_runs": 0,
            "failed_runs": 0,
            "last_test_passed": False,
            "mutation_seed": None,
            "mutation": "",
        }
        PRACTICE.mkdir(exist_ok=True)
        STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")

    return {
        **public_problem(item),
        "mode": state["mode"],
        "statement": str((problem_root / item["files"]["statement"]).resolve()),
        "statement_markdown": statement_markdown(item),
        "target": str(target.resolve()),
        "tests": str((problem_root / item["files"]["tests"]).resolve()),
        "mutation": state.get("mutation", ""),
    }


def load_state() -> dict[str, Any]:
    if not STATE_PATH.exists():
        raise SystemExit("no active kata session")
    return json.loads(STATE_PATH.read_text(encoding="utf-8"))


def run_tests(item: dict[str, Any]) -> int:
    state = load_state()
    if state["problem"] != item["problem"]["directory"]:
        raise SystemExit(f"active session is for {state['problem']}, not {item['problem']['directory']}")
    test_path = Path(item["_root"]) / item["files"]["tests"]
    if not test_path.exists():
        raise SystemExit(f"tests have not been curated yet: {test_path}")
    target = ROOT / state["target"]
    env = os.environ.copy()
    env["KATA_TARGET"] = str(target)
    completed = subprocess.run(
        [sys.executable, "-m", "pytest", str(test_path), "-q"],
        cwd=ROOT,
        env=env,
        check=False,
    )
    state["test_runs"] += 1
    state["last_test_passed"] = completed.returncode == 0
    if completed.returncode != 0:
        state["failed_runs"] += 1
    STATE_PATH.write_text(json.dumps(state, indent=2) + "\n", encoding="utf-8")
    return completed.returncode


def finish_session(grade: str, note: str, motions: list[str]) -> dict[str, Any]:
    state = load_state()
    item = resolve_problem(state["problem"])
    started = datetime.fromisoformat(state["started_at"])
    finished = datetime.now().astimezone()
    duration = max(0, int((finished - started).total_seconds()))

    review = item["review"]
    level = int(review.get("level", -1))
    if grade == "again":
        level = 0
        review["lapses"] = int(review.get("lapses", 0)) + 1
    elif grade == "hard":
        level = max(0, level)
    elif grade == "good":
        level = min(len(LADDER) - 1, level + 1)
    elif grade == "easy":
        level = min(len(LADDER) - 1, level + 2)
    else:
        raise SystemExit(f"unknown grade: {grade}")

    interval = LADDER[level]
    review.update(
        {
            "state": "review" if interval >= 14 else "learning",
            "level": level,
            "due": (date.today() + timedelta(days=interval)).isoformat(),
            "last_reviewed": date.today().isoformat(),
            "attempts": int(review.get("attempts", 0)) + 1,
            "last_grade": grade,
        }
    )
    clean_meta = {key: value for key, value in item.items() if not key.startswith("_")}
    Path(item["_meta_path"]).write_bytes(tomli_w.dumps(clean_meta).encode())

    event = {
        "started_at": state["started_at"],
        "finished_at": finished.isoformat(timespec="seconds"),
        "problem": state["problem"],
        "mode": state["mode"],
        "duration_seconds": duration,
        "test_runs": state["test_runs"],
        "failed_runs": state["failed_runs"],
        "last_test_passed": state["last_test_passed"],
        "grade": grade,
        "motion_focus": motions,
        "note": note,
        "next_due": review["due"],
    }
    with SESSIONS_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(event, ensure_ascii=False) + "\n")
    STATE_PATH.unlink()
    return event


def session_events() -> list[dict[str, Any]]:
    if not SESSIONS_PATH.exists():
        return []
    return [json.loads(line) for line in SESSIONS_PATH.read_text(encoding="utf-8").splitlines() if line]


def streak(events: list[dict[str, Any]]) -> int:
    days = {datetime.fromisoformat(event["finished_at"]).date() for event in events}
    cursor = date.today()
    if cursor not in days:
        cursor -= timedelta(days=1)
    count = 0
    while cursor in days:
        count += 1
        cursor -= timedelta(days=1)
    return count


def report() -> str:
    events = session_events()
    due = due_problems()
    passed = sum(event.get("last_test_passed", False) for event in events)
    seconds = sum(event.get("duration_seconds", 0) for event in events)
    lines = [
        "# Kata dashboard",
        "",
        f"- Due now: {len(due)}",
        f"- Sessions: {len(events)}",
        f"- Current streak: {streak(events)} day(s)",
        f"- Practice time: {seconds // 60} minute(s)",
        f"- Sessions ending green: {passed}/{len(events)}" if events else "- Sessions ending green: 0/0",
        "",
        "## Next due",
        "",
    ]
    for item in due[:10]:
        problem = public_problem(item)
        patterns = ", ".join(problem["patterns"]) or "unclassified"
        lines.append(f"- {problem['frontend_id']}. {problem['title']} — {patterns}")
    if not due:
        lines.append("- Nothing due. Pick a backlog problem or take the day off.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="LeetCode kata scheduler and session recorder")
    sub = parser.add_subparsers(dest="command", required=True)

    list_parser = sub.add_parser("list")
    list_parser.add_argument("--all", action="store_true")
    list_parser.add_argument("--pattern")
    list_parser.add_argument("--json", action="store_true")

    next_parser = sub.add_parser("next")
    next_parser.add_argument("--json", action="store_true")

    start_parser = sub.add_parser("start")
    start_parser.add_argument("problem")
    start_parser.add_argument("--mode", choices=["recall", "repair"], default="recall")
    start_parser.add_argument("--force", action="store_true")
    start_parser.add_argument("--json", action="store_true")

    resume_parser = sub.add_parser("resume")
    resume_parser.add_argument("problem")
    resume_parser.add_argument("--mode", choices=["recall", "repair"], default="recall")
    resume_parser.add_argument("--json", action="store_true")

    test_parser = sub.add_parser("test")
    target = test_parser.add_mutually_exclusive_group(required=True)
    target.add_argument("--problem")
    target.add_argument("--path")

    finish_parser = sub.add_parser("finish")
    finish_parser.add_argument("--grade", required=True, choices=["again", "hard", "good", "easy"])
    finish_parser.add_argument("--note", default="")
    finish_parser.add_argument("--motion", action="append", default=[])
    finish_parser.add_argument("--json", action="store_true")

    report_parser = sub.add_parser("report")
    report_parser.add_argument("--write", action="store_true")

    args = parser.parse_args()
    if args.command == "list":
        items = [public_problem(item) for item in due_problems(include_backlog=args.all, pattern=args.pattern)]
        if args.json:
            print(json.dumps(items, ensure_ascii=False))
        else:
            for item in items:
                print(f"{item['directory']}\t{item['difficulty']}\t{','.join(item['patterns'])}")
        return 0
    if args.command == "next":
        items = due_problems()
        if not items:
            raise SystemExit("no core problems are due")
        item = public_problem(items[0])
        print(json.dumps(item, ensure_ascii=False) if args.json else item["directory"])
        return 0
    if args.command == "start":
        result = start_session(resolve_problem(args.problem), args.mode, args.force)
        print(json.dumps(result, ensure_ascii=False) if args.json else result["target"])
        return 0
    if args.command == "resume":
        result = resume_session(resolve_problem(args.problem), args.mode)
        print(json.dumps(result, ensure_ascii=False) if args.json else result["target"])
        return 0
    if args.command == "test":
        return run_tests(resolve_problem(args.problem, args.path))
    if args.command == "finish":
        result = finish_session(args.grade, args.note, args.motion)
        print(json.dumps(result, ensure_ascii=False) if args.json else f"next due: {result['next_due']}")
        return 0
    if args.command == "report":
        content = report()
        if args.write:
            target = PRACTICE / "dashboard.md"
            target.write_text(content, encoding="utf-8")
            print(target)
        else:
            print(content, end="")
        return 0
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
