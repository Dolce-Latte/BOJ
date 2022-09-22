import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(x, y):
    each_cnt = 1
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if in_range(nx, ny) and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny))
                each_cnt += 1

    return each_cnt


n, m = map(int, sys.stdin.readline().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

board = []
visited = [[0] * m for _ in range(n)]
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

cnt, max_cnt = 0, 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            cnt += 1
            max_cnt = max(max_cnt, bfs(i, j))

print(cnt)
print(max_cnt)
