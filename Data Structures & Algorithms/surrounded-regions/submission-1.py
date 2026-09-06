from collections import deque
from typing import List


class Solution:

  def solve(self, board: List[List[str]]) -> None:
    if not board:
      return

    ROWS, COLS = len(board), len(board[0])
    q = deque()

    # 1. Collect all border 'O's
    for r in range(ROWS):
      for c in range(COLS):
        if (
            r in (0, ROWS - 1) or c in (0, COLS - 1)
        ) and board[r][c] == "O":
          q.append((r, c))
          board[r][c] = "T"  # Mark safe

    # 2. BFS to mark all connected interior 'O's as safe ('T')
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q:
      r, c = q.popleft()
      for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] == "O":
          board[nr][nc] = "T"
          q.append((nr, nc))

    # 3. Capture surrounded 'O's -> 'X' and restore safe 'T's -> 'O'
    for r in range(ROWS):
      for c in range(COLS):
        if board[r][c] == "O":
          board[r][c] = "X"
        elif board[r][c] == "T":
          board[r][c] = "O"