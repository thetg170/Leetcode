from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "text1,text2,expected",
    [
        ("stone", "long", 2),
        ("abc", "def", 0),
        ("abca", "acba", 3),
    ],
)
def test_solution(text1: str, text2: str, expected: int) -> None:
    assert solution(REFERENCE).longestCommonSubsequence(text1, text2) == expected
