import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        x = queue.popleft()
        if x == k:
            print(distance[x])
            break
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= MAX and not distance[nx]:
                distance[nx] = distance[x] + 1
                queue.append(nx)


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())

    MAX = 10 ** 5
    distance = [0] * (MAX + 1)
    bfs()
