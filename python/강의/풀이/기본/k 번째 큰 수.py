from itertools import permutations
import sys

sys.stdin = open("input.txt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))
ans = []
tmp = list(map(list, (permutations(arr, 3))))

for i in range(len(tmp)):
    ans.append(sum(tmp[i]))
    ans2 = list(set(ans))
    ans2.sort()
print(ans2[-K])
