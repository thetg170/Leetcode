from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "0021-merge-two-sorted-lists.py"


def test_merges_in_order_with_duplicates() -> None:
    solver = solution(REFERENCE)
    actual = solver.mergeTwoLists(list_to_nodes([-2, 2, 4]), list_to_nodes([-2, 1, 5]))
    assert nodes_to_list(actual) == [-2, -2, 1, 2, 4, 5]


def test_accepts_an_empty_input() -> None:
    solver = solution(REFERENCE)
    assert nodes_to_list(solver.mergeTwoLists(None, list_to_nodes([2, 3]))) == [2, 3]
    assert solver.mergeTwoLists(None, None) is None
