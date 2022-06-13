import sys
from heapq import heappop, heappush


sys.stdin = open("input.txt")

input = sys.stdin.readline

heap = []

N = int(input())

for i in range(N):
    x = int(input())
    if x != 0:
        heappush(heap, (abs(x), x))
    else:
        if not heap:
            print(0)
        else:
            print(heappop(heap)[1])
