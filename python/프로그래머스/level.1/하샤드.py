def solution(x):
    tmp = list(map(int, str(x)))
    a = sum(tmp)
    return True if x % a == 0 else False
