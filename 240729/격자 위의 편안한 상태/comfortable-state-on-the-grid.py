# 입력 처리
N, M = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(M)]

# 격자 초기화
grid = [[0] * N for _ in range(N)]

# 방향 벡터 설정: 상, 하, 좌, 우
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

# 결과 리스트
results = []

# 명령 처리
for r, c in commands:
    # 색칠하기
    grid[r-1][c-1] = 1
    comfortable = 0
    
    # 주변 칸 확인
    count = 0
    for dr, dc in directions:
        nr, nc = r-1 + dr, c-1 + dc
        if 0 <= nr < N and 0 <= nc < N:
            count += grid[nr][nc]
    
    # '편안한 상태' 확인
    if count == 3:
        comfortable = 1
    results.append(comfortable)

# 결과 출력
for result in results:
    print(result)