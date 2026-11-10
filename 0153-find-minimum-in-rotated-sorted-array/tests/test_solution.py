from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([5, 7, 9, 1, 3], 1, id="rotated-array"),
        pytest.param([-2, 0, 4], -2, id="unrotated-array"),
        pytest.param([9], 9, id="single-value"),
    ],
)
def test_cases(nums: list[int], expected: int) -> None:
    actual = solution(REFERENCE).findMin(nums)
    assert actual == expected
