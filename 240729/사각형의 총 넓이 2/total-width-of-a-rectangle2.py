def calculate_total_area(n, rectangles):
    # 격자의 크기는 -100부터 100까지이므로, 인덱스 접근을 용이하게 하기 위해 +100 해준다.
    grid = [[0] * 201 for _ in range(201)]
    
    # 모든 직사각형에 대해 격자를 채우기
    for x1, y1, x2, y2 in rectangles:
        for x in range(x1 + 100, x2 + 100):
            for y in range(y1 + 100, y2 + 100):
                grid[x][y] = 1  # 이 격자가 사용되었음을 표시
    
    # 격자를 탐색하여 사용된 부분의 개수를 세기
    total_area = 0
    for row in grid:
        total_area += sum(row)
    
    return total_area

# 입력 받기
n = int(input())
rectangles = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, x2, y2))

# 면적 계산 및 출력
total_area = calculate_total_area(n, rectangles)
print(total_area)