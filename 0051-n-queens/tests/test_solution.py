from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n, expected",
    [
        pytest.param(3, [], id="no-solution-for-three"),
        pytest.param(1, [["Q"]], id="single-queen"),
        pytest.param(
            4,
            [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]],
            id="both-four-queen-arrangements",
        ),
    ],
)
def test_cases(n: int, expected: list[list[str]]) -> None:
    actual = solution(REFERENCE).solveNQueens(n)
    assert sorted(map(tuple, actual)) == sorted(map(tuple, expected))
