from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "s,expected",
    [
        ("abacddc", [3, 4]),
        ("eccbbbbdec", [10]),
        ("abc", [1, 1, 1]),
    ],
)
def test_solution(s: str, expected: list[int]) -> None:
    assert solution(REFERENCE).partitionLabels(s) == expected
