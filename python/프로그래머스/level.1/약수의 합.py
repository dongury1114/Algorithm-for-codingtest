def solution(n):
    tmp = []

    for i in range(1, (n//2+1)):
        if n % i == 0:
            tmp.append(i)

    return sum(tmp)+n

# 절반만 하면 본인을 제외한 약수들 모두가 나옴
