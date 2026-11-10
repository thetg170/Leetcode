from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "hand,groupSize,expected",
    [
        ([7, 8, 9, 8, 9, 10], 3, True),
        ([1, 2, 2, 3], 2, True),
        ([1, 2, 4, 5], 4, False),
    ],
)
def test_solution(hand: list[int], groupSize: int, expected: bool) -> None:
    assert solution(REFERENCE).isNStraightHand(hand, groupSize) is expected
