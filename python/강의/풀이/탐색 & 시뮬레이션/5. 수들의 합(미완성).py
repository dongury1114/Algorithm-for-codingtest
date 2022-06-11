import sys

sys.stdin = open("input.txt")

n, m = list(map(int, input().split()))
tmp = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i, n+1):
        if tmp[i] + tmp[j] == m:
            count += 1
print(count)
