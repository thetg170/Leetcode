# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

from tests.support.nodes import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode | None) -> int:
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            return 1 + max(left, right)

        dfs(root)
        return res
