import sys
from collections import deque
read = sys.stdin.readline # 앞으로 이렇게 사용하자


def bfs(_vertex):
    q = deque()
    q.append(_vertex)
    visit_list_bfs[_vertex] = 1
    while q:
        _vertex = q.popleft()
        print(_vertex, end=" ")
        for i in range(1, n + 1):
            if visit_list_bfs[i] == 0 and graph[_vertex][i] == 1:
                q.append(i)
                visit_list_bfs[i] = 1


def dfs(_vertex):
    visit_list_dfs[_vertex] = 1
    print(_vertex, end=" ")
    for i in range(1, n + 1):
        if visit_list_dfs[i] == 0 and graph[_vertex][i] == 1:
            dfs(i)


n, m, v = map(int, read().split())

graph = [[0] * (n + 1) for _ in range(n + 1)]
visit_list_bfs = [0] * (n + 1)
visit_list_dfs = [0] * (n + 1)

for _ in range(m):
    s, e = map(int, read().split())
    graph[s][e] = graph[e][s] = 1

dfs(v)
print()
bfs(v)
