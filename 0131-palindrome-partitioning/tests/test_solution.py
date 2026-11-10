from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s, expected",
    [
        pytest.param("abb", [["a", "b", "b"], ["a", "bb"]], id="split-or-group-repetition"),
        pytest.param("z", [["z"]], id="single-character"),
        pytest.param(
            "aaa", [["a", "a", "a"], ["a", "aa"], ["aa", "a"], ["aaa"]], id="nested-palindromes"
        ),
    ],
)
def test_cases(s: str, expected: list[list[str]]) -> None:
    actual = solution(REFERENCE).partition(s)
    assert sorted(map(tuple, actual)) == sorted(map(tuple, expected))
