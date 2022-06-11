import sys

sys.stdin = open("input.txt")

n = int(input())
nums = [list(map(int, input().split())) for _ in range(n)]
M = 0
for i in range(n):  # 가로 합
    sum1 = 0
    sum2 = 0
    for j in range(n):
        sum1 += nums[i][j]
        sum2 += nums[j][i]
    M = max(sum1, sum2, M)

for i in range(n):
    sum1 = 0
    sum2 = 0
    sum1 += nums[i][i]
    sum2 += nums[i][n-i-1]
    M = max(sum1, sum2, M)

print(M)
