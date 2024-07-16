# 학생 점수를 입력 받음
scores = list(map(int, input().split()))

# 점수대별 학생 수를 저장할 리스트 초기화 (0~9, 10~19, ..., 90~99, 100)
counts = [0] * 11

# 점수대별 학생 수 세기
for score in scores:
    if score == 0:
        break
    if score == 100:
        counts[10] += 1
    else:
        counts[score // 10] += 1

# 결과 출력 (10점 미만의 점수는 세지 않음)
for i in range(10, -1, -1):
    if i == 10:
        print(f"100 - {counts[i]}")
    else:
        if i != 0:  # 10점 미만의 점수는 세지 않음
            print(f"{i * 10} - {counts[i]}")