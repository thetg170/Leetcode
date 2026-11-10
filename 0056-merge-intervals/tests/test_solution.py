from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0056-merge-intervals.py"


@pytest.mark.parametrize(
    "intervals, expected",
    [
        ([[8, 10], [1, 3], [2, 6], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 9], [3, 5], [6, 7]], [[1, 9]]),
    ],
)
def test_examples(intervals, expected) -> None:
    assert solution(REFERENCE).merge(intervals) == expected
