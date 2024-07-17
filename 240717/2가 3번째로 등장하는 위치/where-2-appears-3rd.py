# Read the input values
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# Initialize a counter for occurrences of 2
count_2 = 0

# Iterate through the list to find the third occurrence of 2
for index in range(n):
    if numbers[index] == 2:
        count_2 += 1
        if count_2 == 3:
            print(index + 1)  # Output the 1-based index
            break