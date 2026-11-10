from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "intervals,newInterval,expected",
    [
        ([[1, 2], [5, 7]], [2, 6], [[1, 7]]),
        ([[4, 5]], [1, 2], [[1, 2], [4, 5]]),
        ([], [2, 3], [[2, 3]]),
    ],
)
def test_solution(
    intervals: list[list[int]], newInterval: list[int], expected: list[list[int]]
) -> None:
    assert solution(REFERENCE).insert(intervals, newInterval) == expected
