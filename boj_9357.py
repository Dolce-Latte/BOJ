import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    h = {}
    for i in range(n):
        clothes, kind = sys.stdin.readline().strip().split()
        if kind not in h:
            h[kind] = 1
        else:
            h[kind] += 1

    total = 1

    for elem in h:
        total *= (h[elem] + 1)
    print(total - 1)
