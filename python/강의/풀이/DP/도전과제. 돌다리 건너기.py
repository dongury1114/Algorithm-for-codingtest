import sys

sys.stdin = open("input.txt")

# 출력: 34

n = int(input())
dp = [0] * (n+2)

dp[1] = 1
dp[2] = 2

for i in range(3, n+2):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[n+1])
