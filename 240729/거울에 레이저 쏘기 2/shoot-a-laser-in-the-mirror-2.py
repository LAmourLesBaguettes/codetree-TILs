def shoot_laser(n, mirrors, k):
    # 방향 설정
    # 위에서 아래로 (1 to N)
    if 1 <= k <= n:
        x, y = 0, k - 1
        dx, dy = 1, 0
    # 오른쪽에서 왼쪽으로 (N+1 to 2N)
    elif n < k <= 2 * n:
        x, y = k - n - 1, n - 1
        dx, dy = 0, -1
    # 아래에서 위로 (2N+1 to 3N)
    elif 2 * n < k <= 3 * n:
        x, y = n - 1, 3 * n - k
        dx, dy = -1, 0
    # 왼쪽에서 오른쪽으로 (3N+1 to 4N)
    elif 3 * n < k <= 4 * n:
        x, y = 4 * n - k, 0
        dx, dy = 0, 1

    while 0 <= x < n and 0 <= y < n:
        if mirrors[x][y] == '\\':
            dx, dy = dy, dx
        elif mirrors[x][y] == '/':
            dx, dy = -dy, -dx
        
        x += dx
        y += dy

    # 격자를 나간 위치
    if x == -1:
        return y + 1
    elif y == -1:
        return 4 * n - x
    elif x == n:
        return n + y + 1
    elif y == n:
        return 3 * n - x + 1

# 입력 받기
n = int(input())
mirrors = [input().strip() for _ in range(n)]
k = int(input())

# 결과 출력
result = shoot_laser(n, mirrors, k)
print(result)