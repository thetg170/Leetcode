from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_removes_internal_node_and_tail() -> None:
    solver = solution(REFERENCE)
    result = solver.removeNthFromEnd(list_to_nodes([1, 2, 3, 4, 5]), 2)
    assert nodes_to_list(result) == [1, 2, 3, 5]
    result = solver.removeNthFromEnd(list_to_nodes([6, 7, 8]), 1)
    assert nodes_to_list(result) == [6, 7]


def test_removes_head_or_only_node() -> None:
    solver = solution(REFERENCE)
    assert nodes_to_list(solver.removeNthFromEnd(list_to_nodes([1, 2]), 2)) == [2]
    assert solver.removeNthFromEnd(list_to_nodes([1]), 1) is None
