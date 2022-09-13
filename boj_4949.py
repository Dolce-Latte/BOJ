while True:
    s = input()
    isValid = True
    a = []
    if s == ".":
        break
    for elem in s:
        if elem == '(' or elem == '[':
            a.append(elem)
        elif elem == ')':
            if not a or a[-1] == '[':
                isValid = False
                break
            elif a[-1] == '(':
                a.pop()
        elif elem == ']':
            if not a or a[-1] == '(':
                isValid = False
                break
            elif a[-1] == '[':
                a.pop()
    if isValid == True and not a:
        print('yes')
    else:
        print('no')