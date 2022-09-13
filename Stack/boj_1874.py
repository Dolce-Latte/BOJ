from collections import deque
import sys

n = int(sys.stdin.readline())
seq = deque()
stk = deque()
for _ in range(n):
    num = int(sys.stdin.readline())

    seq.append(num)

for elem in seq:
    