from collections import Counter

import sys

sys.stdin = open("input.txt")

word = input()
WORD = word.upper()

ans = Counter(WORD).mos
tmp = ans.most_common(2)
if len(WORD) == 1:
    print(WORD)
else:
    if tmp[0][1] == tmp[1][1]:
        print("?")
    else:
        print(tmp[0][0])

# test = input().upper()
# count = Counter(test)
# max_value = max(list(count.values()))
# max1 = count.most_common(2)

# if len(max1) == 1:
#     print(test)
# else:
#     if max1[0][1] == max1[1][1]:
#         print("?")
#     else:
#         print(max1[0][0])
