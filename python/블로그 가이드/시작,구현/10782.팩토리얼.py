import sys

sys.stdin = open("input.txt")


def fac(n):
    if n == 1:
        return 1
    result = n * fac(n-1)
    return result


n = int(input())
print(fac(n))

# n = int(input())
# ans = 1
# for i in range(1, n+1):
#     ans *= i

# print(ans)
