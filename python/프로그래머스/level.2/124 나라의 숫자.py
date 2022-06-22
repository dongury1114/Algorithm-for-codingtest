# n = 1
# n = 2
# n = 3
n = 44

answer = ''
while n:
    if n % 3:
        answer += str(n % 3)
        n //= 3
    else:
        answer += "4"
        n = n//3 - 1
print(answer[::-1])
