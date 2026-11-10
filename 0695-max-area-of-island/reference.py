# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited: set[tuple[int, int]] = set()
        largest = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0 or (row, col) in visited:
                    continue

                # Mark on discovery so each cell enters the stack once.
                stack = [(row, col)]
                visited.add((row, col))
                area = 0
                while stack:
                    r, c = stack.pop()
                    area += 1
                    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                        if (
                            0 <= nr < rows
                            and 0 <= nc < cols
                            and grid[nr][nc] == 1
                            and (nr, nc) not in visited
                        ):
                            visited.add((nr, nc))
                            stack.append((nr, nc))
                largest = max(largest, area)

        return largest
