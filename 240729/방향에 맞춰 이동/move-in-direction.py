# 이동 방향에 따른 dx, dy 설정
direction_map = {
    'N': (0, 1),  # 북쪽은 y 증가
    'S': (0, -1), # 남쪽은 y 감소
    'E': (1, 0),  # 동쪽은 x 증가
    'W': (-1, 0)  # 서쪽은 x 감소
}

# 입력 받기
n = int(input())
x, y = 0, 0  # 시작 위치

# 각 명령어에 따라 이동
for _ in range(n):
    direction, distance = input().split()
    distance = int(distance)
    dx, dy = direction_map[direction]
    x += dx * distance
    y += dy * distance

# 최종 위치 출력
print(x, y)