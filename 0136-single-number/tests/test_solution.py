from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0136-single-number.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([4, 1, 2, 1, 2], 4),
        ([-3, 0, 0], -3),
        ([9], 9),
    ],
)
def test_examples(nums, expected) -> None:
    assert solution(REFERENCE).singleNumber(nums) == expected
