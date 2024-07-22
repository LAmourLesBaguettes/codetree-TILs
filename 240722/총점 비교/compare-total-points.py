# 첫 번째 줄에 정수 n을 입력받습니다.
n = int(input().strip())

# 학생 정보를 저장할 리스트
students = []

# 각 학생의 정보를 입력받아 리스트에 저장합니다.
for _ in range(n):
    name, score1, score2, score3 = input().strip().split()
    score1 = int(score1)
    score2 = int(score2)
    score3 = int(score3)
    total_score = score1 + score2 + score3
    students.append((name, score1, score2, score3, total_score))

# 총점이 낮은 순으로 정렬합니다.
students.sort(key=lambda x: x[4])

# 정렬된 결과를 출력합니다.
for student in students:
    print(student[0], student[1], student[2], student[3])