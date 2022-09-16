import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = list(map(int, sys.stdin.readline().split()))
    queue = list(map(int, sys.stdin.readline().split()))
    idx = list(range(len(queue)))
    idx[m] = 't'

    order = 0

    while True:
        if queue[0] == max(queue):
            order += 1
            if idx[0] == 't':
                print(order)
                break
            else:
                queue.pop(0)
                idx.pop(0)
        else:
            queue.append(queue.pop(0))
            idx.append(idx.pop(0))

