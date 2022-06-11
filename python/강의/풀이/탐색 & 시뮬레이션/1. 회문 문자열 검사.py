import sys

sys.stdin = open("input.txt")

n = int(input())

for _ in range(n):
    tmp = []
    m = list(input().upper())

    if m == m[::-1]:
        print("YES")
    else:
        print("NO")
