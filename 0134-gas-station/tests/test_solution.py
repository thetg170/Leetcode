from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "gas,cost,expected",
    [
        ([1, 4, 2], [2, 1, 3], 1),
        ([2, 3, 4], [3, 4, 3], -1),
        ([2], [2], 0),
    ],
)
def test_solution(gas: list[int], cost: list[int], expected: int) -> None:
    assert solution(REFERENCE).canCompleteCircuit(gas, cost) == expected
