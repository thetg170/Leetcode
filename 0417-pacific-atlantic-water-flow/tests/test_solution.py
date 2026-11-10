from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "heights, expected",
    [
        pytest.param(
            [[1, 2], [2, 3]], [[0, 1], [1, 0], [1, 1]], id="higher-cells-can-reach-both-coasts"
        ),
        pytest.param([[4, 4], [4, 4]], [[0, 0], [0, 1], [1, 0], [1, 1]], id="equal-height-plateau"),
        pytest.param([[3, 1, 2]], [[0, 0], [0, 1], [0, 2]], id="single-row-touches-both-coasts"),
    ],
)
def test_cases(heights: list[list[int]], expected: list[list[int]]) -> None:
    actual = solution(REFERENCE).pacificAtlantic(heights)
    assert sorted(map(tuple, actual)) == sorted(map(tuple, expected))
