from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "0295-find-median-from-data-stream.py"


def test_running_median() -> None:
    finder = load_module(REFERENCE).MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2

