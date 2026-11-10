from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "coins,amount,expected",
    [
        ([2, 5, 7], 12, 2),
        ([2, 4], 7, -1),
        ([2], 0, 0),
    ],
)
def test_solution(coins: list[int], amount: int, expected: int) -> None:
    assert solution(REFERENCE).coinChange(coins, amount) == expected
