from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_compares_against_every_ancestor() -> None:
    root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
    assert solution(REFERENCE, TreeNode=TreeNode).goodNodes(root) == 4


def test_equal_negative_values_count_as_good() -> None:
    root = TreeNode(-1, TreeNode(-2), TreeNode(-1))
    assert solution(REFERENCE, TreeNode=TreeNode).goodNodes(root) == 2
