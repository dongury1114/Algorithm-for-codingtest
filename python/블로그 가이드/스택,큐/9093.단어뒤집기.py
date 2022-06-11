import sys

sys.stdin = open("input.txt")

n = int(input())

for _ in range(n):
    m = list(input().split())
    ans = []
    for i in m:
        ans.append(i[::-1])
    print(*ans)

-------------------------------------

n = int(input())

for i in range(n):
    word = []
    word = list(input().split())
    for i in range(len(word)):
        word[i] = word[i][::-1]
    print(" ".join(word))
