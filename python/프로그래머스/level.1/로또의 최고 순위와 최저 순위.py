def solution(lottos, win_nums):
    count = 0  # 같은게 있는 갯수
    zero = lottos.count(0)

    for i in lottos:
        if i in win_nums:
            count += 1

    Max, Min = 7-count, 7-(count + zero)
    Max = 6 if Max == 7 else 7 - count
    if Min == 7:
        Min = 6
    return [Min, Max]


def solution(lottos, win_nums):
    zero = lottos.count(0)
    a = [x for x in lottos if x in win_nums]
    max = zero+len(a)
    min = len(a)

    max = 7 - max if max >= 1 else 6
    min = 7 - min if min >= 1 else 6
    return [max, min]
