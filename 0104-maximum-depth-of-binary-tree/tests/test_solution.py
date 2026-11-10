from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_depth_follows_longest_branch() -> None:
    root = TreeNode(7, TreeNode(3, right=TreeNode(5)), TreeNode(9))
    assert solution(REFERENCE, TreeNode=TreeNode).maxDepth(root) == 3


def test_empty_tree_and_singleton() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.maxDepth(None) == 0
    assert solver.maxDepth(TreeNode(8)) == 1
