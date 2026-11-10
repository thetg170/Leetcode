from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0053-maximum-subarray.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([-5, -1, -8], -1),
        ([3], 3),
    ],
)
def test_examples(nums, expected) -> None:
    assert solution(REFERENCE).maxSubArray(nums) == expected
