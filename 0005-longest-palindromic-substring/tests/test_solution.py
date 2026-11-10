from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0005-longest-palindromic-substring.py"


def test_tied_odd_palindromes_and_even_center() -> None:
    solver = solution(REFERENCE)
    assert solver.longestPalindrome("babad") in {"bab", "aba"}
    assert solver.longestPalindrome("cbbd") == "bb"
    assert solver.longestPalindrome("a") == "a"
