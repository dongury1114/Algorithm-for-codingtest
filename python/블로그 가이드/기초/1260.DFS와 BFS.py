from re import L
import sys

sys.stdin = open("input.txt")

input = sys.stdin.readline
# 첫째 줄에 정점의 개수 N 간선의 개수 M, 탐색을 시작할 정점의 번호 V가 주어진다
N, M, V = map(int, input().split())

# graph = [[]*(N+1)]
visited = [False] * (N + 1)
graph = []
for _ in range(N+1):
    graph.append([])

print(graph)
for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N + 1):
    graph[i].sort()
