from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "num1,num2,expected",
    [
        ("17", "24", "408"),
        ("0", "1234", "0"),
        ("99", "99", "9801"),
    ],
)
def test_solution(num1: str, num2: str, expected: str) -> None:
    assert solution(REFERENCE).multiply(num1, num2) == expected
