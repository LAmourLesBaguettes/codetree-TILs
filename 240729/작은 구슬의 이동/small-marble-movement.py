# 입력 처리
n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# 방향 설정: 상(U), 하(D), 좌(L), 우(R)
directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
opposite_directions = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}

# 초기 방향
dx, dy = directions[d]

# t초 동안 이동
for _ in range(t):
    # 다음 위치 계산
    nr, nc = r + dx, c + dy
    
    # 벽에 부딪히면 방향 반대로 전환
    if nr < 1 or nr > n or nc < 1 or nc > n:
        d = opposite_directions[d]
        dx, dy = directions[d]
        nr, nc = r + dx, c + dy  # 반대 방향으로 재계산
    
    # 위치 업데이트
    r, c = nr, nc

# 결과 출력
print(r, c)