#!/usr/bin/env python3
"""Offline terminal workspace for the existing LeetCode archive."""

from __future__ import annotations

import argparse
import fcntl
import json
import math
import re
import shutil
import subprocess
import sys
import tempfile
import tomllib
from collections import Counter
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from kata import statement_markdown, stub_source
from lc_runner import run_local
from lc_workspace import Workspace
from migrate import problem_header, topic_map

ROOT = Path(__file__).resolve().parents[1]
PRACTICE = ROOT / "practice"
LOCAL = PRACTICE / ".lc"
REVIEWS = LOCAL / "reviews"
STATES = {
    "not-started": "Not Started",
    "in-progress": "In Progress",
    "solved": "Solved",
    "need-review": "Need Review",
}


@dataclass(frozen=True)
class Problem:
    directory: Path
    repo_id: int
    frontend_id: int
    slug: str
    title: str
    difficulty: str
    language: str
    url: str
    topics: tuple[str, ...]
    reference: Path
    archived_solution: Path
    statement: Path
    tests: Path

    @property
    def name(self) -> str:
        return self.directory.name

    @property
    def solution(self) -> Path:
        extension = {"python": "py", "sql": "sql"}.get(self.language, "txt")
        return self.directory / f"solution.{extension}"

    @property
    def progress_path(self) -> Path:
        return PRACTICE / "progress" / f"{self.name}.json"

    def label(self) -> str:
        return (
            f"{self.name}\t#{self.frontend_id}  {self.title}  [{self.difficulty}, {self.language}]"
        )


def child_path(directory: Path, filename: str) -> Path:
    path = directory / filename
    if not path.resolve().is_relative_to(directory):
        raise ValueError(f"Path leaves {directory.name}: {filename}")
    return path


def archive_problem(directory: Path, archive_topics: dict[str, list[str]]) -> Problem:
    repo_id, slug = directory.name.split("-", 1)
    try:
        frontend_id, title, url = problem_header(directory)
    except FileNotFoundError:
        frontend_id, title, url = int(repo_id), slug.replace("-", " ").title(), ""

    default_ref = directory / f"{directory.name}.py"
    language = "python" if default_ref.is_file() else "unknown"
    if language == "unknown" and default_ref.with_suffix(".sql").is_file():
        language, default_ref = "sql", default_ref.with_suffix(".sql")
    meta_path = directory / "meta.toml"
    meta = {}
    if meta_path.is_file():
        try:
            meta = tomllib.loads(meta_path.read_text(encoding="utf-8"))
        except tomllib.TOMLDecodeError as exc:
            print(
                f"lc: {directory.name}/meta.toml: {exc}. Using archive defaults.", file=sys.stderr
            )

    problem = meta.get("problem", {})
    files = meta.get("files", {})
    classification = meta.get("classification", {})
    reference = child_path(directory, files.get("reference", default_ref.name))
    archived_name = files.get("archived_solution")
    archived_solution = child_path(directory, archived_name) if archived_name else reference
    return Problem(
        directory=directory,
        repo_id=int(repo_id),
        frontend_id=problem.get("frontend_id", frontend_id),
        slug=problem.get("slug", slug),
        title=problem.get("title", title),
        difficulty=problem.get("difficulty", "unknown"),
        language=problem.get("language", language),
        url=problem.get("source_url", url),
        topics=tuple(classification.get("tags", archive_topics.get(directory.name, []))),
        reference=reference,
        archived_solution=archived_solution,
        statement=child_path(directory, files.get("statement", "README.md")),
        tests=child_path(directory, files.get("tests", "tests/test_solution.py")),
    )


def catalog() -> list[Problem]:
    topics = topic_map()
    problems = []
    for directory in sorted(ROOT.iterdir()):
        if not re.fullmatch(r"[0-9]+-[a-z0-9][a-z0-9-]*", directory.name):
            continue
        if not directory.is_dir() or directory.is_symlink():
            continue
        try:
            problems.append(archive_problem(directory, topics))
        except (OSError, ValueError, TypeError, AttributeError) as exc:
            print(f"lc: Skipping {directory.name}: {exc}", file=sys.stderr)
    return problems


