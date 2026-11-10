from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "temperatures, expected",
    [
        pytest.param([65, 66, 64, 70], [1, 2, 1, 0], id="warmer-after-a-gap"),
        pytest.param([72, 72, 71], [0, 0, 0], id="equal-is-not-warmer"),
        pytest.param([60], [0], id="single-day"),
    ],
)
def test_cases(temperatures: list[int], expected: list[int]) -> None:
    actual = solution(REFERENCE).dailyTemperatures(temperatures)
    assert actual == expected
