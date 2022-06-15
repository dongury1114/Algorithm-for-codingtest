def solution(s):
    n = len(s)
    if n % 2 == 1:
        return s[int(n/2)]
    else:
        return s[int(n//2)-1:int(n//2)+1]


def solution(s):
    return str[(len(str)-1)//2:len(str)//2+1]
