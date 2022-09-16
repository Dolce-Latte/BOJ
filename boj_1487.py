import sys

n = int(sys.stdin.readline())

cost = []
for _ in range(n):
    price, delivery = map(int, sys.stdin.readline().split())
    cost.append((price, delivery))

cost.sort()

total = [0] * n
for i in range(n):
    for j in range(i, n):
        profit = cost[i][0] - cost[j][1]
        if profit > 0:
            total[i] += profit

result = [
    cost[i][0] for i in range(n)
    if total[i] == max(total)
]

if sum(total) == 0:
    print(0)
else:
    print(min(result))
