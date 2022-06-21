from heapq import *

scoville, K = [1, 2, 3, 9, 10, 12], 7


def solution(scoville, K):
    heap = []
    for num in scoville:
        heappush(heap, num)

    count = 0
    while heap[0] < k:
        try:
            heappush(heap, heappop(heap) + heappop(heap) * 2)
            count += 1
        except IndexError:
            print(-1)
    print(count)


def solution(scoville, K):
    from heapq import heappop, heappush, heapify

    count = 0
    heapify(scoville)
    while len(scoville) > 1 and scoville[0] < K:
        num1 = heappop(scoville)
        num2 = heappop(scoville)
        heappush(scoville, num1 + num2 * 2)
        count += 1
    if scoville[0] >= K:
        return count
    else:
        return -1
