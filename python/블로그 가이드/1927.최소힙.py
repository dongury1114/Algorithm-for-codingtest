import sys
import heapq

input = sys.stdin.readlines

sys.stdin = open("input.txt")

heap = []

n = int(input())

for i in range(n):
    m = int(input())
    if m == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, m)
