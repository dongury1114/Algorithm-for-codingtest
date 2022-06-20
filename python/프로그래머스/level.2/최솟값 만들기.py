def solution(A, B):
    A.sort(reverse=True)
    B.sort(reverse=False)
    ans = 0
    for i in range(len(A)):
        ans += A[i] * B[i]
    return ans
