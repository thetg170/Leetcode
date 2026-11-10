from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([3, 8, 4, 7], 15, id="take-nonadjacent-high-values"),
        pytest.param([9], 9, id="single-house"),
        pytest.param([2, 1, 1, 2], 4, id="optimal-skips-tempting-middle-house"),
    ],
)
def test_cases(nums: list[int], expected: int) -> None:
    actual = solution(REFERENCE).rob(nums)
    assert actual == expected
