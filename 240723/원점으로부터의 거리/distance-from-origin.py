N = int(input())

points = []

for i in range(1, 1+N):
    x, y = map(int, input().split())
    manhattan_distance = abs(x) + abs(y)
    points.append((manhattan_distance, i, x, y))

points.sort()

for point in points:
    print(point[1])