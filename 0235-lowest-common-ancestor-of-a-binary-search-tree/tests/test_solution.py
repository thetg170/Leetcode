from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_nodes_in_opposite_branches() -> None:
    left, right = TreeNode(2), TreeNode(8)
    root = TreeNode(6, left, right)
    assert solution(REFERENCE, TreeNode=TreeNode).lowestCommonAncestor(root, left, right) is root


def test_one_node_is_the_ancestor_of_the_other() -> None:
    descendant = TreeNode(4)
    ancestor = TreeNode(2, TreeNode(0), descendant)
    root = TreeNode(6, ancestor, TreeNode(8))
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.lowestCommonAncestor(root, descendant, ancestor) is ancestor
