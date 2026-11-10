from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[1, 3], [2, 4], [4, 5]], 1),
        ([[1, 2], [2, 3]], 0),
        ([[1, 10], [2, 3], [3, 4]], 1),
    ],
)
def test_solution(intervals: list[list[int]], expected: int) -> None:
    assert solution(REFERENCE).eraseOverlapIntervals(intervals) == expected
