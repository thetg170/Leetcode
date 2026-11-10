from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import RandomListNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_copies_links_and_random_targets_without_aliasing() -> None:
    head, middle, tail = RandomListNode(7), RandomListNode(13), RandomListNode(7)
    head.next, middle.next = middle, tail
    head.random, middle.random, tail.random = tail, head, tail

    result = solution(REFERENCE, Node=RandomListNode).copyRandomList(head)
    assert result is not None and result.next is not None and result.next.next is not None
    cloned_middle, cloned_tail = result.next, result.next.next
    assert [result.val, cloned_middle.val, cloned_tail.val] == [7, 13, 7]
    originals = (head, middle, tail)
    assert all(
        copy is not original
        for copy in (result, cloned_middle, cloned_tail)
        for original in originals
    )
    assert result.random is cloned_tail
    assert cloned_middle.random is result
    assert cloned_tail.random is cloned_tail
    assert cloned_tail.next is None
    assert head.next is middle and middle.next is tail and head.random is tail


def test_copies_empty_and_singleton_lists() -> None:
    solver = solution(REFERENCE, Node=RandomListNode)
    assert solver.copyRandomList(None) is None
    original = RandomListNode(3)
    copy = solver.copyRandomList(original)
    assert copy is not None and copy is not original
    assert copy.val == 3 and copy.next is None and copy.random is None
