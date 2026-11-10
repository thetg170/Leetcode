from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n,expected",
    [
        (7, True),
        (2, False),
        (1, True),
    ],
)
def test_solution(n: int, expected: bool) -> None:
    assert solution(REFERENCE).isHappy(n) is expected
