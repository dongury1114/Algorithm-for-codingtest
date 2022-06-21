from math import factorial

n, k = 3, 5

answer = []
nums = list(range(1, n+1))

while n != 0:
    fac = factorial(n-1)
    answer.append(nums.pop((k-1)//fac))
    n -= 1
    k %= fac
print(answer)
