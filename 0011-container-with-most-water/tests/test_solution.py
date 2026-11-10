from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0011-container-with-most-water.py"


def test_maximum_area() -> None:
    solver = solution(REFERENCE)
    assert solver.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert solver.maxArea([1, 1]) == 1
    assert solver.maxArea([1, 2, 4, 3]) == 4

