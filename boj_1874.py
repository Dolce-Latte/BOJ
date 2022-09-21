import sys

n = int(sys.stdin.readline())

stk = []
ans = []

flag = False
curr_num = 1
for i in range(n):
    nums = int(sys.stdin.readline())
    while curr_num <= nums:
        stk.append(curr_num)
        ans.append('+')
        curr_num += 1

    if stk[-1] == nums:
        stk.pop()
        ans.append('-')
    else:
        print('NO')
        flag = True
        break

if not flag:
    for elem in ans:
        print(elem)

    