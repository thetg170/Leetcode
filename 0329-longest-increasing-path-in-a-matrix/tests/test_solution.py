from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "matrix,expected",
    [
        ([[1, 3], [2, 4]], 3),
        ([[7, 7], [7, 7]], 1),
        ([[4, 3, 2, 1]], 4),
    ],
)
def test_solution(matrix: list[list[int]], expected: int) -> None:
    assert solution(REFERENCE).longestIncreasingPath(matrix) == expected
