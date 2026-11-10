from pathlib import Path

from tests.support.assertions import normalized_nested
from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0049-group-anagrams.py"


def test_groups_anagrams_without_relying_on_output_order() -> None:
    solver = solution(REFERENCE)
    actual = solver.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    expected = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    assert normalized_nested(actual) == normalized_nested(expected)
    assert normalized_nested(solver.groupAnagrams([""])) == [("",)]

