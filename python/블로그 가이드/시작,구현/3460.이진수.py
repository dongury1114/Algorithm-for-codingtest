import sys

# sys.stdin = open("input.txt")

n = int(input())


for i in range(n):
    ans = [0]
    count = 0
    two = list(bin(int(input()))[2:][::-1])
    for i in two:
        if i == '1':
            print(count, end=" ")
            count += 1
        else:
            count += 1
