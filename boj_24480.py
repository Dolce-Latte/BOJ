import sys
sys.setrecursionlimit(10**9)
read = sys.stdin.readline


def dfs(_vertex):
    global cnt
    visited_list_dfs[_vertex] = cnt
    graph[_vertex].sort()
    for elem in graph[_vertex][::-1]:
        if visited_list_dfs[elem] == 0:
            cnt += 1
            dfs(elem)


n, m, r = map(int, read().split())

visited_list_dfs = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
cnt = 1

for _ in range(m):
    s, e = map(int, read().split())
    graph[s].append(e)
    graph[e].append(s)

dfs(r)

for i in range(1, n + 1):
    print(visited_list_dfs[i])
