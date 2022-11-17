import sys
INF = float('inf')


def bellman_ford(start):
    dist[start] = 0

    for i in range(1, n + 1):
        for j in range(m):
            now, nxt, cost = edge[j][0], edge[j][1], edge[j][2]
            if dist[now] != INF and dist[nxt] > dist[now] + cost:
                dist[nxt] = dist[now] + cost
                if i == n:
                    return True
    return False


n, m = map(int, sys.stdin.readline().split())
edge = []
dist = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edge.append((a,b,c))

negative = bellman_ford(1)

if negative:
    print(-1)
else:
    for i in range(2, n + 1):
        if dist[i] == INF:
            print(-1)
        else:
            print(dist[i])