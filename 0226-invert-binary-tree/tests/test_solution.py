from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def tree_shape(node: TreeNode | None) -> tuple | None:
    if node is None:
        return None
    return node.val, tree_shape(node.left), tree_shape(node.right)


def test_swaps_both_levels_of_an_asymmetric_tree() -> None:
    root = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3, right=TreeNode(5)))
    inverted = solution(REFERENCE, TreeNode=TreeNode).invertTree(root)
    assert tree_shape(inverted) == (1, (3, (5, None, None), None), (2, None, (4, None, None)))


def test_empty_tree_and_singleton() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.invertTree(None) is None
    assert tree_shape(solver.invertTree(TreeNode(4))) == (4, None, None)
