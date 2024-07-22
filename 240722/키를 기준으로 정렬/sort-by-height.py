n = int(input().strip())

people = []

for _ in range(n):
    name, height, weight = input().strip().split()
    height = int(height)
    weight = int(weight)
    people.append((name, height, weight))

people.sort(key = lamda x: x[1])

for person in people:
    print(person[0], person[1], person[2])