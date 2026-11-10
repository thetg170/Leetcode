from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "prices,expected",
    [
        ([2, 5, 1, 2, 8], 9),
        ([1, 2, 3, 0, 2], 3),
        ([3, 2, 1], 0),
    ],
)
def test_solution(prices: list[int], expected: int) -> None:
    assert solution(REFERENCE).maxProfit(prices) == expected
