from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s1,s2,s3,expected",
    [
        ("ab", "xy", "axby", True),
        ("aabcc", "dbbca", "aadbbbaccc", False),
        ("", "", "", True),
    ],
)
def test_solution(s1: str, s2: str, s3: str, expected: bool) -> None:
    assert solution(REFERENCE).isInterleave(s1, s2, s3) is expected
