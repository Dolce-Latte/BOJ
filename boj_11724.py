import sys
sys.setrecursionlimit(10**6)


def dfs(_v):
    visited[_v] = True
    for _e in graph[_v]:
        if not visited[_e]:
            dfs(_e)


n, m = map(int, sys.stdin.readline().split())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n + 1):
    if not visited[i]:
        dfs(i)
        cnt += 1

print(cnt)
