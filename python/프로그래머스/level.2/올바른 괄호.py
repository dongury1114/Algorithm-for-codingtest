def solution(s):
    s = list(s)
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
        if count < 0:
            break

    if count < 0 or count > 0:
        return False
    else:
        return True
