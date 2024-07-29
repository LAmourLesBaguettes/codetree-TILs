n = int(input())
tiles = {}  # 각 타일의 색상을 기록하기 위한 딕셔너리
current_position = 0

for _ in range(n):
    command = input().strip()
    steps = int(command[:-1])
    direction = command[-1]
    
    if direction == 'L':
        start = current_position - steps + 1
        end = current_position + 1
        current_position -= steps
    elif direction == 'R':
        start = current_position + 1
        end = current_position + steps + 1
        current_position += steps
    
    for i in range(start, end):
        if i in tiles:
            tiles[i] += 1
        else:
            tiles[i] = 1

white_tiles = 0
black_tiles = 0
gray_tiles = 0

for count in tiles.values():
    if count == 1:
        black_tiles += 1
    elif count >= 2:
        gray_tiles += 1

print(white_tiles, black_tiles, gray_tiles)