import math
import sys

s = sys.stdin.readline().strip()

length = len(s)

if s == s[0] * length:
    print(-1)
elif s[:length//2][::-1] == s[math.ceil(length/2):]:
    print(length - 1)
else:
    print(length)

