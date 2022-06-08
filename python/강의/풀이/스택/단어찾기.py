import sys

sys.stdin = open("input.txt")

# tmp = []
# ---------------------------
# n = int(input())

# for i in range(n):
#     tmp.append(input())

# for i in range(n-1):
#     tmp.remove(input())
# print(tmp[0])
# ---------------------------

n = int(input())
p = dict()

for _ in range(n):
    word = input()
    p[word] = 1

for _ in range(n-1):
    word = input()
    p[word] = 0

for key, val in p.items():
    if val == 1:
        print(key)
        break

# ---------------------------
