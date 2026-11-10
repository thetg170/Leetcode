from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "0146-lru-cache.py"


def test_read_refreshes_recency() -> None:
    cache = load_module(REFERENCE).LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    assert cache.get(1) == 10

    cache.put(3, 30)
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 30


def test_update_refreshes_recency() -> None:
    cache = load_module(REFERENCE).LRUCache(2)
    cache.put(1, 10)
    cache.put(2, 20)
    cache.put(1, 99)
    cache.put(3, 30)
    assert cache.get(2) == -1
    assert cache.get(1) == 99
    assert cache.get(3) == 30
