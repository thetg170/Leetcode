from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "word1,word2,expected",
    [
        ("cart", "cut", 2),
        ("", "abc", 3),
        ("same", "same", 0),
    ],
)
def test_solution(word1: str, word2: str, expected: int) -> None:
    assert solution(REFERENCE).minDistance(word1, word2) == expected
