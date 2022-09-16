import sys

n = int(sys.stdin.readline())
N = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().split()))

hashmap = {}
for elem in N:
    if elem in hashmap:
        hashmap[elem] += 1
    else:
        hashmap[elem] = 1

for elem in M:
    if elem in hashmap:
        print(hashmap[elem], end=' ')
    else:
        print(0, end=' ')
