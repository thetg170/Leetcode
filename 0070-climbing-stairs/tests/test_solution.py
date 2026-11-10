from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0070-climbing-stairs.py"


@pytest.mark.parametrize(
    "n, expected",
    [
        (1, 1),
        (2, 2),
        (5, 8),
        (10, 89),
    ],
)
def test_examples(n, expected) -> None:
    assert solution(REFERENCE).climbStairs(n) == expected
