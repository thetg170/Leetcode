from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0121-best-time-to-buy-and-sell-stock.py"


@pytest.mark.parametrize(
    "prices, expected",
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2], 0),
        ([3, 5, 1], 2),
    ],
)
def test_examples(prices, expected) -> None:
    assert solution(REFERENCE).maxProfit(prices) == expected
