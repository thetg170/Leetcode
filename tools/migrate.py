#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SEED = [
    "0001-two-sum",
    "0125-valid-palindrome",
    "0003-longest-substring-without-repeating-characters",
    "0035-search-insert-position",
    "0020-valid-parentheses",
    "0560-subarray-sum-equals-k",
    "0206-reverse-linked-list",
    "0347-top-k-frequent-elements",
    "0078-subsets",
    "0217-contains-duplicate",
    "0167-two-sum-ii-input-array-is-sorted",
    "0424-longest-repeating-character-replacement",
    "0069-sqrtx",
    "0735-asteroid-collision",
    "0303-range-sum-query-immutable",
    "0141-linked-list-cycle",
    "0295-find-median-from-data-stream",
    "0039-combination-sum",
    "0242-valid-anagram",
    "0011-container-with-most-water",
    "0438-find-all-anagrams-in-a-string",
    "0792-binary-search",
    "0155-min-stack",
    "0724-find-pivot-index",
    "0908-middle-of-the-linked-list",
    "0049-group-anagrams",
    "0015-3sum",
    "0209-minimum-size-subarray-sum",
    "0907-koko-eating-bananas",
    "0283-move-zeroes",
]

PATTERN_BY_TAG = {
    "Hash Table": "hash-map",
    "Two Pointers": "two-pointers",
    "Sliding Window": "sliding-window",
    "Binary Search": "binary-search",
    "Stack": "stack",
    "Monotonic Stack": "monotonic-stack",
    "Prefix Sum": "prefix-sum",
    "Linked List": "linked-list",
    "Heap (Priority Queue)": "heap",
    "Backtracking": "backtracking",
    "Dynamic Programming": "dynamic-programming",
    "Graph": "graph",
    "Topological Sort": "topological-sort",
    "Union-Find": "union-find",
    "Greedy": "greedy",
}


def quoted(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def array(values: list[str]) -> str:
    return "[" + ", ".join(quoted(value) for value in values) + "]"


def topic_map() -> dict[str, list[str]]:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    result: dict[str, list[str]] = {}
    for match in re.finditer(r"^## ([^\n]+)\n(.*?)(?=^## |\Z)", text, re.MULTILINE | re.DOTALL):
        topic, body = match.groups()
        for directory in re.findall(r"\[([^\]]+)\]\(https://github\.com/[^)]+\)", body):
            result.setdefault(directory, []).append(topic.strip())
    return result


def problem_header(directory: Path) -> tuple[int, str, str]:
    readme = (directory / "README.md").read_text(encoding="utf-8")
    match = re.search(r'<h2><a href="([^"]+)">(\d+)\.\s*(.*?)</a>', readme)
    if not match:
        return int(directory.name[:4]), directory.name[5:].replace("-", " ").title(), ""
    url, frontend_id, title = match.groups()
    return int(frontend_id), re.sub(r"<[^>]+>", "", title), url


def metadata_text(directory: Path, tags: list[str], difficulty: str) -> str:
    reference = next(
        path
        for path in sorted(directory.glob("*.py"))
        if path.name not in {"kata.py", "buggy.py"}
    )
    frontend_id, title, url = problem_header(directory)
    patterns = sorted({PATTERN_BY_TAG[tag] for tag in tags if tag in PATTERN_BY_TAG})
    is_seed = directory.name in SEED
    seed_order = SEED.index(directory.name) + 1 if is_seed else 0
    state = "learning" if is_seed else "new"
    due = date.today().isoformat() if is_seed else ""
    lines = [
        "schema_version = 1",
        "",
        "[problem]",
        f"repo_id = {int(directory.name[:4])}",
        f"frontend_id = {frontend_id}",
        f"directory = {quoted(directory.name)}",
        f"slug = {quoted(directory.name[5:])}",
        f"title = {quoted(title)}",
        'language = "python"',
        f"difficulty = {quoted(difficulty)}",
        f"source_url = {quoted(url)}",
        "active = true",
        "",
        "[files]",
        'statement = "README.md"',
        f"reference = {quoted(reference.name)}",
        'tests = "tests/test_solution.py"',
        "",
        "[classification]",
        f"tags = {array(sorted(tags))}",
        f"patterns = {array(patterns)}",
        "pattern_verified = false",
        "",
        "[review]",
        f"state = {quoted(state)}",
        f"queue = {quoted('core' if is_seed else 'backlog')}",
        f"seed_order = {seed_order}",
        "level = -1",
        f"due = {quoted(due)}",
        'last_reviewed = ""',
        "attempts = 0",
        "lapses = 0",
        'last_grade = ""',
        "",
    ]
    return "\n".join(lines)


def note_text(title: str) -> str:
    return f"# {title}\n\n## Pattern\n\n## Mistakes\n\n## Review notes\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Create practice metadata without touching LeetHub files"
    )
    parser.add_argument("--apply", action="store_true", help="write files; default is dry-run")
    parser.add_argument("--force", action="store_true", help="replace existing generated metadata")
    args = parser.parse_args()

    topics = topic_map()
    stats = json.loads((ROOT / "stats.json").read_text(encoding="utf-8"))["leetcode"]["shas"]
    python_dirs = sorted(
        {
            path.parent
            for path in ROOT.glob("[0-9][0-9][0-9][0-9]-*/*.py")
            if (path.parent / "README.md").is_file()
        }
    )
    created = skipped = 0
    for directory in python_dirs:
        target = directory / "meta.toml"
        if target.exists() and not args.force:
            skipped += 1
            continue
        difficulty = stats.get(directory.name, {}).get("difficulty", "unknown")
        content = metadata_text(directory, topics.get(directory.name, []), difficulty)
        if args.apply:
            target.write_text(content, encoding="utf-8")
            if directory.name in SEED:
                frontend_id, title, _ = problem_header(directory)
                note = directory / "notes.md"
                if not note.exists():
                    note.write_text(note_text(f"{frontend_id}. {title}"), encoding="utf-8")
        created += 1

    verb = "would create" if not args.apply else "created"
    print(f"{verb} {created} metadata files; skipped {skipped}; Python problems {len(python_dirs)}")
    print(f"core seed size: {len(SEED)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
