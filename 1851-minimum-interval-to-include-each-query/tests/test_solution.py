from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "intervals,queries,expected",
    [
        ([[1, 3], [2, 5]], [2, 4, 6], [3, 4, -1]),
        ([[1, 5], [3, 3]], [4, 3, 4, 0], [5, 1, 5, -1]),
    ],
)
def test_solution(intervals: list[list[int]], queries: list[int], expected: list[int]) -> None:
    assert solution(REFERENCE).minInterval(intervals, queries) == expected
