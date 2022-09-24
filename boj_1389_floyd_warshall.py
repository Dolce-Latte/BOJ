import sys
from collections import deque
INF = sys.maxsize


def floyd_warshall():
    for k in range(1, n + 1):
        graph[k][k] = 0
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    graph = [[INF] * (n + 1) for _ in range(n + 1)]

    for i in range(m):
        _a, _b = map(int, sys.stdin.readline().split())
        graph[_a][_b] = 1
        graph[_b][_a] = 1

    floyd_warshall()

    sum = [0] * (n + 1)
    ans = INF
    result = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            sum[i] += graph[i][j]
        if ans > sum[i]:
            ans = sum[i]
            result = i

    print(result)