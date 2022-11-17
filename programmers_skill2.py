import sys


def possible(x, y, n, row):
    for i in range(x):
        if y == row[i] or abs(y - row[i]) == x - i:
            return False
    return True


def queen(x, n, row):
    if x == n:
        return 1
    cnt = 0

    for i in range(n):
        if possible(x, i, n, row):
            row[x] = i
            cnt += queen(x+1, n, row)

    return cnt

def solution(n):
    row = [0] * n
    answer = queen(0, n, row)

    return answer

n = int(sys.stdin.readline())
print(solution(n))

