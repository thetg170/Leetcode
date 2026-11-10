from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "m,n,expected",
    [
        (2, 4, 4),
        (1, 5, 1),
        (3, 3, 6),
    ],
)
def test_solution(m: int, n: int, expected: int) -> None:
    assert solution(REFERENCE).uniquePaths(m, n) == expected
