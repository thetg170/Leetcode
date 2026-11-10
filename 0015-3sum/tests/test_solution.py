from pathlib import Path

from tests.support.assertions import normalized_nested
from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0015-3sum.py"


def test_unique_triplets() -> None:
    solver = solution(REFERENCE)
    assert normalized_nested(solver.threeSum([-1, 0, 1, 2, -1, -4])) == [
        (-1, -1, 2),
        (-1, 0, 1),
    ]
    assert solver.threeSum([0, 1, 1]) == []
    assert normalized_nested(solver.threeSum([0, 0, 0, 0])) == [(0, 0, 0)]

