import sys
from collections import deque


def bfs(r):
    global cnt
    queue = deque([r])
    visited[r] = 1

    while queue:
        v = queue.popleft()
        graph[v].sort()

        for elem in graph[v]:
            if visited[elem] == 0:
                cnt += 1
                visited[elem] = cnt
                queue.append(elem)


n, m, r = map(int, sys.stdin.readline().split())

visited = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
cnt = 1

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph[s].append(e)
    graph[e].append(s)

bfs(r)

for v in visited[1:]:
    print(v)