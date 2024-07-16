def count_tens_place(numbers):
    counts = [0] * 10
    for number in numbers:
        if number == 0:
            continue
        tens_place = number // 10
        if tens_place > 0:
            counts[tens_place] += 1
    return counts[1:]  # we skip the first element (index 0) as we don't need the count for 0

# Read input values
numbers = list(map(int, input().split()))

# Get the counts of each tens place digit
result = count_tens_place(numbers)

# Print the results in the specified format
for i in range(1, 10):
    print(f"{i} - {result[i-1]}")