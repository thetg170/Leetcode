from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "amount,coins,expected",
    [
        (6, [2, 3], 2),
        (0, [2, 3], 1),
        (3, [2], 0),
    ],
)
def test_solution(amount: int, coins: list[int], expected: int) -> None:
    assert solution(REFERENCE).change(amount, coins) == expected
