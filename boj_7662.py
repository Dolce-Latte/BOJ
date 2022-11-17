import sys
import heapq

t = int(sys.stdin.readline().strip())

for _ in range(t):
    k = int(sys.stdin.readline().strip())
    minQ, maxQ = [], []
    visited = [False] * k
    for idx in range(k):
        op, n = sys.stdin.readline().split()
        n = int(n)

        if op == 'I':
            heapq.heappush(minQ, (n, idx))
            heapq.heappush(maxQ, (-n, idx))
            visited[idx] = True

        else:
            if n == 1:
                while maxQ and not visited[maxQ[0][1]]:
                    heapq.heappop(maxQ)
                if maxQ:
                    visited[maxQ[0][1]] = False
                    heapq.heappop(maxQ)
            else:
                while minQ and not visited[minQ[0][1]]:
                    heapq.heappop(minQ)
                if minQ:
                    visited[minQ[0][1]] = False
                    heapq.heappop(minQ)

    while minQ and not visited[minQ[0][1]]:
        heapq.heappop(minQ)
    while maxQ and not visited[maxQ[0][1]]:
        heapq.heappop(maxQ)

    if not minQ or not maxQ:
        print('EMPTY')
    else:
        num1 = -maxQ[0][0]
        num2 = minQ[0][0]
        print("%d %d" %(num1, num2))
