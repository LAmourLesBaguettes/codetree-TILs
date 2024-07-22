# 첫 번째 줄에 학생의 수 N을 입력받습니다.
n = int(input().strip())

# 학생 정보를 저장할 리스트
students = []

# 각 학생의 정보를 입력받아 리스트에 저장합니다.
for _ in range(n):
    name, height, weight = input().strip().split()
    height = int(height)
    weight = int(weight)
    students.append((name, height, weight))

# 키를 기준으로 오름차순 정렬, 키가 동일한 경우 몸무게를 기준으로 내림차순 정렬
students.sort(key=lambda x: (x[1], -x[2]))

# 정렬된 결과를 출력합니다.
for student in students:
    print(f"{student[0]} {student[1]} {student[2]}")