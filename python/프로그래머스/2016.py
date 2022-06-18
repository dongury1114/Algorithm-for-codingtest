from datetime import date

a, b = 5, 24

t = 'MON TUE WED THU FRI SAT SUN'.split()
print(t[date(2016, a, b).weekday()])
