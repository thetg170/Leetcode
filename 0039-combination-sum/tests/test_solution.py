from pathlib import Path

from tests.support.assertions import normalized_nested
from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0039-combination-sum.py"


def test_combinations_can_reuse_candidates() -> None:
    solver = solution(REFERENCE)
    assert normalized_nested(solver.combinationSum([2, 3, 6, 7], 7)) == normalized_nested(
        [[2, 2, 3], [7]]
    )
    assert normalized_nested(solver.combinationSum([2, 3, 5], 8)) == normalized_nested(
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    )
