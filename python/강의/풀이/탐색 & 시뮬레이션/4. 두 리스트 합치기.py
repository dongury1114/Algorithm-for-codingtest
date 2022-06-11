import sys

sys.stdin = open("input.txt")

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

ans = N_list + M_list
ans.sort(reverse=False)
print(ans)
