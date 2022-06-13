from collections import Counter

import sys

sys.stdin = open("input.txt")

arr = [int(input()) for _ in range(10)]
# val =
val = Counter(arr).most_common()

print(sum(arr)//10)
print(val[0][0])
