from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_orders_all_courses_after_prerequisites() -> None:
    prerequisites = [[1, 0], [3, 1], [2, 3], [4, 0]]
    actual = solution(REFERENCE).findOrder(5, prerequisites)

    assert sorted(actual) == list(range(5))
    positions = {course: index for index, course in enumerate(actual)}
    assert all(positions[dependency] < positions[course] for course, dependency in prerequisites)


def test_cycle_has_no_order() -> None:
    assert solution(REFERENCE).findOrder(3, [[0, 1], [1, 0]]) == []
