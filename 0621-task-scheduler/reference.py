# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations

import collections


class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        counter = collections.Counter(tasks)
        max_count = max(counter.values())
        min_time = (max_count - 1) * (n + 1) + sum(
            map(lambda count: count == max_count, counter.values())
        )

        return max(min_time, len(tasks))
