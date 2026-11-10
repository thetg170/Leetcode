from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0252-meeting-rooms.py"


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[5, 10], [0, 30], [15, 20]], False),
        ([[7, 10], [2, 7]], True),
        ([], True),
    ],
)
def test_examples(intervals, expected) -> None:
    assert solution(REFERENCE).canAttendMeetings(intervals) is expected
