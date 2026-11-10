from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0128-longest-consecutive-sequence.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([100, 4, 200, 1, 3, 2], 4),
        ([1, 2, 0, 1], 3),
        ([], 0),
        ([-3, -1, -2], 3),
    ],
)
def test_examples(nums, expected) -> None:
    assert solution(REFERENCE).longestConsecutive(nums) == expected
