from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_reads_latest_value_at_or_before_timestamp() -> None:
    store = load_module(REFERENCE).TimeMap()
    store.set("device", "early", 2)
    store.set("device", "late", 5)
    assert store.get("device", 1) == ""
    assert store.get("device", 2) == "early"
    assert store.get("device", 4) == "early"
    assert store.get("device", 5) == "late"
    assert store.get("device", 9) == "late"


def test_histories_are_separate_by_key() -> None:
    store = load_module(REFERENCE).TimeMap()
    store.set("a", "one", 2)
    store.set("b", "two", 3)
    assert store.get("a", 3) == "one"
    assert store.get("b", 2) == ""
    assert store.get("b", 3) == "two"
    assert store.get("absent", 8) == ""
