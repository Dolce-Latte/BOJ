import math
import sys
from collections import deque
import copy


def is_prime(x, y):
    primes = deque()
    for i in range(x, y + 1):
        check = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                check = False
        if check:
            primes.append(i)

    return primes


a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())

yt = is_prime(a, b)
yj = is_prime(c, d)
cnt = 0
for elem in copy.deepcopy(yt):
    if elem in yj:
        yt.remove(elem)
        yj.remove(elem)
        cnt += 1

if cnt % 2 == 0:
    if len(yt) > len(yj):
        print('yt')
    else:
        print('yj')
else:
    if len(yt) < len(yj):
        print('yj')
    else:
        print('yt')


