from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0560-subarray-sum-equals-k.py"


def test_subarray_count() -> None:
    solver = solution(REFERENCE)
    assert solver.subarraySum([1, 1, 1], 2) == 2
    assert solver.subarraySum([1, 2, 3], 3) == 2
    assert solver.subarraySum([1, -1, 0], 0) == 3

