from pathlib import Path

import pytest

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "reference.py"


@pytest.mark.parametrize(
    "tokens, expected",
    [
        pytest.param(["7", "3", "-", "2", "*"], 8, id="subtraction-order"),
        pytest.param(["-7", "3", "/"], -2, id="negative-division-toward-zero"),
        pytest.param(["-11"], -11, id="single-token"),
    ],
)
def test_cases(tokens: list[str], expected: int) -> None:
    actual = solution(REFERENCE).evalRPN(tokens)
    assert actual == expected
