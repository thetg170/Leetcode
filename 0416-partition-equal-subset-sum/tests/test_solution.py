from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([2, 2, 3, 3], True),
        ([1, 2, 5], False),
        ([1, 2, 4], False),
    ],
)
def test_solution(nums: list[int], expected: bool) -> None:
    assert solution(REFERENCE).canPartition(nums) is expected
