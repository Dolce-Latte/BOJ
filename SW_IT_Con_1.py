import sys

n, m = map(int, sys.stdin.readline().split())

n = n // 2

if n <= m:
    print(n)
else:
    print(m)