from itertools import combinations


def solution(numbers):
    ans = []
    for i in list(combinations(numbers, 2)):
        ans.append(sum(i))
    ans = list(set(ans))
    return sorted(ans)
