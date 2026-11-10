from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_balanced_and_empty_trees() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.isBalanced(TreeNode(1, TreeNode(2), TreeNode(3, right=TreeNode(4)))) is True
    assert solver.isBalanced(None) is True


def test_imbalanced_below_a_balanced_root() -> None:
    left = TreeNode(2, TreeNode(3, TreeNode(4)))
    right = TreeNode(5, TreeNode(6))
    assert solution(REFERENCE, TreeNode=TreeNode).isBalanced(TreeNode(1, left, right)) is False
