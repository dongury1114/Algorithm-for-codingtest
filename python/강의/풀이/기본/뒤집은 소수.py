import sys

sys.stdin = open("input.txt")

n = int(input())
num = list(map(int, input().split()))


def isPrime(x):
    count = 0
    for i in range(2, x):
        if x % i == 0:
            count += 1
    if count == 0:
        return True


def reverse(x):
    reverse = int(str(x)[::-1])
    return reverse


for i in num:
    tmp = reverse(i)
    if isPrime(tmp) == True:
        print(tmp, end=" ")
