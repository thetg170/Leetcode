from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,t,expected",
    [
        ("ababa", "aba", 4),
        ("aaaa", "aa", 6),
        ("abc", "d", 0),
    ],
)
def test_solution(s: str, t: str, expected: int) -> None:
    assert solution(REFERENCE).numDistinct(s, t) == expected
