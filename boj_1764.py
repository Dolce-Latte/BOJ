import sys

n, m = map(int, sys.stdin.readline().split())

neither_heard_nor_seen = {}
for _ in range(n+m):
    name = sys.stdin.readline().strip()
    if name in neither_heard_nor_seen:
        neither_heard_nor_seen[name] += 1
    else:
        neither_heard_nor_seen[name] = 1

result = []
for elem in neither_heard_nor_seen:
    if neither_heard_nor_seen[elem] == 2:
        result.append(elem)

result.sort()
print(len(result))
for name in result:
    print(name)
