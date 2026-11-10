from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "0303-range-sum-query-immutable.py"


def test_range_sum_queries() -> None:
    array = load_module(REFERENCE).NumArray([-2, 0, 3, -5, 2, -1])
    assert array.sumRange(0, 2) == 1
    assert array.sumRange(2, 5) == -1
    assert array.sumRange(0, 5) == -3

