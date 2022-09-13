import sys
from collections import deque

n = int(sys.stdin.readline())

words = deque()

word = sys.stdin.readline().strip()
words.append(word)
for _ in range(1, n):
    word = sys.stdin.readline().strip()

    if len(word) > len(words[0])


