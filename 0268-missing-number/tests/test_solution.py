from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([4, 0, 2, 1], 3),
        ([0, 1], 2),
        ([1], 0),
    ],
)
def test_solution(nums: list[int], expected: int) -> None:
    assert solution(REFERENCE).missingNumber(nums) == expected
