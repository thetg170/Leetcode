from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        pytest.param([2, 4, 1, 3], 2, [4, 4, 3], id="overlapping-windows"),
        pytest.param([-3, -1, -2], 1, [-3, -1, -2], id="width-one"),
        pytest.param([5, 5, 1, 1], 2, [5, 5, 1], id="duplicate-maxima"),
    ],
)
def test_cases(nums: list[int], k: int, expected: list[int]) -> None:
    actual = solution(REFERENCE).maxSlidingWindow(nums, k)
    assert actual == expected
