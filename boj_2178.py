import sys
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if in_range(nx, ny) and board[nx][ny] == 1:
                queue.append((nx, ny))
                board[nx][ny] = board[x][y] + 1


n, m = map(int, sys.stdin.readline().split())
board = []

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

bfs(0, 0)
print(board[n-1][m-1])
