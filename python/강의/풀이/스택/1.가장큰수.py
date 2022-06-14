import sys

sys.stdin = open("input.txt")

n, m = map(int, input().split())

stack = []
n = list(map(int, str(n)))

for i in n:
    while stack and m > 0 and stack[-1] < i:
        stack.pop()
        m -= 1
    stack.append(i)
if m != 0:
    stack = stack[:-m]
ans = "".join(map(str, stack))
print(ans)
# for i in n:
#     while stack and m > 0 and stack[-1] < i:
#         stack.pop()
#         m -= 1
#     stack.append(i)
# if m != 0:
#     stack = stack[:-m]
# res = "".join(map(str, stack))
# print(res)
