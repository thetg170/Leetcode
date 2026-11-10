from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0438-find-all-anagrams-in-a-string.py"


def test_anagram_start_indices() -> None:
    solver = solution(REFERENCE)
    assert solver.findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert solver.findAnagrams("abab", "ab") == [0, 1, 2]
    assert solver.findAnagrams("a", "ab") == []

