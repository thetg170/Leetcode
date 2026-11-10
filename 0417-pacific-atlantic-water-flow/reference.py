# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        rows, cols = len(heights), len(heights[0])

        def reachable_from(coast: set[tuple[int, int]]) -> set[tuple[int, int]]:
            reached = coast.copy()
            stack = list(coast)
            while stack:
                r, c = stack.pop()
                # Walk opposite the flow of water, from the ocean uphill.
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if (
                        0 <= nr < rows
                        and 0 <= nc < cols
                        and heights[nr][nc] >= heights[r][c]
                        and (nr, nc) not in reached
                    ):
                        reached.add((nr, nc))
                        stack.append((nr, nc))
            return reached

        pacific = {(r, 0) for r in range(rows)} | {(0, c) for c in range(cols)}
        atlantic = {(r, cols - 1) for r in range(rows)} | {(rows - 1, c) for c in range(cols)}
        both = reachable_from(pacific) & reachable_from(atlantic)
        return [[r, c] for r, c in both]
