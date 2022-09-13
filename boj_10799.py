s = input()

stk = []
answer = 0

for i in range(len(s)):
    if s[i] == '(':
        stk.append(s[i])
    else:
        if s[i-1] == '(':
            stk.pop()
            answer += len(stk)
        else:
            stk.pop()
            answer += 1

print(answer)
