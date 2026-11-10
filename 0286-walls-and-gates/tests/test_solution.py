from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "rooms, expected",
    [
        pytest.param(
            [[0, 2147483647], [-1, 2147483647]], [[0, 1], [-1, 2]], id="distance-around-a-wall"
        ),
        pytest.param(
            [[0, 2147483647, 2147483647, 2147483647, 0]],
            [[0, 1, 2, 1, 0]],
            id="nearest-of-two-gates",
        ),
        pytest.param(
            [[0, -1, 2147483647]], [[0, -1, 2147483647]], id="unreachable-room-is-unchanged"
        ),
    ],
)
def test_cases(rooms: list[list[int]], expected: list[list[int]]) -> None:
    solution(REFERENCE).wallsAndGates(rooms)
    assert rooms == expected
