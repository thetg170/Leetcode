"""Summarize local pytest outcomes without changing existing test files."""

import os
from pathlib import Path

import pytest


@pytest.hookimpl(wrapper=True)
def pytest_runtest_makereport(call):
    report = yield
    if report.failed and call.excinfo:
        target = Path(os.environ["KATA_TARGET"]).resolve()
        origin = call.excinfo.traceback[-1].path
        wrong_answer = (
            call.when == "call"
            and call.excinfo.errisinstance(AssertionError)
            and Path(origin).resolve() != target
        )
        report.user_properties.append(("lc_outcome", "Failed" if wrong_answer else "Runtime Error"))
    return report


def pytest_terminal_summary(terminalreporter, exitstatus):
    reports = terminalreporter.stats.get("failed", []) + terminalreporter.stats.get("error", [])
    outcomes = {
        value for report in reports for key, value in report.user_properties if key == "lc_outcome"
    }
    if exitstatus == pytest.ExitCode.OK and terminalreporter.stats.get("passed"):
        summary = "Passed"
    elif exitstatus in (pytest.ExitCode.OK, pytest.ExitCode.NO_TESTS_COLLECTED):
        summary = "No test cases executed"
    else:
        summary = ", ".join(sorted(outcomes)) or "Runtime Error"
    terminalreporter.write_sep("=", summary)
