import sys

sys.stdin = open("input.txt")

# Y = 30 초 마다 10원
# M = 60 초 마다 15원 (if X < 60  15   x< 120 30)

n = int(input())
s = list(map(int, input().split()))
y = 0
m = 0
for i in s:
    y += i//30 * 10 + 10
    m += i//60 * 15 + 15


if y > m:
    print(f'M {m}')
elif y < m:
    print(f'Y {y}')
elif y == m:
    print(f'Y M {m}')

# f'저는 {s}를 좋아합니다. 하루 {n}잔 마셔요.'