def resolve(problems: list[Problem], selector: str | None) -> Problem:
    if selector is None:
        raise ValueError("Choose a problem with lc open, or pass its ID.")
    query = selector.casefold()
    matches = [item for item in problems if query in {item.name, item.slug}]
    if not matches and query.isascii() and query.isdecimal():
        matches = [item for item in problems if int(query) in {item.repo_id, item.frontend_id}]
    if not matches:
        raise ValueError(f"Problem not found: {selector}")
    if len(matches) > 1:
        names = ", ".join(item.name for item in matches)
        raise ValueError(f"Ambiguous problem {selector}: {names}. Use a full directory name.")
    return matches[0]


@contextmanager
def workspace_lock():
    LOCAL.mkdir(parents=True, exist_ok=True)
    with (LOCAL / "lock").open("a") as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        yield


def write_local(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        delete=False,
    ) as temp:
        temp_path = Path(temp.name)
        try:
            temp.write(content)
            temp.close()
            temp_path.replace(path)
        finally:
            temp_path.unlink(missing_ok=True)


def get_language() -> str:
    try:
        language = (LOCAL / "language").read_text(encoding="utf-8").strip()
        return language if language in {"en", "vi"} else "en"
    except FileNotFoundError:
        return "en"


def render(item: Problem, requested: str, *, review: bool = False) -> str:
    summaries = PRACTICE / "statements" / item.name
    en, vi = summaries / "en.md", summaries / "vi.md"
    original = item.statement.is_file()
    sources = {"en": en.is_file() or original, "vi": vi.is_file()}
    alternate = "vi" if requested == "en" else "en"
    actual = requested if sources[requested] else alternate
    headers = [
        f"# {item.frontend_id}. {item.title}",
        "",
        f"**Difficulty** {item.difficulty} · **Topics** {', '.join(item.topics) or '—'}",
    ]
    if review:
        headers += ["", "**Mode** Review draft · local only"]
    if item.url:
        headers += ["", f"[LeetCode]({item.url})"]
    if not sources[actual]:
        body = "No local statement. Add an original summary in practice/statements."
    elif (summaries / f"{actual}.md").is_file():
        body = (summaries / f"{actual}.md").read_text(encoding="utf-8")
    else:
        body = item.statement.read_text(encoding="utf-8")
        if body.lstrip().startswith("<h2"):
            converted = statement_markdown(
                {
                    "_root": str(item.directory),
                    "problem": {
                        "frontend_id": item.frontend_id,
                        "title": item.title,
                        "difficulty": item.difficulty,
                    },
                    "files": {"statement": str(item.statement.relative_to(item.directory))},
                }
            )
            body = converted.split("\n\n", 2)[-1]
    if sources[actual]:
        language = actual.upper()
        if actual != requested:
            language += f" (fallback: {requested.upper()} unavailable)"
    else:
        language = f"{requested.upper()} unavailable"
    return "\n".join([*headers, "", f"**Statement** {language}", "", body.strip(), ""])


def solution_template(item: Problem) -> str:
    content = f"# {item.title}\n"
    if item.language == "sql":
        content = f"-- {item.title}\n"
    if item.language == "python" and item.reference.is_file():
        try:
            content = stub_source(item.reference)
        except (SystemExit, SyntaxError):
            print(f"lc: No usable signature in {item.reference.name}; starting with a blank file.")
    return content


def ensure_solution(item: Problem) -> Path:
    target = child_path(item.directory, item.solution.name)
    if target.is_symlink():
        raise ValueError(f"Expected a regular workspace solution: {target}")
    if not target.exists():
        content = solution_template(item)
        try:
            with target.open("x", encoding="utf-8") as handle:
                handle.write(content)
        except FileExistsError:
            pass
    if not target.is_file():
        raise ValueError(f"Expected a workspace solution file: {target}")
    return target


