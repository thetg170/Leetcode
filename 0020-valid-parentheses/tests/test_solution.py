from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0020-valid-parentheses.py"


def test_parentheses_validation() -> None:
    solver = solution(REFERENCE)
    assert solver.isValid("()") is True
    assert solver.isValid("()[]{}") is True
    assert solver.isValid("(]") is False
    assert solver.isValid("([)]") is False
    assert solver.isValid("{") is False

