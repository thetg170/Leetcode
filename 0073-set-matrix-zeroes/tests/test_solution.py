from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[4, 0, 6], [7, 8, 9]], [[0, 0, 0], [7, 0, 9]]),
        ([[0, 1, 2], [3, 4, 5], [6, 7, 0]], [[0, 0, 0], [0, 4, 0], [0, 0, 0]]),
        ([[1, 2], [3, 4]], [[1, 2], [3, 4]]),
    ],
)
def test_solution(matrix: list[list[int]], expected: list[list[int]]) -> None:
    matrix = [row.copy() for row in matrix]
    solution(REFERENCE).setZeroes(matrix)
    assert matrix == expected
