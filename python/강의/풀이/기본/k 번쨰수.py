import sys

sys.stdin = open("input.txt")

T = int(input())

for t in range(T):
    N, s, e, k = map(int, input().split())
    a = list()
