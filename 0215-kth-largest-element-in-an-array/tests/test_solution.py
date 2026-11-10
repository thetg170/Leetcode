from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, k, expected",
    [
        pytest.param([8, 3, 8, 2, 7], 2, 8, id="duplicates-count-as-distinct-positions"),
        pytest.param([-4, -1, -5], 3, -5, id="k-equals-length"),
    ],
)
def test_cases(nums: list[int], k: int, expected: int) -> None:
    actual = solution(REFERENCE).findKthLargest(nums, k)
    assert actual == expected
