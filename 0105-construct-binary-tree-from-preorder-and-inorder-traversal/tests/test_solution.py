from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def tree_shape(node: TreeNode | None) -> tuple | None:
    if node is None:
        return None
    return node.val, tree_shape(node.left), tree_shape(node.right)


def test_reconstructs_asymmetric_tree() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    root = solver.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
    assert tree_shape(root) == (3, (9, None, None), (20, (15, None, None), (7, None, None)))


def test_reconstructs_a_one_sided_tree() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    root = solver.buildTree([1, 2, 3], [3, 2, 1])
    assert tree_shape(root) == (1, (2, (3, None, None), None), None)
