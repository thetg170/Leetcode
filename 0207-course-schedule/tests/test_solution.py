from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "numCourses, prerequisites, expected",
    [
        pytest.param(4, [[1, 0], [2, 1], [0, 2]], False, id="cycle-and-an-independent-course"),
        pytest.param(
            4, [[1, 0], [2, 0], [3, 1], [3, 2]], True, id="converging-acyclic-prerequisites"
        ),
        pytest.param(1, [], True, id="no-prerequisites"),
    ],
)
def test_cases(numCourses: int, prerequisites: list[list[int]], expected: bool) -> None:
    actual = solution(REFERENCE).canFinish(numCourses, prerequisites)
    assert actual is expected