def create_review(item: Problem) -> Path:
    if item.language != "python":
        raise ValueError(f"Review drafts support Python. {item.name} uses {item.language}.")
    parent = REVIEWS / item.name
    if parent.resolve() != parent:
        raise ValueError("The review draft directory must be local to this checkout.")
    content = solution_template(item)
    parent.mkdir(parents=True, exist_ok=True)
    attempt = Path(tempfile.mkdtemp(prefix="attempt-", dir=parent))
    target = attempt / item.solution.name
    write_local(target, content)
    return target


def pick(problems: list[Problem]) -> Problem | None:
    if not problems:
        raise ValueError("No problems found.")
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        raise ValueError("Open the picker in a terminal, or use lc list / lc open <problem>.")
    if shutil.which("fzf"):
        result = subprocess.run(
            ["fzf", "--prompt", "LeetCode > ", "--layout=reverse"],
            input="\n".join(item.label() for item in problems) + "\n",
            stdout=subprocess.PIPE,
            text=True,
            check=False,
        )
        if result.returncode in (1, 130):
            return None
        if result.returncode != 0:
            raise ValueError(f"fzf exited with code {result.returncode}.")
        return resolve(problems, result.stdout.split("\t", 1)[0])
    for index, item in enumerate(problems, 1):
        print(f"{index:>3}  {item.label()}")
    choice = input("Problem number, or Enter to cancel: ").strip()
    if not choice:
        return None
    if not choice.isascii() or not choice.isdecimal() or not 1 <= int(choice) <= len(problems):
        raise ValueError("Select a number from the list.")
    return problems[int(choice) - 1]


def get_progress(item: Problem) -> dict[str, str]:
    if item.progress_path.is_file():
        data = json.loads(item.progress_path.read_text(encoding="utf-8"))
        if not isinstance(data, dict) or data.get("status") not in STATES:
            raise ValueError(f"Invalid progress record: {item.progress_path.relative_to(ROOT)}")
        return data
    status = "in-progress" if item.solution.is_file() else "not-started"
    return {"status": status}


def show_status(problems: list[Problem], item: Problem | None) -> None:
    if item:
        progress = get_progress(item)
        print(item.label())
        print(STATES[progress["status"]])
        print(f"Last practiced: {progress.get('last_practiced', '—')}")
        print(f"Solution: {item.solution.relative_to(ROOT)}")
        print(f"Notes: {(item.directory / 'notes.md').relative_to(ROOT)}")
        return
    states = [(problem, get_progress(problem)["status"]) for problem in problems]
    counts = Counter(state for _, state in states)
    print(f"Total: {len(problems)}")
    for key, label in STATES.items():
        print(f"{label}: {counts[key]}")
    for problem, state in states:
        if state == "need-review":
            print(f"  {problem.label()}")


def git(*args: str, capture: bool = False) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        capture_output=capture,
        text=True,
        check=False,
    )
    if capture and result.returncode != 0:
        raise ValueError(result.stderr.strip() or f"git {args[0]} failed.")
    return result


def sync(workspace: Workspace) -> int:
    worktree = git("rev-parse", "--show-toplevel", capture=True).stdout.strip()
    if Path(worktree).resolve() != ROOT:
        raise ValueError("Run sync from a LeetCode Git checkout.")
    operations = (
        "MERGE_HEAD",
        "CHERRY_PICK_HEAD",
        "REVERT_HEAD",
        "rebase-merge",
        "rebase-apply",
        "sequencer",
        "BISECT_START",
    )
    for operation in operations:
        path = git("rev-parse", "--git-path", operation, capture=True).stdout.strip()
        if (ROOT / path).exists():
            raise ValueError("Finish or abort the in-progress Git operation before pulling.")
    if git("status", "--porcelain=v1", "--untracked-files=normal", capture=True).stdout:
        raise ValueError("Working tree has changes. Review them with git status before pulling.")
    if workspace.editor_running():
        raise ValueError("Save and quit the workspace Neovim editor with :qa before pulling.")
    return git("pull", "--ff-only", "--no-rebase", "--no-autostash").returncode


