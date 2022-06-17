# https://data-flower.tistory.com/99
import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

while start <= end:
    sum = 0
    mid = (start + end)//2
    for i in trees:
        if i > mid:
            sum += i-mid

    if sum >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)

# while start <= end:
#     sum = 0
#     mid = (start + end) // 2
#     for i in trees:
#         if i > mid:
#             sum += i - mid
#     if sum >= m:
#         start = mid + 1
#     elif sum < m:
#         end = mid - 1
# print(end)
