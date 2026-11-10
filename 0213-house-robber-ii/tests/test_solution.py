from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([6, 1, 2, 7], 8, id="first-and-last-are-adjacent"),
        pytest.param([9], 9, id="single-house"),
        pytest.param([2, 3, 2], 3, id="same-value-at-both-ends"),
    ],
)
def test_cases(nums: list[int], expected: int) -> None:
    actual = solution(REFERENCE).rob(nums)
    assert actual == expected
