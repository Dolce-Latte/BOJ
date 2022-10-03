import sys


def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r

    return a


def lcm(a, b):
    return int(a * b / gcd(a, b))


n = int(sys.stdin.readline().strip())
t = list(map(int, sys.stdin.readline().split()))

if n == 3:
    print(t[0])
elif n == 4:
    print(lcm(t[0], t[1]))
else:
    l = lcm(t[0], t[1])
    for i in range(2, len(t)):
        l = lcm(l, t[i])

    print(l)
