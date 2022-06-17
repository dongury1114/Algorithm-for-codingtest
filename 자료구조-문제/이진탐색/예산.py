import sys

sys.stdin = open("input.txt")

n = int(input())
city = list(map(int, input().split()))
m = int(input())
tmp = sum(city) - m
start = 0


end = max(city)
while start <= end:
    mid = (start + end) // 2
    sum = 0

    for i in city:
        if i > mid:
            sum += i - mid

    if sum >= tmp:
        start = mid + 1
    else:
        end = mid - 1
print(end)
