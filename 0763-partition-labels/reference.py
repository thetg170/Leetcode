# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        count = {}
        res = []
        i, length = 0, len(s)
        for j in range(length):
            c = s[j]
            count[c] = j

        curLen = 0
        goal = 0
        while i < length:
            c = s[i]
            goal = max(goal, count[c])
            curLen += 1

            if goal == i:
                res.append(curLen)
                curLen = 0
            i += 1
        return res
