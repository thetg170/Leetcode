# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        if n == 0:
            return not edges
        if len(edges) != n - 1:
            return False

        neighbors = [[] for _ in range(n)]
        for left, right in edges:
            neighbors[left].append(right)
            neighbors[right].append(left)

        visited = {0}
        stack = [0]
        while stack:
            node = stack.pop()
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return len(visited) == n
