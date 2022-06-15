s = "P"
n = 15
tmp = list(s)
ttmp = []
ans = []
for i in tmp:
    a = ord(i) + n

    # if a > 90:
    #     ttmp.append(65+n-1)l
    # elif a > 122:
    #     ttmp.append(97+n-1)
    # elif a == 32:
    #     ttmp.append(32)
    # else:
    #     ttmp.append(a+n)

for i in ttmp:
    ans.append(chr(i))

print("".join(ans))
