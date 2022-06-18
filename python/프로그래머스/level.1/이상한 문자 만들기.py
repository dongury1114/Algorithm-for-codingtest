def solution(s):
    ans = []
    s = list(s.split(" "))
    for i in s:
        for j in range(len(i)):
            if j % 2 == 0:
                ans.append(i[j].upper())
            else:
                ans.append(i[j].lower())
        ans.append(" ")
    ans = ans[:-1]

    return "".join(ans)
