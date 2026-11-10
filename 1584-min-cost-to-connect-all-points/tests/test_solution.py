from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "points, expected",
    [
        pytest.param([[0, 0], [1, 2], [4, 2]], 6, id="connect-through-intermediate-point"),
        pytest.param([[3, -5]], 0, id="single-point-costs-zero"),
        pytest.param([[-2, 3], [3, -1]], 9, id="use-manhattan-distance"),
    ],
)
def test_cases(points: list[list[int]], expected: int) -> None:
    actual = solution(REFERENCE).minCostConnectPoints(points)
    assert actual == expected
