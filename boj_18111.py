import sys
from math import inf
n, m, b = map(int, sys.stdin.readline().split())

land = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
ans_time = inf
height = 0

for h in range(0, 257):
    minimum = 0
    maximum = 0
    for i in range(n):
        for j in range(m):
            # temp = land[i][j] - h
            if land[i][j] < h:
                minimum += (h - land[i][j])
            else:
                maximum += (land[i][j] - h)

    # 기존 인벤토리 블록 개수 + 넣는 블록 개수 >= 빼내는 블록 개수
    inventory = maximum + b
    if inventory < minimum:
        continue

    time = 2 * maximum + minimum
    if time <= ans_time: # If there are multiple answers, the highest one is printed
        ans_time = time
        height = h

print(ans_time, height)

