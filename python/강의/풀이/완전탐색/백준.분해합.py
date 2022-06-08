import sys

sys.stdin = open("input.txt")

n = int(input())
ans = 0
for i in range(1, n+1):
    a = list(map(int, str(i)))
    s = i + sum(a)
    if s == n:
        ans = i
        break
print(ans)
