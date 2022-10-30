import sys
n, x = map(int, sys.stdin.readline().split())

t = list(map(int, sys.stdin.readline().split()))

idx = 0
while True:
    idx %= n
    if x > t[idx]:
        print(idx + 1)
        break
    else:
        x += 1
        idx += 1


