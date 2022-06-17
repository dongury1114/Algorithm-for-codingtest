from operator import le
import sys

sys.stdin = open("input.txt")
n, m = map(int, input())
lesson = list(map(int, input().split()))

start = max(lesson)
end = sum(lesson)

while start <= end:
    mid = (start + end) // 2
    tmp = 0
    count = 0
    for i in lesson:
        if tmp + lesson > mid:
            count += 1
            tmp = 0
        tmp += i

    if tmp:
        count += 1
    else:
        0
