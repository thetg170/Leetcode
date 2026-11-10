from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0209-minimum-size-subarray-sum.py"


def test_minimum_window_length() -> None:
    solver = solution(REFERENCE)
    assert solver.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
    assert solver.minSubArrayLen(4, [1, 4, 4]) == 1
    assert solver.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0

