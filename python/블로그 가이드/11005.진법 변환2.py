import sys
import string

sys.stdin = open("input.txt")

tmp = string.digits+string.ascii_lowercase


a, b = input().split()

print(int(a, int(b)))
