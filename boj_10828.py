import sys

n = int(sys.stdin.readline().strip())

stk = []

for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == "push":
        stk.append(command[-1])
    elif command[0] == "pop":
        if not stk:
            print(-1)
        else:
            print(stk[-1])
            stk.pop()
    elif command[0] == "top":
        if not stk:
            print(-1)
        else:
            print(stk[-1])
    elif command[0] == "size":
        print(len(stk))
    elif command[0] == "empty":
        if not stk:
            print(1)
        else:
            print(0)