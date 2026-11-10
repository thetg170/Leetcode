from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,target,expected",
    [
        ([1, 2, 2], 1, 2),
        ([0, 0, 1], 1, 4),
        ([1, 2], -4, 0),
    ],
)
def test_solution(nums: list[int], target: int, expected: int) -> None:
    assert solution(REFERENCE).findTargetSumWays(nums, target) == expected
