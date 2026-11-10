from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "triplets,target,expected",
    [
        ([[1, 4, 3], [3, 2, 4], [9, 9, 9]], [3, 4, 4], True),
        ([[1, 2, 3], [2, 2, 3], [3, 1, 5]], [3, 2, 3], False),
        ([[2, 3, 4]], [2, 3, 4], True),
    ],
)
def test_solution(triplets: list[list[int]], target: list[int], expected: bool) -> None:
    assert solution(REFERENCE).mergeTriplets(triplets, target) is expected
