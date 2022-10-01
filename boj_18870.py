import sys

n = int(sys.stdin.readline())

l = list(map(int, sys.stdin.readline().split()))
s = set(l)
ll = sorted(list(s))
dict = {ll[i]: i for i in range(len(ll))}

for i in l:
    print(dict[i], end=" ")


