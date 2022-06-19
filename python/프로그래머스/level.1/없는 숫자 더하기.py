def solution(numbers):
    tmp = list(range(1, 10))
    ans = 0
    for i in tmp:
        if i not in numbers:
            ans += i
    return ans
