# 셔틀 운행 횟수 n, 셔틀 운행 간격 t, 한 셔틀에 탈 수 있는 최대 크루 수 m
# 크루가 대기열에 도착하는 시각을 모은 배열 timetable
# 셔틀은 09:00부터
n = 2
t = 10
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]

bus = []
tmp_timetable = []
tmp = 900
count = 0

for i in range(n):
    tmp += t
    bus.append(tmp)


for i in timetable:
    tmp_timetable.append(int(i[1]+i[3:]))

for i in tmp_timetable:
    if m - 1:
        break
