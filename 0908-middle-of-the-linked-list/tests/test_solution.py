from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "0908-middle-of-the-linked-list.py"


def test_returns_second_middle_for_even_length() -> None:
    solver = solution(REFERENCE)
    assert nodes_to_list(solver.middleNode(list_to_nodes([1, 2, 3, 4, 5]))) == [3, 4, 5]
    assert nodes_to_list(solver.middleNode(list_to_nodes([1, 2, 3, 4, 5, 6]))) == [4, 5, 6]

