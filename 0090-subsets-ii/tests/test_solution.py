from pathlib import Path

from tests.support.assertions import normalized_nested
from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0090-subsets-ii.py"


def test_duplicate_inputs_do_not_produce_duplicate_subsets() -> None:
    solver = solution(REFERENCE)
    assert normalized_nested(solver.subsetsWithDup([2, 1, 2])) == [
        (),
        (1,),
        (1, 2),
        (1, 2, 2),
        (2,),
        (2, 2),
    ]
    assert normalized_nested(solver.subsetsWithDup([0, 0, 0])) == [
        (),
        (0,),
        (0, 0),
        (0, 0, 0),
    ]
