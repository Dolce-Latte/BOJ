import sys
from collections import deque


def bfs(_graph, _start):
    num = [0] * (n + 1)
    visited = [_start]
    queue = deque()
    queue.append(_start)

    while queue:
        _x = queue.popleft()
        for elem in _graph[_x]:
            if elem not in visited:
                num[elem] = num[_x] + 1
                visited.append(elem)
                queue.append(elem)

    return sum(num)


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().split())

    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        _a, _b = map(int, sys.stdin.readline().split())
        graph[_a].append(_b)
        graph[_b].append(_a)

    result = []
    for i in range(1, n + 1):
        result.append(bfs(graph, i))

    print(result.index(min(result)) + 1)
