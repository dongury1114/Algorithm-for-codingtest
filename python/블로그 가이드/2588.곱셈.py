import sys

sys.stdin = open("input.txt")

a = int(input())
b = input()[::-1]
B = int(b[::-1])
for i in b:
    print(a * int(i))
print(a * B)
