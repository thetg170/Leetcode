# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

import collections

from tests.support.nodes import TreeNode


class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        q = collections.deque([root])

        while q:
            rightSide = None
            qLen = len(q)

            for _i in range(qLen):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val)
        return res
