# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] != "1" or (row, col) in visited:
                    continue
                islands += 1
                visited.add((row, col))
                stack = [(row, col)]
                while stack:
                    r, c = stack.pop()
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == "1"
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))
        return islands
