import sys


def in_range(x, y, h):
    return x <= r < x + h and y <= c < y + h


def zigzag(x, y, h):
    global cnt

    if x == r and y == c:
        print(cnt)
        exit(0)

    if h == 1:
        cnt += 1
        return

    if not in_range(x, y, h):
        cnt += h**2
        return

    h = h // 2
    zigzag(x, y, h)
    zigzag(x, y + h, h)
    zigzag(x + h, y, h)
    zigzag(x + h, y + h, h)


N, r, c = map(int, sys.stdin.readline().split())
r = r
c = c
cnt = 0
board = [[0] * N for _ in range(N)]

zigzag(0, 0, 2 ** N)