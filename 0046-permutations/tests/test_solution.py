from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "nums, expected",
    [
        pytest.param([4, 7], [[4, 7], [7, 4]], id="two-distinct-values"),
        pytest.param([-1], [[-1]], id="single-value"),
        pytest.param(
            [0, 1, 2],
            [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]],
            id="all-six-orders",
        ),
    ],
)
def test_cases(nums: list[int], expected: list[list[int]]) -> None:
    actual = solution(REFERENCE).permute(nums)
    assert sorted(map(tuple, actual)) == sorted(map(tuple, expected))
