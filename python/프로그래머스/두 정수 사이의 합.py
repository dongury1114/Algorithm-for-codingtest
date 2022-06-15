def solution(a, b):
    if a == b:
        return a
    elif a < b:
        tmp = list(range(a, b+1))
        return sum(tmp)
    elif a > b:
        tmp = list(range(b, a+1))
        return sum(tmp)


def solution(a, b):

    if a > b:
        a, b = b, a
    return sum(range(a, b+1))
