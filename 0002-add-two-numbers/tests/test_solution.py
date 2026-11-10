from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "0002-add-two-numbers.py"


def test_adds_reverse_order_digits() -> None:
    solver = solution(REFERENCE)
    result = solver.addTwoNumbers(list_to_nodes([2, 4, 3]), list_to_nodes([5, 6, 4]))
    assert nodes_to_list(result) == [7, 0, 8]


def test_carry_survives_the_last_digit() -> None:
    solver = solution(REFERENCE)
    result = solver.addTwoNumbers(list_to_nodes([9, 9]), list_to_nodes([1]))
    assert nodes_to_list(result) == [0, 0, 1]
    assert nodes_to_list(solver.addTwoNumbers(list_to_nodes([0]), list_to_nodes([0]))) == [0]
