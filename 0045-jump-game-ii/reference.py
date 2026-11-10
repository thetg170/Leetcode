# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def jump(self, nums: list[int]) -> int:
        left, right = 0, 0
        res = 0
        while right < (len(nums) - 1):
            maxJump = 0
            for i in range(left, right + 1):
                maxJump = max(maxJump, i + nums[i])
            left = right + 1
            right = maxJump
            res += 1
        return res
