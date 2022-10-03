import math
import sys


def distance(_x1, _y1, _x2, _y2):
    d = math.sqrt((_x1 - _x2) ** 2 + (_y1 - _y2) ** 2)

    return d


t = int(sys.stdin.readline().strip())

for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    dis = distance(x1, y1, x2, y2)

    if dis == 0 and r1 == r2:
        print(-1)
    elif dis == abs(r1 - r2) or dis == r1 + r2:
        print(1)
    elif abs(r1 - r2) < dis < r1 + r2:
        print(2)
    else:
        print(0)
