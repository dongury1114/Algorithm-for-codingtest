from itertools import combinations

nums = [6, 7, 8, 9]
count = 0

for n in nums:
    for i in range(2, n):
        if n % i == 0:
            pass
        else:
            print(True)
