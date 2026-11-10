from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "tasks, n, expected",
    [
        pytest.param(["A", "A", "A", "B"], 1, 5, id="idle-slots-needed"),
        pytest.param(["A", "A", "B"], 0, 3, id="no-cooldown"),
        pytest.param(["A", "A", "A", "B", "B", "B"], 2, 8, id="tied-most-frequent-tasks"),
    ],
)
def test_cases(tasks: list[str], n: int, expected: int) -> None:
    actual = solution(REFERENCE).leastInterval(tasks, n)
    assert actual == expected
