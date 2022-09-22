import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1

    while q:
        x, y = q.popleft()

        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]

            if in_range(nx, ny) and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

T = int(sys.stdin.readline())

for _ in range(T):
    m, n, k = map(int, sys.stdin.readline().split())
    board = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        b_y, b_x = map(int, sys.stdin.readline().split())
        board[b_x][b_y] = 1

    for i in range(n):
        for j in range(m):
            if board[i][j] == 1 and not visited[i][j]:
                cnt += 1
                bfs(i, j)

    print(cnt)