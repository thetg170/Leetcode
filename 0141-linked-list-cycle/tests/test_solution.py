from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import list_to_nodes

REFERENCE = Path(__file__).parents[1] / "0141-linked-list-cycle.py"


def test_detects_cycle() -> None:
    solver = solution(REFERENCE)
    head = list_to_nodes([3, 2, 0, -4])
    assert head is not None and head.next is not None
    tail = head
    while tail.next is not None:
        tail = tail.next
    tail.next = head.next
    assert solver.hasCycle(head) is True
    assert solver.hasCycle(list_to_nodes([1, 2])) is False
    assert solver.hasCycle(None) is False

