def fill_spiral(n, m):
    # 격자 초기화
    grid = [[0] * m for _ in range(n)]
    
    # 방향: 오른쪽, 아래쪽, 왼쪽, 위쪽 순서
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0  # 초기 방향은 오른쪽
    x, y = 0, 0  # 시작 위치
    num = 1  # 시작 숫자
    
    for _ in range(n * m):
        grid[x][y] = num
        num += 1
        
        # 다음 위치 계산
        next_x, next_y = x + directions[current_direction][0], y + directions[current_direction][1]
        
        # 경계를 벗어나거나 이미 채워진 경우 방향 전환
        if not (0 <= next_x < n and 0 <= next_y < m and grid[next_x][next_y] == 0):
            current_direction = (current_direction + 1) % 4
            next_x, next_y = x + directions[current_direction][0], y + directions[current_direction][1]
        
        x, y = next_x, next_y
    
    return grid

# 입력 받기
n, m = map(int, input().split())

# 달팽이 채우기
grid = fill_spiral(n, m)

# 결과 출력
for row in grid:
    print(" ".join(map(str, row)))