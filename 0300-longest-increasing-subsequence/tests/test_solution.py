from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([4, 1, 5, 2, 2, 6], 3),
        ([2, 2, 2], 1),
        ([5, 4, 3, 2, 1], 1),
    ],
)
def test_solution(nums: list[int], expected: int) -> None:
    assert solution(REFERENCE).lengthOfLIS(nums) == expected
