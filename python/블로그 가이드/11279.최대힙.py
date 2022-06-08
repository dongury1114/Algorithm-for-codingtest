from heapq import heappop, heappush

import sys

sys.stdin = open("input.txt")

N = int(input())

heap = []

for i in range(N):
    m = int(input())*-1
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heappop(heap)*-1)
    else:
        heappush(heap, m)
