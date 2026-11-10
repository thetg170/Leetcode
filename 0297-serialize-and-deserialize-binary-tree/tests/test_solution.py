from pathlib import Path

from tests.support.loader import load_module
from tests.support.nodes import TreeNode

REFERENCE = Path(__file__).parents[1] / "reference.py"


def tree_shape(node: TreeNode | None) -> tuple | None:
    if node is None:
        return None
    return node.val, tree_shape(node.left), tree_shape(node.right)


def test_encoding_preserves_shape_and_signed_values() -> None:
    codec = load_module(REFERENCE, TreeNode=TreeNode).Codec
    root = TreeNode(1, TreeNode(-2, right=TreeNode(6)), TreeNode(3))
    expected = (1, (-2, None, (6, None, None)), (3, None, None))
    encoded = codec().serialize(root)

    assert isinstance(encoded, str)
    assert tree_shape(codec().deserialize(encoded)) == expected


def test_empty_and_single_node_trees() -> None:
    codec = load_module(REFERENCE, TreeNode=TreeNode).Codec
    assert codec().deserialize(codec().serialize(None)) is None
    assert tree_shape(codec().deserialize(codec().serialize(TreeNode(-1)))) == (-1, None, None)
