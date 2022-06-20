import math

progresses = [93, 30, 55]
speeds = [1, 30, 5]


tmp = []
ttmp = []
ans = []
count = 0
for i in progresses:
    tmp.append(100 - i)

for i in range(len(speeds)):
    ttmp.append(math.ceil(tmp[i]/speeds[i]))
