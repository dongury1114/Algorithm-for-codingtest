from collections import Counter
import sys
from collections import Counter
sys.stdin = open("input.txt")

n = int(input())
tmp = list(map(int, input().split()))
average = round(sum(tmp)/n)
# for i in Counter(tmp).mos:
ans = []
# for i in tmp:
# ans.append(abs(average - i))
a = list(map(list, Counter(tmp).most_common()))
for i in range(n):
    ans.append(list(a[i][0]-average, a[i][1]))
print(a)
# print(average, i, sep=" ")
