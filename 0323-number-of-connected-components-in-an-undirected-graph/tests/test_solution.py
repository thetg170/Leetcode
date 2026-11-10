from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        pytest.param(6, [[0, 2], [2, 4], [1, 3]], 3, id="isolated-node-and-two-components"),
        pytest.param(3, [], 3, id="no-edges"),
        pytest.param(3, [[0, 1], [1, 2], [0, 2]], 1, id="cycle-counted-once"),
    ],
)
def test_cases(n: int, edges: list[list[int]], expected: int) -> None:
    actual = solution(REFERENCE).countComponents(n, edges)
    assert actual == expected
