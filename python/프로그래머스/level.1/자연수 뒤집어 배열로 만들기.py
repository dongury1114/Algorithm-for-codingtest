def solution(n):
    # return list(str(n))[:-1]
    a = list(map(int, str(n)))[::-1]  # sol.1
    a = list(map(int, reversed(str(n))))  # sol.2
    return a
