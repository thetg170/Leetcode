from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "x,n,expected",
    [
        (4.0, -2, 0.0625),
        (-2.0, 3, -8.0),
        (2.5, 0, 1.0),
    ],
)
def test_solution(x: float, n: int, expected: float) -> None:
    assert solution(REFERENCE).myPow(x, n) == pytest.approx(expected)
