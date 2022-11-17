import sys

n, m = map(int, sys.stdin.readline().split())
times = []

for _ in range(n):
    times.append(int(sys.stdin.readline()))

left = 0
answer = right = max(times) * m

