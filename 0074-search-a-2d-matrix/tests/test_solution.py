from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0074-search-a-2d-matrix.py"


@pytest.mark.parametrize(
    "matrix, target, expected",
    [
        ([[1, 3, 5], [7, 9, 11]], 7, True),
        ([[1, 3, 5], [7, 9, 11]], 6, False),
        ([[1]], 1, True),
        ([[1]], 0, False),
    ],
)
def test_examples(matrix, target, expected) -> None:
    assert solution(REFERENCE).searchMatrix(matrix, target) is expected
