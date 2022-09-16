import sys
from itertools import combinations
n = int(sys.stdin.readline())

decrease = []

for i in range(1, 11):
    for elem in combinations(range(0, 10), i):
        elem = list(elem)
        elem.sort(reverse=True)
        decrease.append(int("".join(map(str, elem))))

decrease.sort()

try:
    print(decrease[n])
except:
    print(-1)