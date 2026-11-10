from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "0143-reorder-list.py"


def test_alternates_front_and_back_in_place() -> None:
    solver = solution(REFERENCE)
    head = list_to_nodes([1, 2, 3, 4, 5])
    solver.reorderList(head)
    assert nodes_to_list(head) == [1, 5, 2, 4, 3]


def test_even_length_and_singleton() -> None:
    solver = solution(REFERENCE)
    for values, expected in (([1, 2, 3, 4], [1, 4, 2, 3]), ([8], [8])):
        head = list_to_nodes(values)
        solver.reorderList(head)
        assert nodes_to_list(head) == expected
