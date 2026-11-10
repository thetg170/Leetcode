from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,p,expected",
    [
        ("ccc", "bc*", False),
        ("aab", "c*a*b", True),
        ("ab", ".*c", False),
    ],
)
def test_solution(s: str, p: str, expected: bool) -> None:
    assert solution(REFERENCE).isMatch(s, p) is expected
