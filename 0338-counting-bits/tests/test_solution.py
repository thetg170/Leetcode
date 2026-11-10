from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n,expected",
    [
        (3, [0, 1, 1, 2]),
        (0, [0]),
        (5, [0, 1, 1, 2, 1, 2]),
    ],
)
def test_solution(n: int, expected: list[int]) -> None:
    assert solution(REFERENCE).countBits(n) == expected
