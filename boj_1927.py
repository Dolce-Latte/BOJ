import sys
import heapq as hq

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    heap = []

    for _ in range(n):
        x = int(sys.stdin.readline())

        if x != 0:
            hq.heappush(heap, x)
        else:
            if len(heap) >= 1:
                print(hq.heappop(heap))
            else:
                print(0)
