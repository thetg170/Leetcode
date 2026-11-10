from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (-7, 12, 5),
        (-4, -8, -12),
        (7, -7, 0),
    ],
)
def test_solution(a: int, b: int, expected: int) -> None:
    assert solution(REFERENCE).getSum(a, b) == expected
