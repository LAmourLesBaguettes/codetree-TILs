# 입력 처리
n = int(input())
events = []

# 시작점과 끝점 이벤트를 추가
for _ in range(n):
    x1, x2 = map(int, input().split())
    events.append((x1, 1))  # 시작점
    events.append((x2, -1)) # 끝점

# 이벤트를 x좌표 순서로, 같은 x좌표에서는 끝점이 시작점보다 먼저 오도록 정렬
events.sort(key=lambda x: (x[0], x[1]))

# 스위핑하여 최대 겹치는 선분 수 계산
current_overlap = 0
max_overlap = 0

for event in events:
    current_overlap += event[1]
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)