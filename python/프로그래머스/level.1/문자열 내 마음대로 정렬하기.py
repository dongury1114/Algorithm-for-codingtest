def solution(strings, n):
    strings.sort()
    ans = sorted(strings, key=lambda x: (x[n]))
    return ans

# c = sorted(a, key = lambda x : x[0])
