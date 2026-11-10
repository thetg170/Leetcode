from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "0206-reverse-linked-list.py"


def test_reverses_linked_list() -> None:
    solver = solution(REFERENCE)
    assert nodes_to_list(solver.reverseList(list_to_nodes([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]
    assert solver.reverseList(None) is None

