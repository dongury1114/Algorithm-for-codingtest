import sys

sys.stdin = open("input.txt")

ans = []  # 소수 저장

n = int(input())

for i in range(2, n+1):
    count = 0
    for j in range(2, n+1):
        if i % j == 0:
            count += 1
    if count == 1:
        ans.append(i)
print(len(ans))
