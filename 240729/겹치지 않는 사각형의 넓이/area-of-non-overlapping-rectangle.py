def rectangle_area(x1, y1, x2, y2):
    return (x2 - x1) * (y2 - y1)

def intersection_area(ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
    ix1 = max(ax1, bx1)
    iy1 = max(ay1, by1)
    ix2 = min(ax2, bx2)
    iy2 = min(ay2, by2)
    
    if ix1 < ix2 and iy1 < iy2:
        return rectangle_area(ix1, iy1, ix2, iy2)
    return 0

# 입력 받기
ax1, ay1, ax2, ay2 = map(int, input().split())
bx1, by1, bx2, by2 = map(int, input().split())
mx1, my1, mx2, my2 = map(int, input().split())

# 직사각형 A와 M의 교집합 면적 계산
a_covered = intersection_area(ax1, ay1, ax2, ay2, mx1, my1, mx2, my2)
# 직사각형 B와 M의 교집합 면적 계산
b_covered = intersection_area(bx1, by1, bx2, by2, mx1, my1, mx2, my2)

# 남은 면적 계산
remaining_a = rectangle_area(ax1, ay1, ax2, ay2) - a_covered
remaining_b = rectangle_area(bx1, by1, bx2, by2) - b_covered

# 출력
print(remaining_a + remaining_b)