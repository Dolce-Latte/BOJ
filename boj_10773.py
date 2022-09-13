import sys

k = int(sys.stdin.readline())

stk = []

for _ in range(k):
    n = int(sys.stdin.readline())

    if n == 0:
        if not stk:
            continue
        else:
            stk.pop()
    else:
        stk.append(n)

print(sum(stk))