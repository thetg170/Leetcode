from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "grid, expected",
    [
        pytest.param([["1", "0", "1"], ["0", "1", "1"]], 2, id="diagonal-is-not-connected"),
        pytest.param([["0", "0"]], 0, id="all-water"),
        pytest.param(
            [["1", "1", "1"], ["1", "0", "1"], ["1", "1", "1"]], 1, id="one-component-with-a-hole"
        ),
    ],
)
def test_cases(grid: list[list[str]], expected: int) -> None:
    actual = solution(REFERENCE).numIslands(grid)
    assert actual == expected
