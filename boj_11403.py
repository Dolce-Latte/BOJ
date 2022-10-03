import sys
INF = sys.maxsize


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adj_matrix[i][k] == 1 and adj_matrix[k][j] == 1:
                    adj_matrix[i][j] = 1


n = int(sys.stdin.readline().strip())

adj_matrix = []
for _ in range(n):
    adj_matrix.append(list(map(int, sys.stdin.readline().split())))

floyd_warshall()

for i in range(n):
    for j in range(n):
        print(adj_matrix[i][j], end=" ")
    print()
