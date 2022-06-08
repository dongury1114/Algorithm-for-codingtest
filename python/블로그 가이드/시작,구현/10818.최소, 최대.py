import sys

sys.stdin = open("input.txt")

n = int(input())
m = list(map(int, input().split()))

print(min(m), max(m))
