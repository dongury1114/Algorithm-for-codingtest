import sys
from collections import Counter
sys.stdin = open("input.txt")

n = int(input())
num = list(list(map(int, input().split()))for _ in range(n))
tmp = []

for i in num:
    a = list(map(list, Counter(i).most_common()))
    if a[0][1] == 3:
        tmp.append(10000 + a[0][0] * 1000)
    elif a[0][1] == 2:
        tmp.append(1000 + a[0][0] * 100)
    else:
        tmp.append(max(a[0]) * 100)
print(max(tmp))
