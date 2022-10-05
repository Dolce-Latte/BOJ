import sys
# 누적 합 구하기
n, m = map(int, sys.stdin.readline().split())

nums = list(map(int, sys.stdin.readline().split()))

acc_sum = [0]

sum_num = 0
for num in nums:
    sum_num += num
    acc_sum.append(sum_num)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(acc_sum[j] - acc_sum[i - 1])