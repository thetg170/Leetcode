from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0242-valid-anagram.py"


def test_anagrams() -> None:
    solver = solution(REFERENCE)
    assert solver.isAnagram("anagram", "nagaram") is True
    assert solver.isAnagram("rat", "car") is False
    assert solver.isAnagram("aacc", "ccac") is False

