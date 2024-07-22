# 학생 정보를 저장할 리스트
students = []

# 5명의 학생 정보를 입력받아 리스트에 저장합니다.
for _ in range(5):
    name, height, weight = input().strip().split()
    height = int(height)
    weight = float(weight)
    students.append((name, height, weight))

# 이름순으로 정렬합니다.
students_sorted_by_name = sorted(students, key=lambda x: x[0])

# 키순으로 정렬합니다.
students_sorted_by_height = sorted(students, key=lambda x: -x[1])

# 이름순으로 정렬된 결과를 출력합니다.
print("name")
for student in students_sorted_by_name:
    print(f"{student[0]} {student[1]} {student[2]:.1f}")

print(" ")

# 키순으로 정렬된 결과를 출력합니다.
print("height")
for student in students_sorted_by_height:
    print(f"{student[0]} {student[1]} {student[2]:.1f}")