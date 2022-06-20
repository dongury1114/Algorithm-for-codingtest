def solution(n):
    tmp = []
    count = 0
    total = 0
    for i in range(1, n+1):
        for j in range(i, n+1):
            tmp.append(j)
            total = sum(tmp)

            if total > n:
                total = 0
                tmp = []
                break

            elif total == n:
                count += 1
                total = 0
                tmp = []
                break
    return count


def solution(n):
    count = 0
    for i in range(1, n + 1):
        total = 0
    while total < n:
        total += i
        i += 1
    if total == n:
        count += 1

    return count
