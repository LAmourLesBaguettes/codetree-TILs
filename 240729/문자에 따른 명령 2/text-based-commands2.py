# 방향 설정: 북(N), 동(E), 남(S), 서(W)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction_idx = 0  # 시작 방향은 북쪽

# 초기 위치 설정
x, y = 0, 0

# 명령어 입력 받기
commands = input().strip()

for command in commands:
    if command == 'L':
        direction_idx = (direction_idx - 1) % 4  # 왼쪽으로 회전
    elif command == 'R':
        direction_idx = (direction_idx + 1) % 4  # 오른쪽으로 회전
    elif command == 'F':
        dx, dy = directions[direction_idx]
        x += dx
        y += dy

# 최종 위치 출력
print(x, y)