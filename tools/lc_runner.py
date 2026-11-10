"""Run saved Python solutions in a child process with a time limit."""

from __future__ import annotations

import json
import os
import signal
import subprocess
import sys
import traceback
from pathlib import Path


def run_local(
    action: str,
    root: Path,
    directory: Path,
    solution: Path,
    test_path: Path | None,
    timeout: float,
) -> int:
    example_path = root / "practice" / "examples" / f"{directory.name}.json"
    python = [sys.executable, "-u", "-m"]
    if action == "run":
        if not example_path.is_file():
            print(f"No local example for {directory.name}. Add {example_path.relative_to(root)}.")
            return 2
        command = [*python, "tools.lc_runner", str(example_path), str(solution)]
    else:
        if test_path is None or not test_path.is_file():
            print(f"No test cases for {directory.name}.")
            return 2
        command = [
            *python,
            "pytest",
            "-p",
            "tools.lc_pytest",
            "--showlocals",
            str(test_path),
        ]

    if not solution.is_file():
        print(f"No saved solution for {directory.name}. Open the problem and save your code first.")
        return 2

    env = os.environ.copy()
    env["KATA_TARGET"] = str(solution)
    env["PYTEST_DISABLE_PLUGIN_AUTOLOAD"] = "1"
    env.pop("PYTEST_ADDOPTS", None)
    with subprocess.Popen(
        command,
        cwd=root,
        env=env,
        stdin=subprocess.DEVNULL,
        start_new_session=True,
    ) as child:
        try:
            result = child.wait(timeout=timeout)
        except (subprocess.TimeoutExpired, KeyboardInterrupt) as error:
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            child.wait()
            if isinstance(error, KeyboardInterrupt):
                print("Interrupted")
                return 130
            print(f"Timeout ({timeout:g}s)")
            return 124

    if result < 0:
        print(f"Runtime Error (signal {-result})")
        return 128 - result
    return result


def same_items(actual: object, expected: list[object]) -> bool:
    if not isinstance(actual, (list, tuple)) or len(actual) != len(expected):
        return False
    remaining = expected.copy()
    for item in actual:
        try:
            remaining.remove(item)
        except ValueError:
            return False
    return True


def run_example(example_path: Path, solution_path: Path) -> int:
    from tests.support.loader import solution

    sample = json.loads(example_path.read_text(encoding="utf-8"))
    if not isinstance(sample, dict):
        raise ValueError("Example must be a JSON object")
    method = sample.get("method")
    args = sample.get("args")
    unordered = sample.get("unordered", False)
    if not isinstance(method, str) or not method.isidentifier() or method.startswith("_"):
        raise ValueError("Example requires a public Solution method")
    if not isinstance(args, list) or "expected" not in sample:
        raise ValueError("Example requires an args array and an expected value")
    expected = sample["expected"]
    if not isinstance(unordered, bool) or (unordered and not isinstance(expected, list)):
        raise ValueError("unordered must be a boolean and requires an expected array when true")

    print(f"Input:    {method}{tuple(args)!r}")
    print(f"Expected: {expected!r}")
    actual = getattr(solution(solution_path), method)(*args)
    print(f"Actual:   {actual!r}")
    passed = same_items(actual, expected) if unordered else actual == expected
    print("Passed" if passed else "Failed (wrong answer)")
    return 0 if passed else 1


if __name__ == "__main__":
    try:
        status = run_example(Path(sys.argv[1]), Path(sys.argv[2]))
    except (Exception, SystemExit):
        traceback.print_exc()
        print("Runtime Error")
        status = 2
    raise SystemExit(status)
