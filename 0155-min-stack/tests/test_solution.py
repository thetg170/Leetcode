from pathlib import Path

from tests.support.loader import load_module

REFERENCE = Path(__file__).parents[1] / "0155-min-stack.py"


def test_min_stack_operations() -> None:
    stack = load_module(REFERENCE).MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.getMin() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.getMin() == -2
