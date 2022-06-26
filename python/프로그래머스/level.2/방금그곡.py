m = "CC#BCC#BCC#BCC#B"
musicinfos = ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
tmp = []
ttmp = []
for i in musicinfos:
    i = list(list(i.split(",")))
    tmp.append(i)

for i in range(len(musicinfos)):
    ans = list(tmp[i][3])
    ans.sort()
    c_ans = "".join(ans)
    if m in c_ans or c_ans in m:
        print(tmp[i][2])
