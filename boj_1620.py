import sys

n, m = map(int, sys.stdin.readline().split())

dictionary = {}
for i in range(1, n + 1):
    poket_mon = sys.stdin.readline().strip()
    dictionary[poket_mon] = i
    dictionary[i] = poket_mon

for _ in range(m):
    quiz = sys.stdin.readline().strip()
    if quiz.isdigit():
        print(dictionary[int(quiz)])
    else:
        print(dictionary[quiz])
