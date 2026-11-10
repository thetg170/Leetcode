from pathlib import Path

from tests.support.loader import solution
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def test_exact_nested_subtree_matches() -> None:
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
    candidate = TreeNode(4, TreeNode(1), TreeNode(2))
    assert solution(REFERENCE, TreeNode=TreeNode).isSubtree(root, candidate) is True


def test_extra_descendant_prevents_match() -> None:
    root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
    candidate = TreeNode(4, TreeNode(1), TreeNode(2))
    assert solution(REFERENCE, TreeNode=TreeNode).isSubtree(root, candidate) is False
