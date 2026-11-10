from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,expected",
    [
        ("112", 3),
        ("06", 0),
        ("2101", 1),
    ],
)
def test_solution(s: str, expected: int) -> None:
    assert solution(REFERENCE).numDecodings(s) == expected
