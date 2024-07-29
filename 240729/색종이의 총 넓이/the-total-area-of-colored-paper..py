def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    positions = [(int(data[i*2+1]), int(data[i*2+2])) for i in range(N)]
    
    # 격자 생성: 색종이가 차지할 수 있는 전체 범위
    grid = [[0] * 201 for _ in range(201)]
    
    # 색종이 넓이 8x8, 각 색종이를 격자에 표시
    for x, y in positions:
        for i in range(x + 100, x + 100 + 8):
            for j in range(y + 100, y + 100 + 8):
                grid[i][j] = 1  # 이 부분을 색종이가 차지
    
    # 총 넓이 계산
    total_area = sum(sum(row) for row in grid)
    
    print(total_area)

if __name__ == "__main__":
    main()