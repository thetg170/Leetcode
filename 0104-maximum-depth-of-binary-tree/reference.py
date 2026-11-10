# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

from collections import deque

from tests.support.nodes import TreeNode


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        q = deque()
        if root:
            q.append(root)

        level = 0

        while q:
            for _i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level
