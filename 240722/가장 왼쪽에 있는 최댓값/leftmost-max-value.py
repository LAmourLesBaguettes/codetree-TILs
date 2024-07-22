N = int(input())

numbers = list(map(int, input().split()))

result_positions = []

current_end = len(numbers)

while current_end > 0 :
    max_value = max(numbers[:current_end])
    max_position = numbers[:current_end].index(max_value) + 1

    result_positions.append(max_position)

    current_end = max_position - 1

print(" ".join(map(str, result_positions)))