import sys
sys.stdin = open("input.txt", "r")


def digit_sum(x):
    a = 0
    tmp = list(map(int, str(x)))
    a = sum(tmp)
    return a


n = int(input())
a = list(map(int, input().split()))
res = 0
max = 0

for x in a:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x
print(res)

# import sys
# sys.stdin=open("input.txt", "r")0
# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10
#         x=x//10
#     return sum

# n=int(input())
# a=list(map(int, input().split()))
# res=0
# max=-2147000000
# for x in a:
#     tot=digit_sum(x)
#     if tot>max:
#         max=tot
#         res=x
# print(res)
