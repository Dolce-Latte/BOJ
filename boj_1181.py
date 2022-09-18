import sys

n = int(sys.stdin.readline())

words = []
for _ in range(n):
    word = sys.stdin.readline().strip()
    words.append(word)

words = list(set(words))
words.sort()
words.sort(key=len)

for elem in words:
    print(elem)
