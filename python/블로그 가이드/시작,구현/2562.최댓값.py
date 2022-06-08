from gettext import find
from operator import index
import sys

sys.stdin = open("input.txt")

tmp = []
Max = 0
idx = 0
for i in range(9):
    tmp.append(int(input()))

Max = max(tmp)
idx = tmp.index(max(tmp))
print(Max)
print(idx+1)
