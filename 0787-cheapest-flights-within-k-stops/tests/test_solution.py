from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "n, flights, src, dst, k, expected",
    [
        pytest.param(
            4,
            [[0, 1, 4], [1, 2, 4], [2, 3, 4], [0, 3, 20]],
            0,
            3,
            1,
            20,
            id="cheapest-route-exceeds-stop-limit",
        ),
        pytest.param(
            3, [[0, 1, 5], [1, 2, 7], [0, 2, 20]], 0, 2, 1, 12, id="allow-exactly-one-stop"
        ),
        pytest.param(3, [[0, 1, 5], [1, 2, 7]], 0, 2, 0, -1, id="unreachable-without-a-stop"),
    ],
)
def test_cases(n: int, flights: list[list[int]], src: int, dst: int, k: int, expected: int) -> None:
    actual = solution(REFERENCE).findCheapestPrice(n, flights, src, dst, k)
    assert actual == expected
