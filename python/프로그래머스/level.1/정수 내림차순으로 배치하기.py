def solution(n):
    tmp = list(map(int, str(n)))
    tmp.sort(reverse=True)
    ans = "".join(map(str, tmp))
    return int(ans)


def solution(n):
    tmp = list(str(n))
    tmp.sort(reverse=True)
    ans = "".join(tmp)
    return int(ans)
