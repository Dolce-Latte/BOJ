import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    cnt = 1

    while queue:
        x, y = queue.popleft()

        for idx in range(4):
            nx, ny = x + dx[idx], y + dy[idx]

            if in_range(nx, ny) and board[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))
                cnt += 1

    return cnt


n = int(sys.stdin.readline())

board = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

count = 0
estate = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            count += 1
            estate.append(bfs(i, j))

estate.sort()
print(count)
for elem in estate:
    print(elem)
