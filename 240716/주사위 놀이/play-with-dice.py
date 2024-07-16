def count_dice_rolls(rolls):
    counts = [0] * 6
    for roll in rolls:
        if 1 <= roll <= 6:
            counts[roll - 1] += 1
    return counts

# Read the input
rolls = list(map(int, input().split()))

# Get the counts of each dice number from 1 to 6
result = count_dice_rolls(rolls)

# Print the results in the specified format
for i in range(1, 7):
    print(f"{i} - {result[i-1]}")