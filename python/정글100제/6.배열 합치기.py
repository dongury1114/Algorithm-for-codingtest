import sys

sys.stdin = open("input.txt")

n = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

ans = a+b
ans.sort()
ans = list(map(str, ans))
print(" ".join(ans))
