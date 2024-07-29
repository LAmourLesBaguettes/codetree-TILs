# 입력 받기
n, m = map(int, input().split())

# n * m 크기의 격자 초기화
grid = [[0] * m for _ in range(n)]

# 달팽이 방향 설정 (오른쪽, 아래쪽, 왼쪽, 위쪽)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

x, y = 0, 0  # 시작 위치
direction = 0  # 현재 방향 (0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽)
num = 1  # 시작 숫자

for _ in range(n * m):
    grid[x][y] = num
    num += 1
    
    # 다음 위치 계산
    nx, ny = x + dx[direction], y + dy[direction]
    
    # 다음 위치가 격자 내부이고 아직 숫자가 채워지지 않은 경우
    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0:
        x, y = nx, ny
    else:  # 방향 전환
        direction = (direction + 1) % 4
        x += dx[direction]
        y += dy[direction]

# 결과 출력
for row in grid:
    print(' '.join(map(str, row)))