from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_literal_and_wildcard_search() -> None:
    words = load_module(REFERENCE).WordDictionary()
    for word in ("bad", "dad", "mad", "bake"):
        words.addWord(word)
    assert words.search("pad") is False
    assert words.search("bad") is True
    assert words.search(".ad") is True
    assert words.search("b..e") is True


def test_wildcards_match_exactly_one_character() -> None:
    words = load_module(REFERENCE).WordDictionary()
    words.addWord("mint")
    assert words.search("....") is True
    assert words.search("...") is False
    assert words.search(".....") is False
