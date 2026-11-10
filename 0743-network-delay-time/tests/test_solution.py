from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "times, n, k, expected",
    [
        pytest.param(
            [[1, 2, 3], [1, 3, 9], [2, 3, 2]], 3, 1, 5, id="cheaper-via-intermediate-node"
        ),
        pytest.param([[1, 2, 1]], 2, 2, -1, id="edge-is-directed"),
        pytest.param([[1, 2, 0]], 2, 1, 0, id="zero-weight-edge"),
    ],
)
def test_cases(times: list[list[int]], n: int, k: int, expected: int) -> None:
    actual = solution(REFERENCE).networkDelayTime(times, n, k)
    assert actual == expected
