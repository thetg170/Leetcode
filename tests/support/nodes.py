from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field


@dataclass(eq=False)
class ListNode:
    val: int = 0
    next: ListNode | None = None


@dataclass(eq=False)
class Node:
    val: int = 0
    prev: Node | None = None
    next: Node | None = None
    child: Node | None = None


@dataclass(eq=False)
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


@dataclass(eq=False)
class GraphNode:
    val: int = 0
    neighbors: list[GraphNode] = field(default_factory=list)


@dataclass(eq=False)
class RandomListNode:
    val: int = 0
    next: RandomListNode | None = None
    random: RandomListNode | None = None


def list_to_nodes(values: Iterable[int]) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def nodes_to_list(head: ListNode | None, *, limit: int = 10_000) -> list[int]:
    values: list[int] = []
    current = head
    while current is not None:
        if len(values) >= limit:
            raise AssertionError("linked list exceeded limit; it may contain a cycle")
        values.append(current.val)
        current = current.next
    return values

