import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())

num = [list(map(int, input().split()))for _ in range(n)]
#dp[i][j] -> 1,1 부터 i,j 까지의 부분합

dp = [[0] * (m+1) for _ in range(n+1)]

# print(num[0][0])
for i in range (1, n+1): # 범위 설정 제대로 하지많으면, 값이 꼬여서 나옴
    for j in range (1, m+1):
        dp[i][j] = dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]+num[i-1][j-1]
print(dp)
# print(dp)
# k = int(input())
# for _ in range(k):
#     i, j, x, y = map(int, input().split())
#     print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])



