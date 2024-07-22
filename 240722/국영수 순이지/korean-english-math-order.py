n = int(input().strip())

students = []

for _ in range(n):
    name, korean, english, math = input().strip().split()
    korean = int(korean)
    english = int(english)
    math = int(math)
    students.append((name, korean, english, math))

students.sort(key=lambda x:(-x[1], -x[2], -x[3]))

for student in students:
    print(student[0], student[1], student[2], student[3])