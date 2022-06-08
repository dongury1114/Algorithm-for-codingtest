import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

n = int(input())

tmp = [list(input().split())for _ in range(n)]

tmp.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
for i in tmp:
    print(i[0])
