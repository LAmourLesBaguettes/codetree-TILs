# 입력 받기
n = int(input())
grid = []
for _ in range(n):
    grid.append(list(map(int, input().split())))

# 방향 설정 (상하좌우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

count = 0

# 격자의 각 칸에 대해 검사
for i in range(n):
    for j in range(n):
        # 현재 칸의 인접한 1의 개수를 센다
        adjacent_ones = 0
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:  # 격자 내에 있는지 확인
                if grid[ni][nj] == 1:
                    adjacent_ones += 1
        if adjacent_ones >= 3:
            count += 1

# 결과 출력
print(count)