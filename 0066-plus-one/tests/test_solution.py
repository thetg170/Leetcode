from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0066-plus-one.py"


@pytest.mark.parametrize(
    "digits, expected",
    [
        ([1, 2, 9], [1, 3, 0]),
        ([9, 9], [1, 0, 0]),
        ([0], [1]),
    ],
)
def test_examples(digits, expected) -> None:
    assert solution(REFERENCE).plusOne(digits) == expected
