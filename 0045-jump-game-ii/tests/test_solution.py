from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([3, 1, 1, 1, 2], 2),
        ([2, 3, 1, 1, 4], 2),
        ([0], 0),
    ],
)
def test_solution(nums: list[int], expected: int) -> None:
    assert solution(REFERENCE).jump(nums) == expected
