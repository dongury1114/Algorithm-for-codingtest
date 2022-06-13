import sys

sys.stdin = open("input.txt")

a = input()

if a == a[::-1]:
    print(1)
else:
    print(0)
