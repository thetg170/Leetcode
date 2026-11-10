from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0003-longest-substring-without-repeating-characters.py"


def test_longest_unique_window() -> None:
    solver = solution(REFERENCE)
    assert solver.lengthOfLongestSubstring("abcabcbb") == 3
    assert solver.lengthOfLongestSubstring("bbbbb") == 1
    assert solver.lengthOfLongestSubstring("pwwkew") == 3
    assert solver.lengthOfLongestSubstring("") == 0
    assert solver.lengthOfLongestSubstring("dvdf") == 3
