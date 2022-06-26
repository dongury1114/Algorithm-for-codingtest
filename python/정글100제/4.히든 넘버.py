import sys

sys.stdin = open("input.txt")

n = int(input())
word = list(input())
tmp = []
for i in word:
    if i.isdecimal():
        tmp.append(i)

print(n)
print(word)
print(tmp)
