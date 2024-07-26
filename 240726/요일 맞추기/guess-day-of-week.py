# 각 달의 일수를 저장한 리스트 (0번 인덱스는 사용하지 않음)
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 요일 리스트 (인덱스 0은 일요일, 1은 월요일, ..., 6은 토요일)
week_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]

# 입력 받기
m1, d1, m2, d2 = map(int, input().split())

# 첫 번째 날짜로부터 두 번째 날짜까지의 총 일수 계산
days_count = 0

# 시작 월과 종료 월이 같은 경우
if m1 == m2:
    days_count = d2 - d1
else:
    # 시작 월의 남은 일수
    days_count += days_in_month[m1] - d1
    # 중간 월들의 일수
    for month in range(m1 + 1, m2):
        days_count += days_in_month[month]
    # 종료 월의 일수
    days_count += d2

# 첫 번째 날짜가 월요일이므로
# 시작점이 월요일 (인덱스 1)에서 days_count만큼 이동한 요일을 계산
start_day_index = 1
final_day_index = (start_day_index + days_count) % 7

# 결과 출력
print(week_days[final_day_index])