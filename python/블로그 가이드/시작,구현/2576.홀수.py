import sys

sys.stdin = open("input.txt")

num = []
for _ in range(7):
    a = int(input())
    if a % 2 == 1:
        num.append(a)
if not num:
    print(-1)
else:
    print(sum(num))
    print(min(num))
