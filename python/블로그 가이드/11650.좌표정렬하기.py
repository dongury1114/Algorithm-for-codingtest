import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline
n = int(input())
tmp = [list(map(int, input().split()))for _ in range(n)]

tmp.sort(key=lambda x: (x[0], x[1]))

for i in tmp:
    print(str(i[0]) + " " + str(i[1]))
