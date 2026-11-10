from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "board, expected",
    [
        pytest.param(
            [["X", "X", "O"], ["X", "O", "X"], ["X", "X", "X"]],
            [["X", "X", "O"], ["X", "X", "X"], ["X", "X", "X"]],
            id="preserve-border-region",
        ),
        pytest.param(
            [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]],
            [["X", "O", "X"], ["X", "O", "X"], ["X", "X", "X"]],
            id="interior-connected-to-border",
        ),
    ],
)
def test_cases(board: list[list[str]], expected: list[list[str]]) -> None:
    solution(REFERENCE).solve(board)
    assert board == expected
