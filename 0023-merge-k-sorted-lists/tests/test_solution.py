from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes, nodes_to_list

REFERENCE = Path(__file__).parents[1] / "0023-merge-k-sorted-lists.py"


def test_merges_multiple_lists_and_skips_empty_ones() -> None:
    solver = solution(REFERENCE)
    lists = [list_to_nodes(values) for values in [[-4, 3], [], [-4, 1], [0, 5]]]
    assert nodes_to_list(solver.mergeKLists(lists)) == [-4, -4, 0, 1, 3, 5]


def test_no_nodes_returns_none() -> None:
    solver = solution(REFERENCE)
    assert solver.mergeKLists([]) is None
    assert solver.mergeKLists([None, None]) is None
