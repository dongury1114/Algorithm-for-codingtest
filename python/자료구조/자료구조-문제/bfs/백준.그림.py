from collections import deque
import sys

sys.stdin = open("input.txt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)


n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

scale = []

visited = [[0 for _ in range(m)] for _ in range(n)]


def bfs(i, j):
    global count
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    que = deque()
    que.append([i, j])
    visited[i][j] = True

    while que:
        x, y = que.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == True and visited[nx][ny] == False:
                    que.append([nx, ny])
                    visited[nx][ny] = True
                    count += 1
    scale.append(count)


for i in range(n):
    for j in range(m):
        if(arr[i][j] == True and visited[i][j] == False):
            count = 1
            bfs(i, j)
if(len(scale) == 0):
    print(len(scale))
    print(0)
else:
    print(len(scale))
    print(max(scale))
# 출처: https: // jainn.tistory.com/173 [Dogfootruler Kim:티스토리]
