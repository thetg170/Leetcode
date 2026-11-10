from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,expected",
    [
        ("(*()", True),
        ("*(", False),
        ("(*))", True),
    ],
)
def test_solution(s: str, expected: bool) -> None:
    assert solution(REFERENCE).checkValidString(s) is expected
