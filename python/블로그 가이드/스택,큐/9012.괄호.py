import sys

sys.stdin = open("input.txt")

n = int(input())

for _ in range(n):
    tmp = list(input())
    count_a = 0
    count_b = 0
    for i in tmp:
        if i == "(":
            count_a += 1
        elif i == ")":
            count_b += 1
        if count_b > count_a:
            print("NO")
            break
    if count_b < count_a:
        print("NO")
    elif count_b == count_a:
        print("YES")

# n = int(input())

# for _ in range(n):
#     check = list(input())
#     count_a = 0
#     count_b = 0
#     sum = 0
#     for i in check:
#         if i == "(":
#             count_a += 1
#         elif i == ")":
#             count_b += 1
#         if count_a < count_b:
#             print("NO")
#             break
#     if count_a > count_b:
#         print("NO")
#     elif count_a == count_b:
#         print("YES")
