import sys
sys.setrecursionlimit(10 ** 6)


def dfs(_start):
    global cnt
    visited[_start] = 1

    for i in graph_computer[_start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph_computer = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
    s, e = map(int, sys.stdin.readline().split())
    graph_computer[s].append(e)
    graph_computer[e].append(s)

dfs(1)
print(cnt)
