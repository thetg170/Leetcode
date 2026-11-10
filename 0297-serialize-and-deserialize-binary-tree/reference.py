# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

from tests.support.nodes import TreeNode


class Codec:
    def serialize(self, root: TreeNode | None) -> str:
        tokens = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node is None:
                tokens.append("N")
            else:
                tokens.append(str(node.val))
                # Visit left before right in preorder.
                stack.append(node.right)
                stack.append(node.left)
        return ",".join(tokens)

    def deserialize(self, data: str) -> TreeNode | None:
        tokens = iter(data.split(","))
        first = next(tokens)
        if first == "N":
            return None

        root = TreeNode(int(first))
        # Pending child positions, in the same preorder as serialization.
        pending = [(root, "right"), (root, "left")]
        for token in tokens:
            parent, side = pending.pop()
            if token != "N":
                child = TreeNode(int(token))
                setattr(parent, side, child)
                pending.append((child, "right"))
                pending.append((child, "left"))
        return root
