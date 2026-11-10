# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

import collections


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        output = []
        q = collections.deque()  # index
        left = right = 0
        # O(n) O(n)
        while right < len(nums):
            # pop smaller values from q
            while q and nums[q[-1]] < nums[right]:
                q.pop()
            q.append(right)

            # remove left val from window
            if left > q[0]:
                q.popleft()

            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            right += 1

        return output
