import sys

sys.stdin = open("input.txt")

# 사용한다 안한다 -> 상태 트리


# def DFS(v):
#     if v == n+1:
#         for i in range(1, n+1):
#             if ch[i] == 1:
#                 print(i, end=' ')
#         print()
#     else:
#         ch[v] = 1
#         DFS(v+1)
#         ch[v] = 0
#         DFS(v+1)


# n = int(input())
# ch = [0] * (n+1)  # 체크변수 (사용했나 안했나)
# DFS(1)


def dfs(v):
    if v == n+1:
        for i in range(1, n+1):
            if ch[i] == 1:
                print(i, end=" ")
        print()
    else:
        ch[v] = 1
        dfs(v+1)
        ch[v] = 0
        dfs(v+1)


n = int(input())
ch = [0] * (n + 1)
dfs(1)
