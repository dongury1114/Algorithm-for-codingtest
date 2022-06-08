from collections import deque
import sys
sys.stdin = open("input.txt")

n, k = map(int, input().split())

tmp = deque(range(1, n+1))

ans = []

while tmp:
    tmp.rotate(-k+1)
    ans.append(tmp.popleft())
print('<%s>' % ', '.join(map(str, ans)))
