from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "beginWord, endWord, wordList, expected",
    [
        pytest.param("cat", "dog", ["cot", "dot", "dog", "bat"], 4, id="counts-both-endpoints"),
        pytest.param("hit", "cog", ["hot", "dot", "dog"], 0, id="target-not-in-word-list"),
        pytest.param("a", "c", ["b", "c"], 2, id="direct-transition"),
    ],
)
def test_cases(beginWord: str, endWord: str, wordList: list[str], expected: int) -> None:
    actual = solution(REFERENCE).ladderLength(beginWord, endWord, wordList)
    assert actual == expected
