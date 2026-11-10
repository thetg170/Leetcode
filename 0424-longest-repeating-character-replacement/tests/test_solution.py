from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0424-longest-repeating-character-replacement.py"


def test_longest_replacement_window() -> None:
    solver = solution(REFERENCE)
    assert solver.characterReplacement("ABAB", 2) == 4
    assert solver.characterReplacement("AABABBA", 1) == 4
    assert solver.characterReplacement("AAAA", 0) == 4

