from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0907-koko-eating-bananas.py"


def test_minimum_eating_speed() -> None:
    solver = solution(REFERENCE)
    assert solver.minEatingSpeed([3, 6, 7, 11], 8) == 4
    assert solver.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
    assert solver.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23

