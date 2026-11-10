from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0125-valid-palindrome.py"


def test_ignores_case_and_non_alphanumeric_characters() -> None:
    solver = solution(REFERENCE)
    assert solver.isPalindrome("A man, a plan, a canal: Panama") is True
    assert solver.isPalindrome("race a car") is False
    assert solver.isPalindrome(" ") is True
    assert solver.isPalindrome("0P") is False

