def solution(price, money, count):
    sum = 0

    for i in range(1, count+1):
        sum += price * i
    ans = sum - money
    return ans if ans > 0 else 0
