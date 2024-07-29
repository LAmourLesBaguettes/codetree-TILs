n = int(input())
rectangles = []

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    rectangles.append((x1, y1, y2, 1))  # 시작점 (열기)
    rectangles.append((x2, y1, y2, -1)) # 끝점 (닫기)

# x 좌표에 따라 정렬하되, 같은 x에서는 닫는 쪽이 우선
rectangles.sort()

total_area = 0
current_y_ranges = []
previous_x = -float('inf')

def calculate_y_coverage(y_ranges):
    y_ranges.sort()
    total_length = 0
    current_start, current_end = -float('inf'), -float('inf')
    
    for start, end in y_ranges:
        if start > current_end:
            total_length += current_end - current_start
            current_start, current_end = start, end
        else:
            current_end = max(current_end, end)
    
    total_length += current_end - current_start
    return total_length

for x, y1, y2, type in rectangles:
    # 이전 x에서 지금 x까지의 너비에 대한 y 커버리지 계산
    if current_y_ranges:
        total_area += (x - previous_x) * calculate_y_coverage(current_y_ranges)
    
    if type == 1: # 열기
        current_y_ranges.append((y1, y2))
    else: # 닫기
        current_y_ranges.remove((y1, y2))
    
    previous_x = x

print(total_area)