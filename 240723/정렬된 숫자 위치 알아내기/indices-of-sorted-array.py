N = int(input())

sequence = list(map(int,input().split()))

indexed_sequence = [(value, index) for index, value in enumerate(sequence)]

sorted_sequence = sorted(indexed_sequence)

result = [0] * N

for new_index, (value, original_index) in enumerate(sorted_sequence):
    result[original_index] = new_index + 1

print(" ".join(map(str, result)))