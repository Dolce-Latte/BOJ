import sys

n = int(sys.stdin.readline())

data = []

for i in range(100000):
    s = str(i)
    if '666' in s:
        data.append(s)

print(data[n-1])

