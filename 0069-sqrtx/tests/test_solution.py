from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0069-sqrtx.py"


def test_integer_square_root() -> None:
    solver = solution(REFERENCE)
    assert solver.mySqrt(0) == 0
    assert solver.mySqrt(1) == 1
    assert solver.mySqrt(4) == 2
    assert solver.mySqrt(8) == 2
    assert solver.mySqrt(2_147_395_599) == 46_339

