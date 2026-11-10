from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0042-trapping-rain-water.py"


@pytest.mark.parametrize(
    "height, expected",
    [
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 2, 3, 4], 0),
        ([3, 0, 3], 3),
        ([2], 0),
    ],
)
def test_examples(height, expected) -> None:
    assert solution(REFERENCE).trap(height) == expected
