from itertools import permutations

n, k = 3, 5

nums = list(range(1, n+1))
tmp = list(permutations(nums, n))
ans = tmp[k-1]
print(list(ans))
