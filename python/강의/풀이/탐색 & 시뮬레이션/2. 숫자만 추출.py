import sys

sys.stdin = open("input.txt")

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res*10+int(x)
print(res)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)

# n = input()
# tmp = []
# count = 0
# for i in n:
#     if 49 <= ord(i) <= 58:
#         tmp.append(str(i))
#         a = int("".join(tmp))

# for i in range(1, a+1):
#     if a % i == 0:
#         count += 1
# print(a)
# print(count)
