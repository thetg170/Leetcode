from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_accepts_valid_tree() -> None:
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    assert solution(REFERENCE, TreeNode=TreeNode).isValidBST(root) is True


def test_rejects_ancestor_bound_violations_and_duplicates() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert (
        solver.isValidBST(TreeNode(5, TreeNode(1), TreeNode(8, TreeNode(4), TreeNode(9)))) is False
    )
    assert solver.isValidBST(TreeNode(2, TreeNode(2))) is False
