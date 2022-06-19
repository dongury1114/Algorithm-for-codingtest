def solution(answers):

    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    count_s1 = 0
    count_s2 = 0
    count_s3 = 0

    for i in range(len(answers)):
        a1 = i % 5
        a2 = i % 8
        a3 = i % 10
        if s1[a1] == answers[i]:
            count_s1 += 1
        if s2[a2] == answers[i]:
            count_s2 += 1
        if s3[a3] == answers[i]:
            count_s3 += 1
    tmp = max(count_s1, count_s2, count_s3)
    ans = []

    if tmp == count_s1:
        ans.append(1)
    if tmp == count_s2:
        ans.append(2)
    if tmp == count_s3:
        ans.append(3)

    return ans


def solution(answers):
    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    result = []

    for i, answer in enumerate(answers):
        if answer == pattern1[i % 5]:
            score[0] += 1
        if answer == pattern1[i % 8]:
            score[1] += 1
        if answer == pattern1[i % 10]:
            score[2] += 1

    for i, s in enumerate(score):
        if s == max(score):
            result.append(i+1)
    print(result)
