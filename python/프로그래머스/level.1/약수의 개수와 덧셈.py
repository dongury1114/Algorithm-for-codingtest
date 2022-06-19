def solution(left, right):
    tmp = list(range(left, right + 1))
    ans = 0

    for i in tmp:
        count = 0
        div = []

        for j in range(1, i+1):
            if i % j == 0:
                div.append(j)
                count += 1
        if count % 2 == 0:
            ans += i
        else:
            ans -= i
    return ans


def solution(left, right):
    tmp = list(range(left, right + 1))
    ans = 0

    for i in tmp:
        if int(i**0.5) == i**0.5:
            ans -= i
        else:
            ans += i
    return ans
