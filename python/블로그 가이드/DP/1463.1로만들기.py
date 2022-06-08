import sys

# sys.stdin = open("input.txt")

n = int(input())

d = [0] * (1000001)

d[1] = 0
d[2] = 1
for i in range(3, n+1):
    d[i] = d[i-1] + 1
    
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] +1)
    
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] +1)
print(d[n])




# n = int(input())
# dp = [0 for i in range(n+2)]

# dp[1] = 0
# dp[2] = 1

# for i in range(3,n+1):
#     dp[i] = dp[i-1] + 1
#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2] + 1)
#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3] + 1)
# print(dp[n])