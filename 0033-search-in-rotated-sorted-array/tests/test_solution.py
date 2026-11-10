from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, target, expected",
    [
        pytest.param([5, 7, 9, 1, 3], 3, 4, id="find-on-rotated-side"),
        pytest.param([5, 7, 9, 1, 3], 6, -1, id="absent-value"),
        pytest.param([8], 8, 0, id="single-value"),
    ],
)
def test_cases(nums: list[int], target: int, expected: int) -> None:
    actual = solution(REFERENCE).search(nums, target)
    assert actual == expected
