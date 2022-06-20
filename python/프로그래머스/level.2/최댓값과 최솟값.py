def solution(s):
    tmp = list(map(int, s.split()))
    MAX, MIN = str(max(tmp)), str(min(tmp))
    return MIN+" "+MAX
