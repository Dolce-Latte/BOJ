import sys
from collections import deque


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


m, n = map(int, sys.stdin.readline().split())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
storage = []
queue = deque()

for _ in range(n):
    storage.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(m):
        if storage[i][j] == 1:
            queue.append((i, j))

while queue:
    x, y = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if in_range(nx, ny) and storage[nx][ny] == 0:
            queue.append((nx, ny))
            storage[nx][ny] = storage[x][y] + 1

flag = False
max_d = 0
for i in range(n):
    for j in range(m):
        if storage[i][j] == 0:
            flag = True
        max_d = max(max_d, storage[i][j])

if flag:
    print(-1)
else:
    print(max_d - 1)
