def solution(d, budget):
    count = 0
    d.sort()
    sum = 0

    for i in range(len(d)):
        sum += d[i]
        if sum <= budget:
            count += 1
    return count
