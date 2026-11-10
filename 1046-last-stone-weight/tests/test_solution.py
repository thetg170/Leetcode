from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "stones, expected",
    [
        pytest.param([8, 5, 4], 1, id="different-stone-weights"),
        pytest.param([4, 4], 0, id="equal-stones-cancel"),
        pytest.param([8], 8, id="single-stone"),
    ],
)
def test_cases(stones: list[int], expected: int) -> None:
    actual = solution(REFERENCE).lastStoneWeight(stones)
    assert actual == expected
