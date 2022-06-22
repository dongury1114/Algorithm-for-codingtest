def solution(n, words):
    tmp = []

    for i in range(len(words)):
        if not tmp:
            tmp.append(words[i].lower())
        elif tmp:
            if len(words[i]) == 1:
                return [i % n + 1, i//n + 1]
                break
            elif words[i] in tmp:
                return [i % n + 1, i//n + 1]
                break

            elif tmp[-1][-1] != words[i][0]:
                return [i % n + 1, i//n + 1]
                break
            elif len(words)-1 == len(tmp):
                return [0, 0]
                break
            else:
                tmp.append(words[i].lower())


def solution(n, words):
    answer = [0, 0]
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i] or len(words[i]) == 1:
            return [(i % n)+1, (i//n)+1]
    return answer
