import sys

sys.stdin = open("input.txt")

a = int(input(), 2)
print(oct(a)[2:])
