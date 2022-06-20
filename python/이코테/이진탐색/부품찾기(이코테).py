import sys

sys.stdin = open("input.txt")

n = int(input())
things = list(map(int, input().split()))
things.sort()

m = int(input())
find_things = list(map(int, input().split()))

# sol.1
# def binary_search(arr, start, end, target):
#     while start <= end:
#         mid = (start+end)//2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             start = mid + 1
#         else:
#             end = mid-1

#     return False


# for i in find_things:
#     if binary_search(things, 0, n-1, i):
#         print("yes", end=" ")
#     else:
#         print("no", end=" ")

for i in find_things:
    if i in things:
        print("yes", end=" ")
    else:
        print("no", end=" ")
