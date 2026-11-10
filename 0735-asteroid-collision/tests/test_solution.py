from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0735-asteroid-collision.py"


def test_collisions() -> None:
    solver = solution(REFERENCE)
    assert solver.asteroidCollision([5, 10, -5]) == [5, 10]
    assert solver.asteroidCollision([8, -8]) == []
    assert solver.asteroidCollision([10, 2, -5]) == [10]
    assert solver.asteroidCollision([-2, -1, 1, 2]) == [-2, -1, 1, 2]

