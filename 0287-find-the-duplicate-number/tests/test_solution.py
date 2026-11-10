from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([2, 5, 1, 4, 2, 3], 2, id="nonadjacent-duplicate"),
        pytest.param([3, 3, 3, 3, 3], 3, id="duplicate-more-than-twice"),
        pytest.param([1, 1], 1, id="smallest-valid-array"),
    ],
)
def test_cases(nums: list[int], expected: int) -> None:
    original = nums.copy()
    actual = solution(REFERENCE).findDuplicate(nums)
    assert actual == expected
    assert nums == original
