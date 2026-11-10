from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_word_lookup_distinguishes_prefixes() -> None:
    trie = load_module(REFERENCE).Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.startsWith("app") is True
    trie.insert("app")
    assert trie.search("app") is True


def test_unrelated_prefixes_and_separate_instances() -> None:
    trie_type = load_module(REFERENCE).Trie
    first, second = trie_type(), trie_type()
    first.insert("banana")
    assert first.startsWith("orange") is False
    assert first.startsWith("ban") is True
    assert second.search("banana") is False
