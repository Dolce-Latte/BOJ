import sys
import heapq as hq

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())

    if x !=0 :
        if x > 0:
            hq.heappush(heap, (x, x))
        else:
            hq.heappush(heap, (-x, x))
    else:
        if len(heap) >= 1:
            print(hq.heappop(heap)[1])
        else:
            print(0)

