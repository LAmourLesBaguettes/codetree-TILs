class Student:
    def __init__ (self, ID = '', level = 0):
        self.ID = ID
        self.level = level

student1 = Student()

student1.ID = 'codetree'
student1.level = 10

ID2, level2 = tuple(input().split())

student2 = Student()

student2.ID = ID2
student2.level = int(level2)

print(f'user codetree lv {student1.level}')
print(f'user hello lv {student2.level}')