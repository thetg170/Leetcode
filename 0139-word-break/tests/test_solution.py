from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,wordDict,expected",
    [
        ("redblueblue", ["red", "blue"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        ("cars", ["car", "ca", "rs"], True),
    ],
)
def test_solution(s: str, wordDict: list[str], expected: bool) -> None:
    assert solution(REFERENCE).wordBreak(s, wordDict) is expected
