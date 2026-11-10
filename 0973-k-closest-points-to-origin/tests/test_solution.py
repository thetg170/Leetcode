from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "points, k, expected",
    [
        pytest.param([[-2, 1], [0, 3], [1, 0]], 2, [[1, 0], [-2, 1]], id="squared-distance"),
        pytest.param([[2, -1], [0, 0], [-2, 1]], 1, [[0, 0]], id="closest-is-origin"),
    ],
)
def test_cases(points: list[list[int]], k: int, expected: list[list[int]]) -> None:
    actual = solution(REFERENCE).kClosest(points, k)
    assert sorted(map(tuple, actual)) == sorted(map(tuple, expected))
