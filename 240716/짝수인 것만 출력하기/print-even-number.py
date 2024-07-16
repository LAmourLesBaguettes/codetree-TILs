n = int(input())
elements = list(map(int, input().split()))

event_numbers = []

for element in elements:
    if element % 2 == 0:
        event_numbers.append(element)

print(" ".join(map(str, event_number)))