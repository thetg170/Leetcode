from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "grid, expected",
    [
        pytest.param([[2, 1, 0], [0, 1, 1]], 3, id="successive-frontiers"),
        pytest.param([[2, 0, 1]], -1, id="isolated-fresh-orange"),
        pytest.param([[2, 1, 1, 2]], 1, id="multiple-sources-in-parallel"),
        pytest.param([[2]], 0, id="already-rotten"),
    ],
)
def test_cases(grid: list[list[int]], expected: int) -> None:
    actual = solution(REFERENCE).orangesRotting(grid)
    assert actual == expected