def doctor() -> int:
    missing = False
    for name in ("uv", "tmux", "nvim", "git", "fzf"):
        path = shutil.which(name)
        required = name != "fzf"
        print(f"{name}: {path or ('missing' if required else 'optional, numbered picker')}")
        missing |= required and path is None
    print(f"Python: {sys.version.split()[0]} ({sys.executable})")
    print(f"Checkout: {ROOT}")
    if not (ROOT / "uv.lock").is_file():
        print("uv.lock: missing")
        missing = True
    return int(missing)


def parser() -> argparse.ArgumentParser:
    cli = argparse.ArgumentParser(prog="lc", description=__doc__)
    sub = cli.add_subparsers(dest="command")
    for name, help_text in [
        ("pick", "choose a problem in the current workspace"),
        ("resume", "reattach to the workspace"),
        ("list", "list archived problems"),
        ("doctor", "check local tools"),
        ("sync", "pull only if the checkout is clean and can fast-forward"),
    ]:
        sub.add_parser(name, help=help_text)
    sub.add_parser("search", help="filter the catalog").add_argument("query")
    for name, help_text in [
        ("open", "open the regular solution"),
        ("next", "open the next problem"),
        ("review", "start a fresh Python draft for an Anki review"),
    ]:
        command = sub.add_parser(name, help=help_text)
        if name != "next":
            command.add_argument("problem")
        command.add_argument("--no-attach", action="store_true")
    sub.add_parser("lang", help="show or change statement language").add_argument(
        "language",
        choices=("vi", "en", "toggle"),
        nargs="?",
    )
    for name in ("run", "test"):
        command = sub.add_parser(
            name, help="run a local example" if name == "run" else "run pytest"
        )
        command.add_argument("problem", nargs="?")
        command.add_argument("--timeout", type=float, default=10, metavar="SECONDS")
        command.add_argument("--path", type=Path, help=argparse.SUPPRESS)
    reference = sub.add_parser("reference", help="print the local archived solution path")
    reference.add_argument("problem", nargs="?")
    reference.add_argument("--path", type=Path, help=argparse.SUPPRESS)
    sub.add_parser("status", help="show study progress").add_argument("problem", nargs="?")
    mark = sub.add_parser("mark", help="set the study state")
    mark.add_argument("status", choices=STATES)
    mark.add_argument("problem", nargs="?")
    note = sub.add_parser("note", help="append a dated Markdown note")
    note.add_argument("text")
    note.add_argument("problem", nargs="?")
    return cli


def review_problem(path: Path) -> str | None:
    if not path.is_relative_to(REVIEWS):
        return None
    parts = path.relative_to(REVIEWS).parts
    if len(parts) != 3 or not parts[1].startswith("attempt-") or parts[2] != "solution.py":
        return None
    return parts[0]


def resolve_target(problems: list[Problem], path: Path) -> tuple[Problem, Path]:
    if path.is_symlink():
        raise ValueError(f"Expected a regular workspace file: {path}")
    target = path.resolve()
    name = review_problem(target)
    item = resolve(problems, name or target.parent.name)
    if not name and target != item.solution:
        raise ValueError(f"Expected a workspace solution path for {item.name}.")
    return item, target


def workspace_target(problems: list[Problem], workspace: Workspace, args) -> tuple[Problem, Path]:
    if args.path and args.problem:
        raise ValueError("Specify a problem or a solution path.")
    path = args.path or (workspace.current_target() if not args.problem else None)
    if path:
        return resolve_target(problems, path)
    item = resolve(problems, args.problem or workspace.current())
    return item, child_path(item.directory, item.solution.name)


