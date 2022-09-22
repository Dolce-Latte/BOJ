import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < m and 0 <= y < n


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]

            if in_range(nx, ny) and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
    return


dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

m, n = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0] * n for _ in range(m)]
cnt = 0
for i in range(m):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            bfs(i, j)

print(cnt)
