import sys

sys.stdin = open("input.txt")


def DFS(x):
    if x == 0:
        return  # 함수의 종료 의미
    else:
        DFS(x//2)
        print(x % 2, end="")


n = int(input())
DFS(n)
