from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_repeated_values_and_changes_to_kth_largest() -> None:
    stream = load_module(REFERENCE).KthLargest(3, [4, 5, 8, 2])
    actual = [stream.add(value) for value in [3, 5, 10, 9, 4]]
    assert actual == [4, 5, 5, 8, 8]


def test_k_one_with_initially_empty_stream() -> None:
    stream = load_module(REFERENCE).KthLargest(1, [])
    assert stream.add(-3) == -3
    assert stream.add(-8) == -3
    assert stream.add(0) == 0
