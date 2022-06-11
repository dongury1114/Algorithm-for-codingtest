import sys

sys.stdin = open("input.txt")

n = int(input())

tree = list(list(map(int, input().split()))for _ in range(n))

# sol.2
a = int((n-1)/2)
ans = 0
# tree[0][a]
# tree[1][a+1] + tree[1][a] + tree[1][a-1]
# tree[2][a+2] + tree[2][a+1] + tree[2][a] + tree[2][a-1] + tree[2][a-2]
# tree[3][a+(4-3)] + tree[3][a] + tree[3][a-(4-3)]
# tree[4][a+(4-4)]

for i in range(n):
    tmp = []

    if a > i:
        tmp = tree[i]
        ans += sum(tmp[a-i:a+i+1])
    elif a == i:
        tmp = tree[i]
        ans += sum(tmp)
    elif a < i:
        tmp = tree[i]
        ans += sum(tmp[a-(n-i-1):a+(n-i-1)+1])
print(ans)
