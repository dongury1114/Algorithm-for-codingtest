# 0 ->8
# 0x ->16

import sys

sys.stdin = open("input.txt")

word = list(input())

if word[1] == "x":
    tmp = "".join(word)
    print(int(tmp, 16))
else:
    if word[0] == "0":
        tmp = "".join(word)
        print(int(tmp, 8))

    else:
        tmp = "".join(word)
        print(int(tmp))
