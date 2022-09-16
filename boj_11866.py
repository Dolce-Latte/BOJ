import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
queue = deque()
ans = []

for i in range(1, n + 1):
    queue.append(i)

while queue:
    for i in range(k - 1):
        queue.append(queue.popleft())
    ans.append(queue.popleft())

print("<", end='')
for i in range(len(ans)-1):
    print("%d, " %ans[i], end='')
print(ans[-1], end='')
print(">")
