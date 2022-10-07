import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)


N = int(sys.stdin.readline())

for _ in range(N):
    data = list(map(int, sys.stdin.readline().split()))

    max_value = -1
    data.sort()

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            max_value = max(max_value, gcd(data[i], data[j]))
    print(max_value)