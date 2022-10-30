import sys


def find_str(_n, _m, _s):
    answer = 0
    count = 0
    idx = 0

    while idx < (_m - 1):
        if _s[idx:idx + 3] == 'IOI':
            idx += 2
            count += 1
            if count == _n:
                answer += 1
                count -= 1
        else:
            idx += 1
            count = 0

    return answer


def main():
    n = int(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()

    print(find_str(n, m, s))


if __name__ == '__main__':
    main()