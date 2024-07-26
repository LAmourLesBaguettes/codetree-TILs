days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

m1, d1, m2, d2 = map(int, in put().split())

day_count = days_in_month[m1] - d1 + 1

if m1 == m2:
    day_count = d2 - d1 + 1
else:
    for month in range(m1 + 1, m2):
        day_count += days_in_month[month]
    day_count += d2

print(day_count)