def solution(s):
    tmp = []
    count_p = 0
    count_y = 0
    for i in s:
        tmp.append(i.upper())

    for i in tmp:
        if i == "P":
            count_p += 1
        elif i == "Y":
            count_y += 1

    if count_p == count_y:
        return True
    elif count_p != count_y:
        return False
