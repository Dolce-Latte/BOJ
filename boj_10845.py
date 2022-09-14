import sys

N = int(sys.stdin.readline())

queue = []

for _ in range(N):
    command = sys.stdin.readline().split()

    order = command[0]

    if order == "push":
        queue.append(command[-1])
    elif order == "pop":
        if queue:
            print(queue.pop(0))
        else:
            print(-1)
    elif order == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif order == "back":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif order == "size":
        print(len(queue))
    elif order == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)

