from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_smallest_middle_and_largest_ranks() -> None:
    root = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.kthSmallest(root, 1) == 1
    assert solver.kthSmallest(root, 3) == 3
    assert solver.kthSmallest(root, 6) == 6


def test_single_node() -> None:
    assert solution(REFERENCE, TreeNode=TreeNode).kthSmallest(TreeNode(-2), 1) == -2
