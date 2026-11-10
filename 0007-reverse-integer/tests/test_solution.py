from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0007-reverse-integer.py"


@pytest.mark.parametrize(
    "value, expected",
    [
        (123, 321),
        (-120, -21),
        (0, 0),
        (1534236469, 0),
        (-2147483648, 0),
    ],
)
def test_examples(value, expected) -> None:
    assert solution(REFERENCE).reverse(value) == expected
