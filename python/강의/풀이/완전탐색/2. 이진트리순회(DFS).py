import sys

sys.stdin = open("input.txt")


def DFS(v):
    if v > 7:
        return
    else:
        DFS(v*2)
        DFS(v*2+1)
        print(v, end=" ")


DFS(1)

# 전위: print(v)가 제일 먼저
# 중위: print(v)가 가운데
# 흐위: print(v)가 마지막
