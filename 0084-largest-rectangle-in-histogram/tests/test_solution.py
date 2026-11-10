from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "heights, expected",
    [
        pytest.param([3, 1, 3, 3], 6, id="adjacent-tall-bars"),
        pytest.param([0, 0], 0, id="all-zero"),
        pytest.param([2, 1, 2], 3, id="best-rectangle-spans-a-valley"),
    ],
)
def test_cases(heights: list[int], expected: int) -> None:
    actual = solution(REFERENCE).largestRectangleArea(heights)
    assert actual == expected
