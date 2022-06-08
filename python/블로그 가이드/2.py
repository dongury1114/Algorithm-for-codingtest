from itertools import combinations

nums = [1, 2, 3, 4]
count = 0
check = 0


def prime(n):
    global count
    global check
    for i in range(2, (n//2)+1):
        if n % i == 0:
            check += 1
    if check == 0:
        return True


ans = list(list(combinations(nums, 3)))
tmp = []

for i in ans:
    tmp.append(sum(i))

for i in tmp:
    if prime(i) == True:
        count += 1
print(count)
