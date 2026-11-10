from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_empty_and_valid_filled_cells() -> None:
    board = [["."] * 9 for _ in range(9)]
    board[0][0], board[1][4], board[4][1] = "7", "7", "7"

    assert solution(REFERENCE).isValidSudoku(board) is True


@pytest.mark.parametrize(
    "row, column",
    [(0, 4), (4, 0), (1, 1)],
    ids=["same-row", "same-column", "same-box"],
)
def test_repeated_digit_in_a_unit(row: int, column: int) -> None:
    board = [["."] * 9 for _ in range(9)]
    board[0][0] = board[row][column] = "7"

    assert solution(REFERENCE).isValidSudoku(board) is False
