from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_diameter_can_stay_below_root() -> None:
    left = TreeNode(2, TreeNode(3, TreeNode(4)), TreeNode(5, TreeNode(6)))
    root = TreeNode(1, left)
    assert solution(REFERENCE, TreeNode=TreeNode).diameterOfBinaryTree(root) == 4


def test_single_node_has_zero_edges() -> None:
    assert solution(REFERENCE, TreeNode=TreeNode).diameterOfBinaryTree(TreeNode(1)) == 0
