import sys
from itertools import permutations
sys.stdin = open("input.txt")

N, M = map(int, input().split())

tmp = list(map(str, range(1, N+1)))

for i in list(permutations(tmp, M)):
    print(" ".join(i))
