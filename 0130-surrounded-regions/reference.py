# Adapted from neetcode-gh/leetcode (MIT). See practice/neetcode-reference-LICENSE.txt.

from __future__ import annotations


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows, cols = len(board), len(board[0])
        boundary = (
            {(r, 0) for r in range(rows)}
            | {(r, cols - 1) for r in range(rows)}
            | {(0, c) for c in range(cols)}
            | {(rows - 1, c) for c in range(cols)}
        )
        safe = {(r, c) for r, c in boundary if board[r][c] == "O"}
        stack = list(safe)
        # Any O connected to the boundary must remain unchanged.
        while stack:
            r, c = stack.pop()
            for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if (
                    0 <= nr < rows
                    and 0 <= nc < cols
                    and board[nr][nc] == "O"
                    and (nr, nc) not in safe
                ):
                    safe.add((nr, nc))
                    stack.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
