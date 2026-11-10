from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[2, 4, 6], [8, 10, 12]], [2, 4, 6, 12, 10, 8]),
        ([[1], [2], [3]], [1, 2, 3]),
        ([[9, 8, 7]], [9, 8, 7]),
    ],
)
def test_solution(matrix: list[list[int]], expected: list[int]) -> None:
    assert solution(REFERENCE).spiralOrder(matrix) == expected
