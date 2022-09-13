import sys

n = int(sys.stdin.readline())

sum = 0
res = 0
for i in range(n):
    s = str(i)
    for elem in s:
        sum += int(elem)
    sum += i

    if sum == n:
        res = i
        break
    else:
        sum = 0
        continue

print(res)
