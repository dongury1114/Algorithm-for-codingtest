import sys

sys.stdin = open("input.txt")

n = int(input())
m = list(map(int, input().split()))
ans = 0
m.sort(reverse=False)

if n == 1:
    ans = pow(m[0], 2)
else:
    ans = min(m) * max(m)
print(ans)
