from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        ([[7]], [[7]]),
    ],
)
def test_solution(matrix: list[list[int]], expected: list[list[int]]) -> None:
    matrix = [row.copy() for row in matrix]
    solution(REFERENCE).rotate(matrix)
    assert matrix == expected
