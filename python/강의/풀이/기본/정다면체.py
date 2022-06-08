# import sys
# sys.stdin = open("input.txt", "r")
# n, m = map(int, input().split())
# cnt = [0]*(n+m+3)
# max = 0
# for i in range(1, n+1):
#     for j in range(1, m+1):
#         cnt[i+j] = cnt[i+j]+1

# for i in range(n+m+1):
#     if cnt[i] > max:
#         max = cnt[i]

# for i in range(n+m+1):
#     if cnt[i] == max:
#         print(i, end=' ')


import sys
from collections import Counter
sys.stdin = open("input.txt")

n, m = map(int, input().split())
max = 0
n_list = list(range(1, n+1))
m_list = list(range(1, m+1))
tmp = []
rst = []
for i in n_list:
    for j in m_list:
        tmp.append(i+j)

ans = list(map(list, Counter(tmp).most_common()))

max = ans[0][1]

for i in range(len(ans)):
    if ans[i][1] == max:
        rst.append(ans[i][0])

for i in rst:
    print(i, end=" ")
