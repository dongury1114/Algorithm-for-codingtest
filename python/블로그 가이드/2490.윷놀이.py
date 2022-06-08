from itertools import count
import sys
sys.stdin = open("input.txt")

tmp = [list(map(int, input().split()))for _ in range(3)]

for i in tmp:
    i.count(1)
    if i.count(1) == 0:
        print("D")
    elif i.count(1) == 3:
        print("A")
    elif i.count(1) == 2:
        print("B")
    elif i.count(1) == 1:
        print("C")
    elif i.count(1) == 4:
        print("E")
