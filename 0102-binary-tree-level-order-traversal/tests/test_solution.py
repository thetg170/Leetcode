from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_groups_nodes_by_depth_and_left_to_right_order() -> None:
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution(REFERENCE, TreeNode=TreeNode).levelOrder(root) == [[3], [9, 20], [15, 7]]


def test_empty_tree_returns_no_levels() -> None:
    assert solution(REFERENCE, TreeNode=TreeNode).levelOrder(None) == []
