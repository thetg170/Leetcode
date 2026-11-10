from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "board, word, expected",
    [
        pytest.param([["C", "A"], ["S", "T"]], "CAT", True, id="path-turns"),
        pytest.param([["A", "B"]], "ABA", False, id="cannot-revisit-start"),
        pytest.param([["A", "Z"], ["Z", "B"]], "AB", False, id="diagonal-is-not-adjacent"),
    ],
)
def test_cases(board: list[list[str]], word: str, expected: bool) -> None:
    actual = solution(REFERENCE).exist(board, word)
    assert actual is expected
