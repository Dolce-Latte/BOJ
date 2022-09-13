s = input()

stk = []
temp = 1
ans = 0

for i in range(len(s)):
    elem = s[i]
    if elem == '(':
        stk.append(elem)
        temp *= 2
    elif elem == '[':
        stk.append(elem)
        temp *= 3
    elif elem == ')':
        if not stk or stk[-1] == '[':
            ans = 0
            break
        if s[i - 1] == '(':
            ans += temp
        temp //= 2
        stk.pop()
    else:
        if not stk or stk[-1] == '(':
            ans = 0
            break
        if s[i - 1] == '[':
            ans += temp
        temp //= 3
        stk.pop()

if stk:
    print(0)
else:
    print(ans)