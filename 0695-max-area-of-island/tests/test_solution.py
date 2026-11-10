from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "grid, expected",
    [
        pytest.param([[1, 0, 0], [1, 0, 1], [0, 1, 1]], 3, id="take-largest-component"),
        pytest.param([[0]], 0, id="all-water"),
        pytest.param([[1, 0], [0, 1]], 1, id="diagonal-is-not-connected"),
    ],
)
def test_cases(grid: list[list[int]], expected: int) -> None:
    actual = solution(REFERENCE).maxAreaOfIsland(grid)
    assert actual == expected
