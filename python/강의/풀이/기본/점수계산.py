import sys
sys.stdin = open("input.txt")

n = int(input())
num = list(map(int, input().split()))

tmp = []
count = 0
sum = 0
for i in range(n):
    if num[i] == 1:
        count += 1
        sum = sum + count
    else:
        count = 0

print(sum)
