from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        pytest.param("cab", "qbaacbx", True, id="permutation-inside-string"),
        pytest.param("ab", "eidboaoo", False, id="same-letters-with-gaps"),
        pytest.param("aab", "abb", False, id="repeated-letter-shortfall"),
    ],
)
def test_cases(s1: str, s2: str, expected: bool) -> None:
    actual = solution(REFERENCE).checkInclusion(s1, s2)
    assert actual is expected
