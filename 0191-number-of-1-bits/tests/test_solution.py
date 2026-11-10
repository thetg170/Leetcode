from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n,expected",
    [
        (42, 3),
        (128, 1),
        (2147483647, 31),
    ],
)
def test_solution(n: int, expected: int) -> None:
    assert solution(REFERENCE).hammingWeight(n) == expected
