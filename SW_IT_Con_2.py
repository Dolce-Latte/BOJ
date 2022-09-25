import sys

n = int(sys.stdin.readline())

string = sys.stdin.readline().strip()

cnt = 0
for i in range(len(string) // 2):
    if string[i] != string[-i - 1]:
        cnt += 1

print(cnt)