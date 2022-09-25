import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

odd = 0
even = 0

for elem in nums:
    if elem % 2 == 0:
        even += 1
    else:
        odd += 1

if n % 2 != 0:
    if even < odd and even + odd == n:
        print(1)
    else:
        print(0)
else:
    if even == odd and even + odd == n:
        print(1)
    else:
        print(0)

