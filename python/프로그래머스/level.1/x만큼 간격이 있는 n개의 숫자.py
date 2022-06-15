def solution(x, n):
    answer = []
    tmp = 0
    for i in range(n):
        tmp += x
        answer.append(tmp)
    return answer

# ----------------------------


def number_generator(x, n):
    return [i * x + x for i in range(n)]


print(number_generator(2, 5))
