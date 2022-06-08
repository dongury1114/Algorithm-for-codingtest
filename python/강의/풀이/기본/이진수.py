import sys

sys.stdin = open("input.txt")


def DFS(x):
    if x == 0:
        return 0
    else:
        print(x % 2, end=" ")
        DFS(x//2)


n = int(input())
DFS(n)
