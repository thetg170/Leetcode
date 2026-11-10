from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import GraphNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_clones_a_cycle_without_reusing_original_nodes() -> None:
    first, second, third = GraphNode(1), GraphNode(2), GraphNode(3)
    first.neighbors = [second, third]
    second.neighbors = [first, third]
    third.neighbors = [first, second]

    clone = solution(REFERENCE, Node=GraphNode).cloneGraph(first)
    assert clone is not None and clone is not first and clone.val == 1
    assert len(clone.neighbors) == 2
    copies = {node.val: node for node in clone.neighbors}
    assert set(copies) == {2, 3}
    assert copies[2] is not second and copies[3] is not third
    assert len(copies[2].neighbors) == len(copies[3].neighbors) == 2
    assert any(node is clone for node in copies[2].neighbors)
    assert any(node is copies[3] for node in copies[2].neighbors)
    assert any(node is clone for node in copies[3].neighbors)
    assert any(node is copies[2] for node in copies[3].neighbors)


def test_clones_empty_graph_and_isolated_node() -> None:
    solver = solution(REFERENCE, Node=GraphNode)
    assert solver.cloneGraph(None) is None
    original = GraphNode(1)
    copy = solver.cloneGraph(original)
    assert copy is not None and copy is not original
    assert copy.val == 1 and copy.neighbors == []
