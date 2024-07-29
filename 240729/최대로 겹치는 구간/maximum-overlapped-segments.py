n = int(input())
events = []

for _ in range(n):
    x1, x2 = map(int, input().split())
    events.append((x1, 1))
    events.append((x2, -1))

events.sort(key=lambda x:(x[0], x[1]))

current_overlap = 0
max_overlap = 0

for event in events:
    current_overlap += event[1]
    max_overlap = max(max_overlap, current_overlap)

print(max_overlap)