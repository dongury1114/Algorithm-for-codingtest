import sys

sys.stdin = open("input.txt")

n = int(input())
m = list(map(int, input()))

print(sum(m))
