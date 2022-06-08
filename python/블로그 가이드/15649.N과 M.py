from itertools import permutations

N, M = 4, 2  # for test

# N, M = map(int, input().split())

arr = [str(i+1) for i in range(N)]

print(arr)

for i in list(permutations(arr, M)):
    print(" ".join(i))
