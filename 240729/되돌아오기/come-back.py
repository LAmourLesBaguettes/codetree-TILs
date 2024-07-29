# 입력 받기
n = int(input())
commands = [input().split() for _ in range(n)]

# 초기 위치와 시간
x, y = 0, 0
time = 0

# 방향 설정
direction_map = {
    'N': (0, 1),
    'S': (0, -1),
    'E': (1, 0),
    'W': (-1, 0)
}

# 이동 명령 처리
for direction, distance in commands:
    dx, dy = direction_map[direction]
    distance = int(distance)
    
    # 각 거리만큼 이동
    for _ in range(distance):
        x += dx
        y += dy
        time += 1
        
        # 처음으로 (0, 0)에 도달한 경우
        if x == 0 and y == 0:
            print(time)
            exit()

# 끝까지 도달하지 못한 경우
print(-1)