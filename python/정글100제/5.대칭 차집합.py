import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = set(a)
b = set(b)

a_length = len(list(a - b))
b_length = len(list(b - a))

print(a_length + b_length)
