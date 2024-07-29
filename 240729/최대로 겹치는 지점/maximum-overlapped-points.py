# 입력 처리
n = int(input())
events = []

# 각 선분의 시작과 끝을 이벤트로 추가
for _ in range(n):
    x1, x2 = map(int, input().split())
    events.append((x1, 1))  # 시작점: +1
    events.append((x2, -1)) # 끝점: -1

# 이벤트를 x좌표 순서로 정렬
events.sort()

# 스위핑하여 최대 겹치는 선분 수 계산
current_overlap = 0
max_overlap = 0

for event in events:
    current_overlap += event[1]
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)