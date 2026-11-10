# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

from heapq import heapify, heappop


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapify(nums)
        while len(nums) > k:
            heappop(nums)
        return nums[0]
