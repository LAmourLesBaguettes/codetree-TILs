# 첫 번째 줄에 학생의 수 N을 입력받습니다.
n = int(input().strip())

# 학생 정보를 저장할 리스트
students = []

# 각 학생의 정보를 입력받아 리스트에 저장합니다.
for i in range(n):
    h, w = map(int, input().strip().split())
    students.append((h, w, i + 1))  # i + 1은 학생의 번호

# 정렬 기준: 키 (내림차순) -> 몸무게 (내림차순) -> 번호 (오름차순)
students.sort(key=lambda x: (-x[0], -x[1], x[2]))

# 정렬된 결과를 출력합니다.
for student in students:
    print(student[0], student[1], student[2])