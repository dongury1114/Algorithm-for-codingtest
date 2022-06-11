import sys

sys.stdin = open("input.txt")

num = list(range(1, 21))

# change = [list(map(int, input().split()))for _ in range(10)]

tmp = []
for i in range(10):
    s, e = list(map(int, input().split()))

for j in range(s, e+1):
    tmp.append(num.pop(j))
print(tmp)
