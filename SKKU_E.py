import sys

def sumDivisor(n):
    sum = 0
    for i in range(n):
        if n % (i+1) == 0:
            sum += (-1)**(i + 1)
    return sum


s, t = map(int, sys.stdin.readline().split())
sum = 0
for i in range(s,t+1):
    sum += sumDivisor(i)

print(sum)