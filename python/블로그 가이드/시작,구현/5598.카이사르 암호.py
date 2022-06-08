import sys

sys.stdin = open("input.txt")

# A 부터는 3만 더하고 X, Y, Z는 따로 처리

tmp = []
ans = []
for i in input():
    tmp.append(ord(i))

for i in tmp:
    if i >= 68:
        ans.append(chr(i-3))
    else:
        ans.append(chr(i+23))
print(''.join(ans))
