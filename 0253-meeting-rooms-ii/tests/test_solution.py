from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "intervals,expected",
    [
        ([[2, 7], [3, 5], [5, 6]], 2),
        ([], 0),
        ([[0, 4], [1, 3], [2, 5]], 3),
    ],
)
def test_solution(intervals: list[list[int]], expected: int) -> None:
    assert solution(REFERENCE).minMeetingRooms(intervals) == expected
