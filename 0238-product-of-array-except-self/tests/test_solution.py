from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0238-product-of-array-except-self.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
        ([0, 0, 2], [0, 0, 0]),
    ],
)
def test_examples(nums, expected) -> None:
    assert solution(REFERENCE).productExceptSelf(nums) == expected
