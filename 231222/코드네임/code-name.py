class Unit:
    def __init__(self, code, grade):
        self.code = code
        self.grade = grade

if __name__ == '__main__':
    units = []
    for _ in range(5):
        code, grade = input().split()
        units.append(Unit(code, int(grade)))

    min_unit = min(units, key=lambda x:x.grade)

    print(min_unit.code, min_unit.grade)