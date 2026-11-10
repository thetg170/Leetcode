from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([-3, 2, -4, 0, 1], 24),
        ([-2], -2),
        ([-2, 0, -1], 0),
    ],
)
def test_solution(nums: list[int], expected: int) -> None:
    assert solution(REFERENCE).maxProduct(nums) == expected
