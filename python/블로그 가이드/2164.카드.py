from collections import deque
import sys
sys.stdin = open("input.txt")

n = int(input())
card = deque(range(1, n+1))

while len(card) > 1:
    card.popleft()
    card.rotate(-1)
print(card[0])
