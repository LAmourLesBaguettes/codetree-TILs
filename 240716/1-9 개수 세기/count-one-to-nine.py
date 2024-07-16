def count_occurrences(n, elements):
    counts = [0] * 9
    for element in elements:
        if 1 <= element <= 9:
            counts[element - 1] += 1
    return counts

# Read input values
n = int(input())
elements = list(map(int, input().split()))

# Get the counts of each number from 1 to 9
result = count_occurrences(n, elements)

for i in range(1, 10):
    print(f"{result[i-1]}")