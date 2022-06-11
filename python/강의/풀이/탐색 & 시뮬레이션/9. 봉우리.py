import sys

sys.stdin = open("input.txt")

# 출력 11
n = int(input())
tmp = list(list(map(int, input().split()))for _ in range(n))
visited = [([0] * (n+2)) for _ in range(n+2)]
# dx = [1, -1, 0, 0]
# dy = [0, 0, 1, -1]

# 일단 시간 복잡도를 생각하지 말고 한번 풀어보자

for i in range(1, n+1):
    for j in range(1, n+1):
        visited[i][j] = tmp[i-1][j-1]
# 모든 좌표들을 순회하면서 상하좌우 비교
count = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if visited[i][j] > max(visited[i-1][j], visited[i+1][j], visited[i][j+1], visited[i][j-1]):
            count += 1
print(count)
