# 명령 입력 받기
commands = input().strip()

# 초기 위치와 방향
x, y = 0, 0
direction = 0  # 0: 북, 1: 동, 2: 남, 3: 서
time = 0

# 방향 설정: 북(N), 동(E), 남(S), 서(W)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

# 명령 처리
for command in commands:
    if command == 'F':
        dx, dy = directions[direction]
        x += dx
        y += dy
    elif command == 'L':
        direction = (direction - 1) % 4
    elif command == 'R':
        direction = (direction + 1) % 4
    
    time += 1
    
    # 처음으로 (0, 0)에 도달한 경우
    if x == 0 and y == 0:
        print(time)
        exit()

# 끝까지 도달하지 못한 경우
print(-1)