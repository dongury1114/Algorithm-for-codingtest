def solution(nums):
    n = len(nums) // 2
    m = len(set(nums))
    return min(n, m)
