# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

from tests.support.nodes import TreeNode


class Solution:
    def invertTree(self, root: TreeNode | None) -> TreeNode | None:
        if not root:
            return None

        # swap the children
        root.left, root.right = root.right, root.left

        # make 2 recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
