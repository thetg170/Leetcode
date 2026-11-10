from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0746-min-cost-climbing-stairs.py"


@pytest.mark.parametrize(
    "cost, expected",
    [
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
        ([0, 2], 0),
    ],
)
def test_examples(cost, expected) -> None:
    assert solution(REFERENCE).minCostClimbingStairs(cost) == expected
