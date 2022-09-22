import sys
sys.setrecursionlimit(10**9)

nn = int(sys.stdin.readline())

zero_dp = [1, 0, 1]
one_dp = [0, 1, 1]


def fibo(n):
    length = len(zero_dp)
    if n >= length:
        for i in range(length, n + 1):
            zero_dp.append(zero_dp[i - 1] + zero_dp[i - 2])
            one_dp.append(one_dp[i - 1] + one_dp[i - 2])
    print('{} {}'.format(zero_dp[n], one_dp[n]))


for _ in range(nn):
    num = int(sys.stdin.readline())
    fibo(num)

