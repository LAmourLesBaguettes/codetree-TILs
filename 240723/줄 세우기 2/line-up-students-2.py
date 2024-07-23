N = int(input())

students = []

for i in range(1, N + 1):
    h,w = map(int, input().split())
    students.append((h,w,i))

students.sort(key = lambda student: (student[0], -student[1]))

for student in students:
    print(student[0], student[1], student[2])