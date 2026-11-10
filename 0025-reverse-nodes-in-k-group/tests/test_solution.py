from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_reverses_only_complete_groups() -> None:
    solver = solution(REFERENCE)
    for k, expected in ((2, [2, 1, 4, 3, 5]), (3, [3, 2, 1, 4, 5])):
        head = list_to_nodes([1, 2, 3, 4, 5])
        assert nodes_to_list(solver.reverseKGroup(head, k)) == expected


def test_groups_of_one_keep_order() -> None:
    solver = solution(REFERENCE)
    assert nodes_to_list(solver.reverseKGroup(list_to_nodes([1, 2]), 1)) == [1, 2]
