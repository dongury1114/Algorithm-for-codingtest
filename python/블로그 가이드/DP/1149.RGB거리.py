import sys

# sys.stdin = open("input.txt")

n = int(input())

# dp = []
# for i in range(n):
#     dp.append(list(map(int, input().split())))

dp = [list(map(int, input().split()))for _ in range(n)]

for i in range(1, n):
    dp[i][0] += min(dp[i-1][1], dp[i-1][2])
    dp[i][1] += min(dp[i-1][0], dp[i-1][2])
    dp[i][2] += min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))