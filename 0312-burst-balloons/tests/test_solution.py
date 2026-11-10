from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 3], 9),
        ([3, 1, 5, 8], 167),
        ([0], 0),
    ],
)
def test_solution(nums: list[int], expected: int) -> None:
    assert solution(REFERENCE).maxCoins(nums) == expected
