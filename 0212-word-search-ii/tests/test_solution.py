from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "board, words, expected",
    [
        pytest.param(
            [["q", "a"], ["r", "t"]],
            ["qa", "qat", "qar", "trq"],
            ["qa", "qat", "trq"],
            id="adjacent-paths-without-reusing-cell",
        ),
        pytest.param([["a", "a"]], ["a", "aa", "aaa"], ["a", "aa"], id="prefix-and-longer-word"),
    ],
)
def test_cases(board: list[list[str]], words: list[str], expected: list[str]) -> None:
    actual = solution(REFERENCE).findWords(board, words)
    assert sorted(actual) == sorted(expected)
