import sys

T = int(sys.stdin.readline())

for _ in range(T):
    ps = sys.stdin.readline().strip()

    stk = []
    flag = 0
    for i in range(len(ps)):
        if ps[i] == '(':
            stk.append(ps[i])
        else:
            if len(stk) == 0:
                flag = 1
            elif stk[-1] == '(':
                stk.pop()
    if stk or flag:
        print("NO")
    else:
        print("YES")