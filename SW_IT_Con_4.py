import sys
from collections import deque

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))
nums.sort(reverse=True)
void = [0] * n
visited = [0] * n
for i in range(n - 1):
    for j in range(i + 1, n):
        if nums[i] > nums[j] and void[i] == 0 and visited[j] == 0:
            void[i] = 1
            visited[j] = -1

cnt = 0
for elem in void:
    if elem == 0:
        cnt += 1

print(cnt)




