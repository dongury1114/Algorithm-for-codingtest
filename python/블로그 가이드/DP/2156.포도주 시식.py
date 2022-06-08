import sys

sys.stdin = open("input.txt")

input  = sys.stdin.readline

n = int(input())
dp = [0] * (n+2)
array = [0] * (n+2)

for i in range(n):
    array[i] = (int(input())) # 인덱스 에러 잡는방법 !

dp[0]=array[0]
dp[1]=array[0]+array[1]
dp[2]=max(array[2]+array[0], array[2]+array[1], dp[1])

for i in range(3, n):
    dp[i] = max(dp[i-1], dp[i-2]+array[i], dp[i-3] + array[i-1] + array[i])

print(max(dp))
