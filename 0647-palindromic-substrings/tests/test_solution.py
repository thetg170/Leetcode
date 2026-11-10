from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abba", 6),
        ("aaa", 6),
        ("abc", 3),
    ],
)
def test_solution(s: str, expected: int) -> None:
    assert solution(REFERENCE).countSubstrings(s) == expected
