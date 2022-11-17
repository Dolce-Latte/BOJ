import sys

while True:
    try:
        n, k = map(int, sys.stdin.readline().split())
        stamp = n

        while True:
            if stamp // k == 0:
                break
            n += stamp // k
            stamp = stamp // k + stamp % k

        print(n)

    except :
        break
