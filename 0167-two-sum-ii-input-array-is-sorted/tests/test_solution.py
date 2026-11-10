from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0167-two-sum-ii-input-array-is-sorted.py"


def test_returns_one_based_indices() -> None:
    solver = solution(REFERENCE)
    assert solver.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert solver.twoSum([2, 3, 4], 6) == [1, 3]
    assert solver.twoSum([-1, 0], -1) == [1, 2]

