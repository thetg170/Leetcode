from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums,expected",
    [
        ([1, 0, 2], False),
        ([2, 0, 0], True),
        ([0], True),
    ],
)
def test_solution(nums: list[int], expected: bool) -> None:
    assert solution(REFERENCE).canJump(nums) is expected