def main() -> int:
    args = parser().parse_args()
    action = args.command
    if action == "doctor":
        return doctor()
    workspace = Workspace(ROOT)
    if action == "sync":
        with workspace_lock():
            return sync(workspace)

    problems = catalog()
    if action in {"list", "search"}:
        for item in problems:
            if action == "list" or args.query.casefold() in item.label().casefold():
                print(item.label())
        return 0
    if action == "status":
        show_status(problems, resolve(problems, args.problem) if args.problem else None)
        return 0
    if action == "reference":
        item, _ = workspace_target(problems, workspace, args)
        archived = item.archived_solution
        if archived.name == "starter.py" or not archived.is_file():
            raise ValueError(
                f"{item.title} chưa có lời giải tham khảo local. "
                "Xem mặt sau thẻ Anki hoặc liên kết LeetCode trong đề."
            )
        print(archived)
        return 0
    if action in {"test", "run"}:
        item, target = workspace_target(problems, workspace, args)
        if not math.isfinite(args.timeout) or args.timeout <= 0:
            raise ValueError("Timeout must be a positive number of seconds.")
        if item.language != "python":
            raise ValueError(f"Local runner supports Python. {item.name} uses {item.language}.")
        if target.is_symlink():
            raise ValueError(f"Expected a regular workspace solution: {target}")
        return run_local(action, ROOT, item.directory, target, item.tests, args.timeout)

    selected = pick(problems) if action in {None, "pick"} else None
    if action in {None, "pick"} and selected is None:
        return 0
    with workspace_lock():
        if action in {"mark", "note"}:
            item = resolve(problems, args.problem or workspace.current())
            if action == "mark":
                progress = {"status": args.status, "last_practiced": date.today().isoformat()}
                write_local(item.progress_path, json.dumps(progress, indent=2) + "\n")
                print(f"{item.name}: {STATES[args.status]}")
            else:
                notes = child_path(item.directory, "notes.md")
                if notes.is_symlink() or not args.text.strip():
                    raise ValueError("Write a nonempty note to a regular notes.md file.")
                with notes.open("a", encoding="utf-8") as handle:
                    handle.write(f"\n- {date.today().isoformat()} — {args.text.strip()}\n")
                print(notes.relative_to(ROOT))
            return 0
        if action == "lang":
            language = get_language()
            if args.language:
                language = args.language
                if language == "toggle":
                    language = "vi" if get_language() == "en" else "en"
                current = workspace.current()
                if current:
                    target = workspace.current_target()
                    review = target is not None and review_problem(target) == current
                    workspace.refresh(render(resolve(problems, current), language, review=review))
                write_local(LOCAL / "language", language + "\n")
            print(language)
            return 0
        target = None
        if action in {"open", "review"}:
            selected = resolve(problems, args.problem)
            if action == "review":
                target = create_review(selected)
        elif action == "next":
            current = workspace.current()
            index = next((i for i, item in enumerate(problems) if item.name == current), -1)
            if index + 1 >= len(problems):
                raise ValueError("Reached the last problem.")
            selected = problems[index + 1]
        elif action == "resume":
            current = workspace.current()
            if current and not workspace.editor_running():
                selected = resolve(problems, current)
                previous = workspace.current_target()
                if previous and review_problem(previous) == selected.name:
                    _, target = resolve_target(problems, previous)
                    if not target.is_file():
                        raise ValueError("Review draft is missing. Run lc review to start again.")
            elif not current:
                raise ValueError("No workspace yet. Run lc to pick a problem.")
        if selected:
            if target is None:
                target = ensure_solution(selected)
            review = review_problem(target) == selected.name
            workspace.open(selected.name, target, render(selected, get_language(), review=review))
    if action == "pick" or getattr(args, "no_attach", False):
        return 0
    if not sys.stdin.isatty() or not sys.stdout.isatty():
        return 0
    return workspace.attach()


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, RuntimeError, ValueError) as exc:
        sys.exit(f"lc: {exc}")
    except (EOFError, KeyboardInterrupt):
        sys.exit(130)
