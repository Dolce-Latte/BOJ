import sys

n, m = map(int, sys.stdin.readline().split())

board = list()
for _ in range(n):
    board.append(list(sys.stdin.readline().strip()))

choice = list()
for i in range(n - 7):
    for j in range(m - 7):
        white = 0
        black = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        white += 1
                    if board[k][l] != 'B':
                        black += 1
                else:
                    if board[k][l] != 'B':
                        white += 1
                    if board[k][l] != 'W':
                        black += 1
        choice.append(white)
        choice.append(black)

print(min(choice))
