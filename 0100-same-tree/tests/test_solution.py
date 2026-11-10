from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_identical_shape_and_values() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    assert solver.isSameTree(None, None) is True
    assert solver.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, TreeNode(2))) is True


def test_values_and_child_positions_both_matter() -> None:
    solver = solution(REFERENCE, TreeNode=TreeNode)
    first = TreeNode(1, TreeNode(2))
    assert solver.isSameTree(first, TreeNode(1, right=TreeNode(2))) is False
    assert solver.isSameTree(first, TreeNode(1, TreeNode(3))) is False
