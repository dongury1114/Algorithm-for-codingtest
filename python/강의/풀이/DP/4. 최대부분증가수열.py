import sys

# sys.stdin = open("input.txt")

# 출력: 7
# n = int(input())
n = 11
# nums = list(map(int, input().split()))
nums = [5, 2, 18, 3, 4, 7, 10, 9, 11, 8, 15]
dp = [1] * (n)
for i in range(n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

# https: // seohyun0120.tistory.com/entry/%EA % B0 % 80 % EC % 9E % A5-%EA % B8 % B4-%EC % A6 % 9D % EA % B0 % 80 % ED % 95 % 98 % EB % 8A % 94-%EB % B6 % 80 % EB % B6 % 84-%EC % 88 % 98 % EC % 97 % B4LIS-%EC % 99 % 84 % EC % A0 % 84-%EC % A0 % 95 % EB % B3 % B5-%EB % B0 % B1 % EC % A4 % 80-%ED % 8C % 8C % EC % 9D % B4 % EC % 8D % AC
