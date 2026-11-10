from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "target, position, speed, expected",
    [
        pytest.param(12, [9, 6, 1], [1, 2, 1], 2, id="catch-at-target"),
        pytest.param(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3, id="unsorted-positions-and-merges"),
        pytest.param(10, [3], [4], 1, id="single-car"),
    ],
)
def test_cases(target: int, position: list[int], speed: list[int], expected: int) -> None:
    actual = solution(REFERENCE).carFleet(target, position, speed)
    assert actual == expected
