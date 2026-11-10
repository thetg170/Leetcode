from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_best_path_need_not_include_root() -> None:
    root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert solution(REFERENCE, TreeNode=TreeNode).maxPathSum(root) == 42


def test_all_negative_tree_uses_one_node() -> None:
    root = TreeNode(-3, TreeNode(-8), TreeNode(-5))
    assert solution(REFERENCE, TreeNode=TreeNode).maxPathSum(root) == -3
