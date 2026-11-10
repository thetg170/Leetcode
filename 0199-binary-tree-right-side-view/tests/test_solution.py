from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_deeper_left_branch_becomes_visible() -> None:
    left = TreeNode(2, right=TreeNode(5, right=TreeNode(7)))
    root = TreeNode(1, left, TreeNode(3, right=TreeNode(4)))
    assert solution(REFERENCE, TreeNode=TreeNode).rightSideView(root) == [1, 3, 4, 7]


def test_empty_tree_and_left_chain() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.rightSideView(None) == []
    assert solver.rightSideView(TreeNode(1, TreeNode(2))) == [1, 2]
