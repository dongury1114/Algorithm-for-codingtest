import sys

sys.stdin = open("input.txt")

n = int(input())
m = list(map(int, input().split()))
M = max(m)
tmp = []

for i in m:
    tmp.append(i/M*100)

print(sum(tmp)/len(tmp))
