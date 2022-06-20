import sys

sys.stdin = open("input.txt")

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

# sol.1
# tmp = []
# for i in range(1, m+1):
#     if i % (k+1) != 0:
#         tmp.append(nums[-1])
#     else:
#         tmp.append(nums[-2])
# print(sum(tmp))

# sol.2
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += nums[-1]
