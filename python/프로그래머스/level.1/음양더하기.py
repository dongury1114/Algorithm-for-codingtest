def solution(absolutes, signs):
    tmp = []
    ans = []
    for i in signs:
        if i == True:
            tmp.append(1)
        elif i == False:
            tmp.append(-1)

    for i in range(len(absolutes)):
        ans.append(absolutes[i]*tmp[i])
    return sum(ans)
