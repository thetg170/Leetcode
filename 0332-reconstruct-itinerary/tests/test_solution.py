from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "tickets, expected",
    [
        pytest.param(
            [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "JFK"], ["ATL", "JFK"]],
            ["JFK", "ATL", "JFK", "SFO", "JFK"],
            id="lexically-smallest-valid-route",
        ),
        pytest.param(
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
            ["JFK", "NRT", "JFK", "KUL"],
            id="lexical-first-would-strand-a-ticket",
        ),
    ],
)
def test_cases(tickets: list[list[str]], expected: list[str]) -> None:
    actual = solution(REFERENCE).findItinerary(tickets)
    assert actual == expected
