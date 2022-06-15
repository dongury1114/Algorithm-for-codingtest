def solution(n):
    tmp = []
    for i in range(n):
        if i % 2 == 0:
            tmp.append("수")
        else:
            tmp.append("박")
    return "".join(tmp)


def solution(n):
    s = "수박"*(n)
    return s[:n]
