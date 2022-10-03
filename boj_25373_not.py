import math
import sys

n = int(sys.stdin.readline())

if n <= 1:
    x = 1
elif n <= 3:
    x = 2
elif n <= 6:
    x = 3
elif n <= 10:
    x = 4
elif n <= 15:
    x = 5
elif n <= 21:
    x = 6
elif n <= 28:
    x = 7
else:
    x = ((n - 28) // 7) + 8
print(x)
