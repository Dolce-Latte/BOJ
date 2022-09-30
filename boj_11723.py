import sys

n = int(sys.stdin.readline())

S = 0
for _ in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'add':
        num = int(command[-1]) - 1
        S |= (1 << num)
    elif command[0] == 'remove':
        num = int(command[-1]) - 1
        S &= ~(1 << num)
    elif command[0] == 'check':
        num = int(command[-1]) - 1
        if S & (1 << num) == 0:
            print(0)
        else:
            print(1)
    elif command[0] == 'toggle':
        num = int(command[-1]) - 1
        S ^= (1 << num)
    elif command[0] == 'all':
        S = (1 << 20) - 1
    else:
        S = 0

