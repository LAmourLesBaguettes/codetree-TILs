def generate_sequence(A1, A2):
    sequence = [A1, A2]
    for i in range(2, 10):
        next_value = sequence[i-1] + 2 * sequence[i-2]
        sequence.append(next_value)
    return sequence

# Read input values for A1 and A2
A1, A2 = map(int, input().split())

# Generate the sequence
result = generate_sequence(A1, A2)

# Print the sequence
print(" ".join(map(str, result)))