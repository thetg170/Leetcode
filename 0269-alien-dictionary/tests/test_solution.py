from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_includes_all_letters_and_obeys_discovered_order() -> None:
    actual = solution(REFERENCE).alienOrder(["ax", "ay", "by"])

    assert sorted(actual) == ["a", "b", "x", "y"]
    assert actual.index("a") < actual.index("b")
    assert actual.index("x") < actual.index("y")


@pytest.mark.parametrize("words", [["abc", "ab"], ["z", "x", "z"]], ids=["bad-prefix", "cycle"])
def test_rejects_inconsistent_dictionary(words: list[str]) -> None:
    assert solution(REFERENCE).alienOrder(words) == ""
