from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0724-find-pivot-index.py"


def test_leftmost_pivot() -> None:
    solver = solution(REFERENCE)
    assert solver.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert solver.pivotIndex([1, 2, 3]) == -1
    assert solver.pivotIndex([2, 1, -1]) == 0

