def solution(arr, divisor):
    ans = []

    for i in arr:
        if i % divisor == 0:
            ans.append(i)
    return [-1] if len(ans) == 0 else sorted(ans)
