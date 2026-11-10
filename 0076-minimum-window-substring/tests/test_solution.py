from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s, t, expected",
    [
        pytest.param("bbaacx", "aac", "aac", id="required-repeated-letter"),
        pytest.param("a", "aa", "", id="not-enough-copies"),
        pytest.param("zxa", "x", "x", id="single-required-character"),
    ],
)
def test_cases(s: str, t: str, expected: str) -> None:
    actual = solution(REFERENCE).minWindow(s, t)
    assert actual == expected
