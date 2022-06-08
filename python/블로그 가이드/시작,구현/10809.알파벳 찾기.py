import sys

sys.stdin = open("input.txt")

word = input()
tmp = []
ans = []
for i in word:
    tmp.append(ord(i))
for i in range(97, 123):
    if i in tmp:
        ans.append(tmp.index(i))
    else:
        ans.append(-1)
ans = ' '.join(map(str, ans))

print(ans)
