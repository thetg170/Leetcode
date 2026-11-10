from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n,expected",
    [
        (12, 805306368),
        (2, 1073741824),
        (0, 0),
    ],
)
def test_solution(n: int, expected: int) -> None:
    assert solution(REFERENCE).reverseBits(n) == expected
