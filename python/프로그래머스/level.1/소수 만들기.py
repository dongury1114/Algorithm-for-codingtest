from itertools import combinations
nums = [1, 2, 3, 4]

a = (1, 2, 3)

tmp = list(combinations(nums, 3))
sums = []
count = 0
for i in tmp:
    sums.append(sum(i))

for i in sums:
    for j in range(2, int((i**0.5))+1):
        if i % j == 0:
            break
    else:
        count += 1
print(count)
