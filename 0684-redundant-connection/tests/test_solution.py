from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "edges, expected",
    [
        pytest.param([[1, 2], [2, 3], [3, 4], [2, 4]], [2, 4], id="last-edge-in-the-cycle"),
        pytest.param([[1, 2], [1, 3], [2, 3], [3, 4]], [2, 3], id="later-bridge-is-not-redundant"),
    ],
)
def test_cases(edges: list[list[int]], expected: list[int]) -> None:
    actual = solution(REFERENCE).findRedundantConnection(edges)
    assert actual == expected
