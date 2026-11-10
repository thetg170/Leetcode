from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n, edges, expected",
    [
        pytest.param(4, [[0, 1], [1, 2], [1, 3]], True, id="connected-and-acyclic"),
        pytest.param(4, [[0, 1], [1, 2], [2, 0]], False, id="cycle-and-an-isolated-node"),
        pytest.param(1, [], True, id="isolated-single-node-is-a-tree"),
    ],
)
def test_cases(n: int, edges: list[list[int]], expected: bool) -> None:
    actual = solution(REFERENCE).validTree(n, edges)
    assert actual is expected
