from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "grid, expected",
    [
        pytest.param([[0, 3], [1, 2]], 2, id="take-path-with-lowest-peak"),
        pytest.param([[3, 0], [1, 2]], 3, id="start-elevation-is-required"),
        pytest.param([[0]], 0, id="single-cell"),
    ],
)
def test_cases(grid: list[list[int]], expected: int) -> None:
    actual = solution(REFERENCE).swimInWater(grid)
    assert actual == expected
