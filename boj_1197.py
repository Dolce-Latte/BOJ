import sys


def find(x):
    if x != vertex_list[x]:
        vertex_list[x] = find(vertex_list[x])
    return vertex_list[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        vertex_list[x] = y
    else:
        vertex_list[y] = x

v, e = map(int, sys.stdin.readline().split())

vertex_list = [i for i in range(v + 1)]
edge_list = []
for _ in range(e):
    edge_list.append(list(map(int, sys.stdin.readline().split())))

edge_list.sort(key=lambda x: x[2])

answer = 0
for start, end, weight in edge_list:
    start_Root = find(start)
    end_Root = find(end)
    if start_Root != end_Root:
        union(start_Root, end_Root)
        answer += weight

print(answer)