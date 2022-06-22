def solution(s):
    s = list(s)
    stack = []
    count = 0
    for i in s:
        if i == "(":
            stack.append(i)
            count += 1
        elif i == ")":
            stack.append(i)
            count -= 1

        if count < 0:
            print(False)
            break

    if count < 0 or count > 0:
        return False
    else:
        return True
