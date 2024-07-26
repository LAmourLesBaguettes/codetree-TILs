# 각 달의 일수를 저장한 리스트 (0번 인덱스는 사용하지 않음)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일 리스트 (인덱스 0은 일요일, 1은 월요일, ..., 6은 토요일)
week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

m1, d1, m2, d2 = map(int, input().split())

days_count = 0

if m1 == m2:
    days_count = d2 - d1
else:
    days_count += days_in_month[m1] - d1
    for month in range(m1 + 1, m2):
        days_count += days_in_month[month]
    days_count += d2

start_day_index = 1
final_day_index = (start_day_index + days_count)%7

print(week_days[final_day_index])