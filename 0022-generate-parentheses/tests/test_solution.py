from pathlib import Path

from tests.support.loader import solution

REFERENCE = Path(__file__).parents[1] / "0022-generate-parentheses.py"


def test_small_and_nested_combinations() -> None:
    solver = solution(REFERENCE)
    assert solver.generateParenthesis(1) == ["()"]
    assert sorted(solver.generateParenthesis(3)) == [
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    ]
